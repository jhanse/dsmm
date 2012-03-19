#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from bases.image import BaseImage
from django.utils.translation import ugettext_lazy as _
from imagestore.utils import load_class, get_model_string

class Image(BaseImage):
    class Meta(BaseImage.Meta):
        abstract = False
        verbose_name = _('Slika')
        verbose_name_plural = _('Slike')
        app_label = 'imagestore'