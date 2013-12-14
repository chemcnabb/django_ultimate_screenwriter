# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Screenplay'
        db.create_table(u'screenwriter_screenplay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('length', self.gf('django.db.models.fields.IntegerField')(default=120, null=True, blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Screenplay'])

        # Adding model 'Act'
        db.create_table(u'screenwriter_act', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('screenplay', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Screenplay'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Act'])

        # Adding model 'Sequence'
        db.create_table(u'screenwriter_sequence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('act', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Act'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Sequence'])

        # Adding model 'Heading'
        db.create_table(u'screenwriter_heading', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Heading'])

        # Adding model 'Scene'
        db.create_table(u'screenwriter_scene', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sequence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Sequence'])),
            ('heading', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Heading'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('action', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Scene'])

        # Adding model 'Action'
        db.create_table(u'screenwriter_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('heading', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Heading'])),
        ))
        db.send_create_signal(u'screenwriter', ['Action'])

        # Adding model 'Character'
        db.create_table(u'screenwriter_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scene', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Scene'])),
            ('heading', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Heading'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Character'])

        # Adding model 'Dialogue'
        db.create_table(u'screenwriter_dialogue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Character'])),
        ))
        db.send_create_signal(u'screenwriter', ['Dialogue'])


    def backwards(self, orm):
        # Deleting model 'Screenplay'
        db.delete_table(u'screenwriter_screenplay')

        # Deleting model 'Act'
        db.delete_table(u'screenwriter_act')

        # Deleting model 'Sequence'
        db.delete_table(u'screenwriter_sequence')

        # Deleting model 'Heading'
        db.delete_table(u'screenwriter_heading')

        # Deleting model 'Scene'
        db.delete_table(u'screenwriter_scene')

        # Deleting model 'Action'
        db.delete_table(u'screenwriter_action')

        # Deleting model 'Character'
        db.delete_table(u'screenwriter_character')

        # Deleting model 'Dialogue'
        db.delete_table(u'screenwriter_dialogue')


    models = {
        u'screenwriter.act': {
            'Meta': {'object_name': 'Act'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'screenplay': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Screenplay']"})
        },
        u'screenwriter.action': {
            'Meta': {'object_name': 'Action'},
            'heading': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Heading']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'screenwriter.character': {
            'Meta': {'object_name': 'Character'},
            'heading': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Heading']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Scene']"})
        },
        u'screenwriter.dialogue': {
            'Meta': {'object_name': 'Dialogue'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'screenwriter.heading': {
            'Meta': {'object_name': 'Heading'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'screenwriter.scene': {
            'Meta': {'object_name': 'Scene'},
            'action': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'heading': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Heading']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sequence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Sequence']"})
        },
        u'screenwriter.screenplay': {
            'Meta': {'object_name': 'Screenplay'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'default': '120', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'screenwriter.sequence': {
            'Meta': {'object_name': 'Sequence'},
            'act': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Act']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['screenwriter']