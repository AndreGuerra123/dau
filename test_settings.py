INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'dau'
]

DJANGO_AUTO_USER = [
    {
        'username':'admin',
        'email':'admin@admin.com',
        'password':'adminpass',
        'is_superuser':True,
        'is_staff':True,
        'is_active':True
    }
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dau_testing',
    }
}
SECRET_KEY = "dau_secret_key_for_testing"