# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')ucor@d*=fa(a33g+c$y@r-ce+oe-hue%oof&c56pbj@b^hs28'

# Application definition

INSTALLED_APPS = [
    # 'NetScan',
    # 'sys',
    # 'CLEP'
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
