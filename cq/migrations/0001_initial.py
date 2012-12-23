# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ComedyQuote'
        db.create_table('cq_comedyquote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('cq', ['ComedyQuote'])


    def backwards(self, orm):
        # Deleting model 'ComedyQuote'
        db.delete_table('cq_comedyquote')


    models = {
        'cq.comedyquote': {
            'Meta': {'object_name': 'ComedyQuote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'quote': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['cq']