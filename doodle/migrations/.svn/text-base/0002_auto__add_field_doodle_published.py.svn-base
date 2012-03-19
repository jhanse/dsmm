# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Doodle.published'
        db.add_column('doodle_doodle', 'published', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Doodle.published'
        db.delete_column('doodle_doodle', 'published')


    models = {
        'doodle.doodle': {
            'Meta': {'object_name': 'Doodle'},
            'avtor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slika': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['doodle']
