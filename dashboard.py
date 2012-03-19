# -*- coding: utf-8 -*-

"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Administration" & "Applications"
        self.children.append(modules.Group(
            _('Skupina: Administracija & Aplikacije'),
            column=1,
            collapsible=True,
            children = [
                modules.AppList(
                    _('Administracija'),
                    column=1,
                    models=('django.contrib.*',),
                    css_classes=('collapse closed',),
                ),
                modules.AppList(
                    _('Aplikacije'),
                    column=1,
                    collapsible=True,
                    #css_classes=('collapse closed',),
                    exclude=('django.contrib.*',),
                )
            ]
        ))
        
        # append an app list module for "Applications"
#        self.children.append(modules.AppList(
#            _('Seznam aplikacij: Aplikacije'),
#            collapsible=True,
#            column=1,
#            css_classes=('collapse closed',),
#            exclude=('django.contrib.*',),
#        ))
        
        # append an app list module for "Administration"
#        self.children.append(modules.ModelList(
#            _('Seznam modelov: Administracija'),
#            column=1,
#            collapsible=True,
#            css_classes=('collapse closed',),
#            models=('django.contrib.*',),
#        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Upravljanje z datotekami'),
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Podpora'),
            column=2,
            children=[
                {
                    'title': _('Django Documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Documentation'),
                    'url': 'http://django-grappelli.readthedocs.org/en/latest/index.html',
                    'external': True,
                },
                {
                    'title': _('Grappelli Google-Code'),
                    'url': 'http://code.google.com/p/django-grappelli/',
                    'external': True,
                },
            ]
        ))
                
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


