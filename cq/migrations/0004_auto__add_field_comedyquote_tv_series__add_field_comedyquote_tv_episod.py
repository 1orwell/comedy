# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ComedyQuote.tv_series'
        db.add_column('cq_comedyquote', 'tv_series',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'ComedyQuote.tv_episode'
        db.add_column('cq_comedyquote', 'tv_episode',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ComedyQuote.tv_series'
        db.delete_column('cq_comedyquote', 'tv_series')

        # Deleting field 'ComedyQuote.tv_episode'
        db.delete_column('cq_comedyquote', 'tv_episode')


    models = {
        'cq.comedyquote': {
            'Meta': {'object_name': 'ComedyQuote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'default': "'TV'", 'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tv_episode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tv_series': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['cq']