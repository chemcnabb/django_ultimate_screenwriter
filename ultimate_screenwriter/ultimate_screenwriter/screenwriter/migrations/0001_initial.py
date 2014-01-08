# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Action'
        db.create_table(u'action', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='ActionID')),
            ('action', self.gf('django.db.models.fields.TextField')(db_column='Action', blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Action'])

        # Adding model 'Character'
        db.create_table(u'character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='CharacterID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='CharacterName')),
        ))
        db.send_create_signal(u'screenwriter', ['Character'])

        # Adding model 'Dialogue'
        db.create_table(u'dialogue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='DialogueID')),
            ('dialogue_text', self.gf('django.db.models.fields.TextField')(db_column='DialogueText', blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Dialogue'])

        # Adding model 'Parentheses'
        db.create_table(u'parentheses', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='ParenthesesID')),
            ('parentheses', self.gf('django.db.models.fields.TextField')(db_column='ParenthesesText', blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Parentheses'])

        # Adding model 'Screenplay'
        db.create_table(u'screenplay', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='ScreenplayID')),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='Title', blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='Author', blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_column='Date', blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Screenplay'])

        # Adding model 'Slug'
        db.create_table(u'slug', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='SlugID')),
            ('slug', self.gf('django.db.models.fields.TextField')(db_column='Slug', blank=True)),
        ))
        db.send_create_signal(u'screenwriter', ['Slug'])

        # Adding model 'ScreenplayElements'
        db.create_table(u'screenplay_elements', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='ScreenplayElementsID')),
            ('element_id', self.gf('django.db.models.fields.TextField')(db_column='ElementID', blank=True)),
            ('element_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.ScreenplayElementType'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['screenwriter.ScreenplayElements'])),
            ('screenplay', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['screenwriter.Screenplay'])),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(db_column='ScreenplaySortOrder')),
        ))
        db.send_create_signal(u'screenwriter', ['ScreenplayElements'])

        # Adding model 'ScreenplayElementType'
        db.create_table(u'screenplay_element_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='ScreenplayElementTypeID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000, db_column='ElementType')),
        ))
        db.send_create_signal(u'screenwriter', ['ScreenplayElementType'])


    def backwards(self, orm):
        # Deleting model 'Action'
        db.delete_table(u'action')

        # Deleting model 'Character'
        db.delete_table(u'character')

        # Deleting model 'Dialogue'
        db.delete_table(u'dialogue')

        # Deleting model 'Parentheses'
        db.delete_table(u'parentheses')

        # Deleting model 'Screenplay'
        db.delete_table(u'screenplay')

        # Deleting model 'Slug'
        db.delete_table(u'slug')

        # Deleting model 'ScreenplayElements'
        db.delete_table(u'screenplay_elements')

        # Deleting model 'ScreenplayElementType'
        db.delete_table(u'screenplay_element_type')


    models = {
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
        u'screenwriter.parentheses': {
            'Meta': {'object_name': 'Parentheses', 'db_table': "u'parentheses'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'ParenthesesID'"}),
            'parentheses': ('django.db.models.fields.TextField', [], {'db_column': "'ParenthesesText'", 'blank': 'True'})
        },
        u'screenwriter.screenplay': {
            'Meta': {'object_name': 'Screenplay', 'db_table': "u'screenplay'"},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Author'", 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'Date'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'ScreenplayID'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Title'", 'blank': 'True'})
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
        u'screenwriter.slug': {
            'Meta': {'object_name': 'Slug', 'db_table': "u'slug'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'SlugID'"}),
            'slug': ('django.db.models.fields.TextField', [], {'db_column': "'Slug'", 'blank': 'True'})
        }
    }

    complete_apps = ['screenwriter']