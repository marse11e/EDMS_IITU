from django.urls import path

from . import views2

app_name = 'web'
urlpatterns = [
    path('', views2.index, name='index'),
    path('login/', views2.log_in, name='login'),
    path('logout/', views2.log_out, name='logout'),
    path('signup/', views2.signup, name='signup'),
    path('user/', views2.user_page, name='user'),
    path('group/', views2.group_review, name='group'),
    path('<str:username>/approve/', views2.approve, name='approve'),
    path('<str:username>/remove/', views2.remove_user, name='remove_user'),
    path('update-account/', views2.update_account, name='update_account'),
    path('new-post/', views2.new_post, name='new-post'),
    path('add-post/', views2.add_new_document, name='add-post'),
    path('cabinet/', views2.show_documents, name='cabinet'),
    path('search/', views2.search, name='search'),
    path('<str:filename>/sign/', views2.sign, name='document_sign'),
    path('<str:filename>/edit/', views2.edit_document, name='document_edit'),
    path('<str:filename>/cancel/', views2.cancel, name='document_cancel'),
    path('<str:filename>/apply/', views2.apply_edits, name='document_edit_apply'),
    path('<str:filename>/review/', views2.review, name='document_review'),
    path('<str:filename>/review/new/', views2.new_review, name='new_document_review'),
    path('<str:filename>/review/download/', views2.download, name='new_document_download'),
    path('.well-known/acme-challenge/wl02Bwi2-dCe4gkHdf5kP0XM3m-kuKq8WgVMjGvv2AM',
         views2.certbot_auth, name='certbot_auth')
]
