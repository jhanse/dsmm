#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from projekti.models import *

class ProjektAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('ime', 'logo', 'vodja', 'spletna_stran', 'kontakt', 'kratek_opis', 'opis'),
        }),
        ('Napredno', {
            'classes': ('collapse closed',),
            'fields': ('sidebar_title', 'sidebar',),
        })
    )
    list_display = ('ime', 'objavljeno', 'vodja', 'spletna_stran', 'kontakt', 'logo', 'author')
    exclude = ('author',)

    def save_form(self, request, form, change):
        obj = super(ProjektAdmin, self).save_form(request, form, change)
        if not change:
            obj.author = request.user
        return obj

    def queryset(self, request):
        qs = super(ProjektAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    class Media:
        js = (
            '/static/js/tiny_mce/tiny_mce_src.js',
            '/static/js/textareas.js',
        )

admin.site.register(Projekt, ProjektAdmin)