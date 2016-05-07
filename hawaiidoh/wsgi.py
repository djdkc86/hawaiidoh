"""
WSGI config for hawaiidoh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('C:/Users/HPUAdmin/Bitnami Django Stack projects/hawaiidoh')
os.environ.setdefault("PYTHON_EGG_CACHE", "C:/Users/HPUAdmin/Bitnami Django Stack projects/hawaiidoh/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hawaiidoh.settings")

from django.core.wsgi import get_wsgi_application

from dj_static import Cling

application = Cling(get_wsgi_application())