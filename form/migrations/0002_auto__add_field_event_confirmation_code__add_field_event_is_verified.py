# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.confirmation_code'
        db.add_column(u'form_event', 'confirmation_code',
                      self.gf('django.db.models.fields.CharField')(default="I'm OG so I don't have a confirmation code", max_length=255),
                      keep_default=False)

        # Adding field 'Event.is_verified'
        db.add_column(u'form_event', 'is_verified',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.confirmation_code'
        db.delete_column(u'form_event', 'confirmation_code')

        # Deleting field 'Event.is_verified'
        db.delete_column(u'form_event', 'is_verified')


    models = {
        u'form.category': {
            'Meta': {'ordering': "['title']", 'object_name': 'Category'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'form.event': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'Event'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['form.Category']", 'symmetrical': 'False'}),
            'confirmation_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'student_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['form']