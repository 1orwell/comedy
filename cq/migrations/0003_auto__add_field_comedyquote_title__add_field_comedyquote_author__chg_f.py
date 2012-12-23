# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ComedyQuote.title'
        db.add_column('cq_comedyquote', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'ComedyQuote.author'
        db.add_column('cq_comedyquote', 'author',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)


        # Changing field 'ComedyQuote.source'
        db.alter_column('cq_comedyquote', 'source', self.gf('django.db.models.fields.CharField')(max_length=2))

    def backwards(self, orm):
        # Deleting field 'ComedyQuote.title'
        db.delete_column('cq_comedyquote', 'title')

        # Deleting field 'ComedyQuote.author'
        db.delete_column('cq_comedyquote', 'author')


        # Changing field 'ComedyQuote.source'
        db.alter_column('cq_comedyquote', 'source', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        'cq.comedyquote': {
            'Meta': {'object_name': 'ComedyQuote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'default': "'TV'", 'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['cq']