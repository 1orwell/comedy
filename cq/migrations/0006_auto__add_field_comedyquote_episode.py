# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ComedyQuote.episode'
        db.add_column('cq_comedyquote', 'episode',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['episodes.Episode']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ComedyQuote.episode'
        db.delete_column('cq_comedyquote', 'episode_id')


    models = {
        'cq.comedyquote': {
            'Meta': {'object_name': 'ComedyQuote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['episodes.Episode']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'default': "'TV'", 'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tv_episode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tv_series': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        'episodes.episode': {
            'Meta': {'object_name': 'Episode'},
            'air_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['episodes.Season']"})
        },
        'episodes.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['cq']