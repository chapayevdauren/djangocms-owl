# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OwlCarousel.extra_options'
        db.add_column(u'djangocms_owl_owlcarousel', 'extra_options',
                      self.gf('jsonfield.fields.JSONField')(default={}, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'OwlCarousel.extra_options'
        db.delete_column(u'djangocms_owl_owlcarousel', 'extra_options')


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
            'Meta': {'object_name': 'OwlCarousel'},
            'auto_height': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'autoplay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'extra_options': ('jsonfield.fields.JSONField', [], {'default': '{}', 'blank': 'True'}),
            'items': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'navigation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pagination': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pagination_numbers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stop_on_hover': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '255'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '255'})
        }
    }

    complete_apps = ['djangocms_owl']