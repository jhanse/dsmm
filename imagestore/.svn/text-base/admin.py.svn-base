#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from imagestore.models import Image, Album, AlbumUpload
from sorl.thumbnail.admin import AdminImageMixin, AdminInlineImageMixin
from django.conf import settings

class InlineImageAdmin(AdminInlineImageMixin, admin.TabularInline):
    model = Image
    fieldsets = ((None, {'fields': ['image', 'user', 'title', 'order', 'tags', 'album']}),)
    raw_id_fields = ('user', )
    extra = 0

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['name', 'is_public', 'order']}),)
    list_display = ('name', 'admin_thumbnail','user', 'created', 'updated', 'is_public', 'order')
    list_editable = ('order', )
    exclude = ('user',)
    inlines = [InlineImageAdmin]

    def queryset(self, request):
        qs = super(AlbumAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_form(self, request, form, change):
        obj = super(AlbumAdmin, self).save_form(request, form, change)
        if not change:
            obj.user = request.user
        return obj

admin.site.register(Album, AlbumAdmin)

class ImageAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['user', 'title', 'image', 'description', 'order', 'tags', 'album']}),)
    list_display = ('admin_thumbnail', 'user', 'order', 'album', 'title')
    raw_id_fields = ('user', )
    list_filter = ('album', )
    exclude = ('user',)

    def queryset(self, request):
        qs = super(ImageAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_form(self, request, form, change):
        obj = super(ImageAdmin, self).save_form(request, form, change)
        if not change:
            obj.user = request.user
        return obj

class AlbumUploadAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

IMAGE_MODEL = getattr(settings, 'IMAGESTORE_IMAGE_MODEL', None)
if not IMAGE_MODEL:
    admin.site.register(Image, ImageAdmin)

ALBUM_MODEL = getattr(settings, 'IMAGESTORE_ALBUM_MODEL', None)
if not ALBUM_MODEL:
    admin.site.register(AlbumUpload, AlbumUploadAdmin)
