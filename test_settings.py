INSTALLED_APPS = (
    'dau',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dau_testing',
    }
}
SECRET_KEY = "dau_secret_key_for_testing"