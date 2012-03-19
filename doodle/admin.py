from django.contrib import admin
from doodle.models import *

class DoodleAdmin(admin.ModelAdmin):
    fields = ('avtor', 'slika')
    list_display = ('avtor', 'slika', 'published')

admin.site.register(Doodle, DoodleAdmin)