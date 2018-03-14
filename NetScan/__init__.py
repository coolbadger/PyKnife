#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: __init__.py
# Author		: badger
# Created		: 2017/8/2
# Description	:
import os
import sys

from django.core.wsgi import get_wsgi_application


def load_env():
    sys.path.extend(['/Users/badger/My/MyPro/Python/PyKnife', ])
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PyKnife.settings")
    if sys.argv[0] != 'manage.py':
        application = get_wsgi_application()


load_env()
