from django.db import models
from datetime import datetime
import os.path
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

#class Category(models.Model):
#    name = models.CharField(max_length=60)
#
#    def __unicode__(self):
#        return smart_unicode(("%s" % self.name))
#
#    class Meta:
#        verbose_name = "kategorijo"
#        verbose_name_plural = "Kategorije"

def save_image(instance, filename):
    finalname = 'thumbs/%s' % ''.join([str(datetime.now().strftime("%Y_%m%d_%H%M_%S")), os.path.splitext(filename)[1]])
    return finalname

class Post(models.Model):
    title = models.CharField(('Naslov'), max_length=200)
    slug = models.SlugField(('Slug'), max_length=120, unique=True, editable=False)
    body = models.TextField(('Vsebina'))
    author = models.ForeignKey(User, blank=False, verbose_name='Avtor')
    image = models.ImageField(('Slika'), upload_to=save_image, blank=True)
    published = models.DateTimeField(('Objavljeno'), default=datetime.now)
#    categories = models.ForeignKey(Category, verbose_name='Kategorija')
    is_commentable = models.BooleanField(('Komentabilno'), default=1)
    is_event = models.BooleanField(('Dogodek'), default=0)

    def __unicode__(self):
        return smart_unicode(("%s" % self.title))

    class Meta:
        ordering = ['-published']
        verbose_name = "novico"
        verbose_name_plural = "Novice"

    def save(self):
        self.slug = slugify(self.title)
        super(Post,self).save()

    def get_absolute_url(self):
        return "/post/%s/" % self.slug

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120, unique=True, editable=False)
    body = models.TextField()
    author = models.ForeignKey(User, blank=False)
    image = models.ImageField(upload_to=save_image, blank=True)
    published = models.DateTimeField(default=datetime.now)
    sidebar_title = models.CharField(max_length=30, blank=True, default=None)
    sidebar = models.TextField(blank=True, default=None)

    def __unicode__(self):
        return smart_unicode(("%s" % self.title))

    class Meta:
        ordering = ['-published']
        verbose_name_plural = "Strani"

    def save(self):
        self.slug = slugify(self.title)
        super(Page,self).save()

    def get_absolute_url(self):
        return "/page/%s/" % self.slug

def save_person(instance, filename):
    finalname = '%s/%s' % ("uporabniki",''.join([instance.slug, "_", str(datetime.now().strftime("%Y_%m%d_%H%M_%S")), os.path.splitext(filename)[1]]))
    return finalname

class Vizitka(models.Model):
    name = models.CharField(('Ime in priimek'), max_length=100)
    about = models.TextField(('O sebi'))
    image = models.ImageField(('Slika'), upload_to=save_person)
    slug = models.SlugField(max_length=120, unique=True, editable=False)
    uo = models.BooleanField(('Upravni odbor'), default=0)
    no = models.BooleanField(('Nadzorni odbor'), default=0)
    
    def __unicode__(self):
        return smart_unicode(("%s" % self.name))

    class Meta:
        verbose_name = "osebo"
        verbose_name_plural = "Osebe"

    def save(self):
        self.slug = slugify(self.name)
        super(Vizitka,self).save()
