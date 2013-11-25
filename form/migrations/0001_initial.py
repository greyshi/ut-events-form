# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'form_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'form', ['Category'])

        # Adding model 'Event'
        db.create_table(u'form_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('student_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'form', ['Event'])

        # Adding M2M table for field categories on 'Event'
        m2m_table_name = db.shorten_name(u'form_event_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'form.event'], null=False)),
            ('category', models.ForeignKey(orm[u'form.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'form_category')

        # Deleting model 'Event'
        db.delete_table(u'form_event')

        # Removing M2M table for field categories on 'Event'
        db.delete_table(db.shorten_name(u'form_event_categories'))


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
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'student_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['form']