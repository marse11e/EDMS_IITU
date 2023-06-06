from documents.logging_dir.setup_logger import info_logger, error_logger


def init_logger(func):
    def wrapper(self, user_id, path, primary=False):
        try:
            func(self, user_id, path, primary)
        except ValueError as error:
            error_logger.error(f'Ошибка: {str(error)}, произошла с файлом: {path}')
        else:
            if primary:
                info_logger.info(f'Файл {path} был инициализирован')
    return wrapper


def sign_logger(func):
    def wrapper(self):
        try:
            func(self)
        except ValueError as error:
            error_logger.error(f'Ошибка: {str(error)}, произошла с файлом: {self.path}')
        else:
            info_logger.info(f'Файл {self.path} был подписан пользователем {self.user_id}')
    return wrapper
