import os, sys
sys.path.append('/home/student/dsmm')
sys.path.append('/home/student')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dsmm.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler() 
