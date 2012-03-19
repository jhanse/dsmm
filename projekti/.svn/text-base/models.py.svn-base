from django.db import models
from datetime import datetime
import os.path
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

def save_image(instance, filename):
    finalname = 'projekti/logoti/%s' % ''.join([instance.slug, str(datetime.now().strftime("%Y_%m%d_%H%M_%S")), os.path.splitext(filename)[1]])
    return finalname

class Projekt(models.Model):
    ime = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=save_image, blank=True)
    slug = models.SlugField(max_length=120, unique=True, editable=False)
    author = models.ForeignKey(User, blank=False)
    vodja = models.CharField(max_length=100)
    spletna_stran = models.URLField(max_length=250, blank=True)
    kontakt = models.EmailField(max_length=100)
    objavljeno = models.DateTimeField(default=datetime.now)
    kratek_opis = models.CharField(max_length=140, blank=True, help_text="max. 140 znakov")
    opis = models.TextField()
    sidebar_title = models.CharField(max_length=30, blank=True, default=None)
    sidebar = models.TextField(blank=True, default=None)

    def __unicode__(self):
        return smart_unicode(("%s" % self.ime))

    class Meta:
        verbose_name_plural = "Projekti"

    def save(self):
        self.slug = slugify(self.ime)
        super(Projekt,self).save()

    def get_absolute_url(self):
        return "/projekt/%s/" % self.slug
