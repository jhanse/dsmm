#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'body', 'image')
        }),
        ('Napredne možnosti', {
            'classes': ('collapse closed',),
            'fields': ('is_commentable', 'is_event')
        })
    )
    list_display = ('title', 'published', 'author', 'is_commentable', 'is_event')
    list_editable = ('is_commentable',)
    exclude = ('author',)

    def save_form(self, request, form, change):
        obj = super(PostAdmin, self).save_form(request, form, change)
        if not change:
            obj.author = request.user
        return obj

    def queryset(self, request):
        qs = super(PostAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js')


class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'body'),
        }),
        ('Napredno', {
            'classes': ('collapse closed',),
            'fields': ('sidebar_title', 'sidebar', 'image',),
        })
    )
    list_display = ('title', 'published', 'author', 'image',)
    exclude = ('author',)

    def save_form(self, request, form, change):
        obj = super(PageAdmin, self).save_form(request, form, change)
        if not change:
            obj.author = request.user
        return obj

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js')


admin.site.register(Post, PostAdmin)
#admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(Vizitka)


# ENCODING: http://stackoverflow.com/questions/2168816/django-headache-with-simple-non-ascii-string
# ENCODING2: http://meta.osqa.net/questions/7126/caught-djangounicodedecodeerror-while-rendering-ascii-codec-cant-decode-byte-0xd0-in-position-0-ordinal-not-in-range128-you-passed-in
