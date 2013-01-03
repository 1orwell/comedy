# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Episode.plot'
        db.add_column('episodes_episode', 'plot',
                      self.gf('django.db.models.fields.TextField')(default='plot'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Episode.plot'
        db.delete_column('episodes_episode', 'plot')


    models = {
        'episodes.episode': {
            'Meta': {'object_name': 'Episode'},
            'air_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'plot': ('django.db.models.fields.TextField', [], {}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['episodes.Season']"}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        'episodes.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['episodes']