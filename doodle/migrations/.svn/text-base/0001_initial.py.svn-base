# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Doodle'
        db.create_table('doodle_doodle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('avtor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slika', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('doodle', ['Doodle'])


    def backwards(self, orm):
        
        # Deleting model 'Doodle'
        db.delete_table('doodle_doodle')


    models = {
        'doodle.doodle': {
            'Meta': {'object_name': 'Doodle'},
            'avtor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slika': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['doodle']
