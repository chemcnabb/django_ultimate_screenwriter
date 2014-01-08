# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Act'
        db.create_table(u'screenwriter_act', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('screenplay', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Screenplay'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Act'])

        # Adding model 'Genre'
        db.create_table(u'screenwriter_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'screenwriter', ['Genre'])

        # Adding model 'Scene'
        db.create_table(u'screenwriter_scene', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sequence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Sequence'])),
            ('heading', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Slug'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('action', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Scene'])

        # Adding model 'Sequence'
        db.create_table(u'screenwriter_sequence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('act', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Act'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Sequence'])

        # Adding field 'Screenplay.user'
        db.add_column(u'screenplay', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Screenplay.screenplay_document'
        db.add_column(u'screenplay', 'screenplay_document',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Act'
        db.delete_table(u'screenwriter_act')

        # Deleting model 'Genre'
        db.delete_table(u'screenwriter_genre')

        # Deleting model 'Scene'
        db.delete_table(u'screenwriter_scene')

        # Deleting model 'Sequence'
        db.delete_table(u'screenwriter_sequence')

        # Deleting field 'Screenplay.user'
        db.delete_column(u'screenplay', 'user_id')

        # Deleting field 'Screenplay.screenplay_document'
        db.delete_column(u'screenplay', 'screenplay_document')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'screenwriter.act': {
            'Meta': {'object_name': 'Act'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'screenplay': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Screenplay']"})
        },
        u'screenwriter.action': {
            'Meta': {'object_name': 'Action', 'db_table': "u'action'"},
            'action': ('django.db.models.fields.TextField', [], {'db_column': "'Action'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'ActionID'"})
        },
        u'screenwriter.character': {
            'Meta': {'object_name': 'Character', 'db_table': "u'character'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'CharacterID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'CharacterName'"})
        },
        u'screenwriter.dialogue': {
            'Meta': {'object_name': 'Dialogue', 'db_table': "u'dialogue'"},
            'dialogue_text': ('django.db.models.fields.TextField', [], {'db_column': "'DialogueText'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'DialogueID'"})
        },
        u'screenwriter.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'screenwriter.parentheses': {
            'Meta': {'object_name': 'Parentheses', 'db_table': "u'parentheses'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'ParenthesesID'"}),
            'parentheses': ('django.db.models.fields.TextField', [], {'db_column': "'ParenthesesText'", 'blank': 'True'})
        },
        u'screenwriter.scene': {
            'Meta': {'object_name': 'Scene'},
            'action': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'heading': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Slug']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sequence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Sequence']"})
        },
        u'screenwriter.screenplay': {
            'Meta': {'object_name': 'Screenplay', 'db_table': "u'screenplay'"},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Author'", 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'Date'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'ScreenplayID'"}),
            'screenplay_document': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Title'", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'screenwriter.screenplayelements': {
            'Meta': {'object_name': 'ScreenplayElements', 'db_table': "u'screenplay_elements'"},
            'element_id': ('django.db.models.fields.TextField', [], {'db_column': "'ElementID'", 'blank': 'True'}),
            'element_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.ScreenplayElementType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'ScreenplayElementsID'"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['screenwriter.ScreenplayElements']"}),
            'screenplay': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Screenplay']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'db_column': "'ScreenplaySortOrder'"})
        },
        u'screenwriter.screenplayelementtype': {
            'Meta': {'object_name': 'ScreenplayElementType', 'db_table': "u'screenplay_element_type'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'ScreenplayElementTypeID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'db_column': "'ElementType'"})
        },
        u'screenwriter.sequence': {
            'Meta': {'object_name': 'Sequence'},
            'act': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['screenwriter.Act']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'screenwriter.slug': {
            'Meta': {'object_name': 'Slug', 'db_table': "u'slug'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'SlugID'"}),
            'slug': ('django.db.models.fields.TextField', [], {'db_column': "'Slug'", 'blank': 'True'})
        }
    }

    complete_apps = ['screenwriter']