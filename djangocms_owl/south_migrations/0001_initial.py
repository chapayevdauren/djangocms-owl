# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OwlCarousel'
        db.create_table(u'djangocms_owl_owlcarousel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('pagination', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pagination_numbers', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('navigation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('autoplay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('stop_on_hover', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('items', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('auto_height', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('style', self.gf('django.db.models.fields.CharField')(default='style1', max_length=255)),
            ('template', self.gf('django.db.models.fields.CharField')(default='template1', max_length=255)),
        ))
        db.send_create_signal(u'djangocms_owl', ['OwlCarousel'])


    def backwards(self, orm):
        # Deleting model 'OwlCarousel'
        db.delete_table(u'djangocms_owl_owlcarousel')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'djangocms_owl.owlcarousel': {
            'Meta': {'object_name': 'OwlCarousel', '_ormbases': ['cms.CMSPlugin']},
            'auto_height': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'autoplay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'items': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'navigation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pagination': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pagination_numbers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stop_on_hover': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'style1'", 'max_length': '255'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'template1'", 'max_length': '255'})
        }
    }

    complete_apps = ['djangocms_owl']