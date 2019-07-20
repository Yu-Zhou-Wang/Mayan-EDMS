from __future__ import unicode_literals

# Default in YAML format
BOOTSTRAP_SETTING_LIST = (
    {'name': 'ALLOWED_HOSTS', 'default': "['127.0.0.1', 'localhost', '[::1]']"},
    {'name': 'APPEND_SLASH'},
    {'name': 'AUTH_PASSWORD_VALIDATORS'},
    {'name': 'COMMON_DISABLED_APPS'},
    {'name': 'COMMON_EXTRA_APPS'},
    {'name': 'DATA_UPLOAD_MAX_MEMORY_SIZE'},
    {'name': 'DATABASES'},
    {'name': 'DEBUG', 'default': 'false'},
    {'name': 'DEFAULT_FROM_EMAIL'},
    {'name': 'DISALLOWED_USER_AGENTS'},
    {'name': 'EMAIL_BACKEND'},
    {'name': 'EMAIL_HOST'},
    {'name': 'EMAIL_HOST_PASSWORD'},
    {'name': 'EMAIL_HOST_USER'},
    {'name': 'EMAIL_PORT'},
    {'name': 'EMAIL_TIMEOUT'},
    {'name': 'EMAIL_USE_SSL'},
    {'name': 'EMAIL_USE_TLS'},
    {'name': 'FILE_UPLOAD_MAX_MEMORY_SIZE'},
    {'name': 'HOME_VIEW'},
    {'name': 'INSTALLED_APPS'},
    {'name': 'INTERNAL_IPS', 'default': "['127.0.0.1']"},
    {'name': 'LANGUAGES'},
    {'name': 'LANGUAGE_CODE'},
    {'name': 'LOGIN_REDIRECT_URL', 'default': 'common:home'},
    {'name': 'LOGIN_URL', 'default': 'authentication:login_view'},
    {'name': 'LOGOUT_REDIRECT_URL', 'default': 'authentication:login_view'},
    {'name': 'STATIC_URL'},
    {'name': 'STATICFILES_STORAGE'},
    {'name': 'TIME_ZONE'},
    {'name': 'WSGI_APPLICATION'}
)