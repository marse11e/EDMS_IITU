from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from datetime import date, datetime, timedelta


class Document(models.Model):
    filename = models.CharField(max_length=200, verbose_name="Имя файла")
    filepath = models.FilePathField(path=settings.MEDIA_ROOT, null=True, verbose_name="Путь к файлу")
    date = models.DateField(verbose_name="Дата")
    description = models.TextField(null=True, verbose_name="Описание")
    signs_number = models.PositiveIntegerField(default=0, verbose_name="Количество подписей")
    signed = models.PositiveIntegerField(default=0, verbose_name="Подписано")
    status = models.CharField(max_length=25, default='В процессе', verbose_name="Статус")

    def __str__(self):
        return self.filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    notifications = models.TextField(blank=True, verbose_name="Уведомления")
    approved = models.BooleanField(default=False, verbose_name="Одобрен")
    personal_files = models.ManyToManyField(Document, related_name='owners', blank=True, verbose_name="Личные документы")
    files_to_review = models.ManyToManyField(Document, related_name='reviewers', blank=True,
                                             verbose_name="Документы для рецензирования")

    def __str__(self):
        return str(self.user)

    def get_statistics(self):
        deadlines_count = 0
        personal_files = Document.objects.filter(owners__user=self.user)
        files_to_review = Document.objects.filter(reviewers__user=self.user, status='В процессе')

        for document in files_to_review:
            deadline = date.fromisoformat(str(document.date))
            if deadline - datetime.now().date() <= timedelta(days=1) and document.status != 'Готов':
                deadlines_count += 1

        personal_context = {
            'deadlines': deadlines_count,
            'files_to_sign': len(files_to_review),
            'personal_files': len(personal_files),
            'my_files': personal_files,
            'review_files': files_to_review
        }
        return personal_context

    def get_group_persons(self):
        persons = set()
        for group in self.user.groups.all():
            users = User.objects.filter(groups=Group.objects.get(name=group.name))
            for user in users:
                persons.add(user.username)
        return persons

    def get_notifications(self):
        notifications = self.notifications.split('\n')
        notifications = [n.strip() for n in notifications if n.strip()]
        self.notifications = ''
        self.save()
        return notifications

    def update(self, username=None, email=None, password=None):
        if username:
            self.user.username = username
        if email:
            self.user.email = email
        if password:
            self.user.set_password(password)
        self.user.save()


class DiscussionText(models.Model):
    author = models.CharField(max_length=200, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    publish_date = models.DateField(verbose_name="Дата публикации")
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, verbose_name="Документ")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
