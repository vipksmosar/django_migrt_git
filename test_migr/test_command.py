#import mytestsite.wsgi as wsgi
from django.core.management import call_command
import os
import sys
#wsgi.application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_migr.settings')
from django.core.management import call_command
call_command('makemigrations', 'testapp', verbosity=3, interactive=False)

