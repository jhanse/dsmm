from django.db import models
from datetime import datetime
import os.path
from django.utils.encoding import smart_unicode

def save_image(instance, filename):
    finalname = 'doodle/%s' % ''.join([str(datetime.now().strftime("%Y_%m%d_%H%M_%S")), os.path.splitext(filename)[1]])
    return finalname

class Doodle(models.Model):
    avtor = models.CharField(max_length=50)
    slika = models.ImageField(upload_to=save_image)
    published = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return smart_unicode(("%s" % self.avtor))