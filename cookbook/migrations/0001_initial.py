# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RecipeTag'
        db.create_table('cookbook_recipetag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('cookbook', ['RecipeTag'])

        # Adding model 'Recipe'
        db.create_table('cookbook_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('cookbook', ['Recipe'])

        # Adding M2M table for field favorite_by on 'Recipe'
        db.create_table('cookbook_recipe_favorite_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['cookbook.recipe'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('cookbook_recipe_favorite_by', ['recipe_id', 'user_id'])

        # Adding M2M table for field recipe_tags on 'Recipe'
        db.create_table('cookbook_recipe_recipe_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['cookbook.recipe'], null=False)),
            ('recipetag', models.ForeignKey(orm['cookbook.recipetag'], null=False))
        ))
        db.create_unique('cookbook_recipe_recipe_tags', ['recipe_id', 'recipetag_id'])

        # Adding model 'Ingredient'
        db.create_table('cookbook_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cookbook.Recipe'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('quantity', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('cookbook', ['Ingredient'])

        # Adding M2M table for field needed_by on 'Ingredient'
        db.create_table('cookbook_ingredient_needed_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ingredient', models.ForeignKey(orm['cookbook.ingredient'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('cookbook_ingredient_needed_by', ['ingredient_id', 'user_id'])

        # Adding model 'Step'
        db.create_table('cookbook_step', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cookbook.Recipe'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('step_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('cookbook', ['Step'])

        # Adding model 'Note'
        db.create_table('cookbook_note', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cookbook.Recipe'])),
            ('note_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('cookbook', ['Note'])


    def backwards(self, orm):
        # Deleting model 'RecipeTag'
        db.delete_table('cookbook_recipetag')

        # Deleting model 'Recipe'
        db.delete_table('cookbook_recipe')

        # Removing M2M table for field favorite_by on 'Recipe'
        db.delete_table('cookbook_recipe_favorite_by')

        # Removing M2M table for field recipe_tags on 'Recipe'
        db.delete_table('cookbook_recipe_recipe_tags')

        # Deleting model 'Ingredient'
        db.delete_table('cookbook_ingredient')

        # Removing M2M table for field needed_by on 'Ingredient'
        db.delete_table('cookbook_ingredient_needed_by')

        # Deleting model 'Step'
        db.delete_table('cookbook_step')

        # Deleting model 'Note'
        db.delete_table('cookbook_note')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cookbook.ingredient': {
            'Meta': {'ordering': "['order']", 'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'needed_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cookbook.Recipe']"})
        },
        'cookbook.note': {
            'Meta': {'object_name': 'Note'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note_text': ('django.db.models.fields.TextField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cookbook.Recipe']"})
        },
        'cookbook.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'favorite_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe_tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cookbook.RecipeTag']", 'symmetrical': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'cookbook.recipetag': {
            'Meta': {'object_name': 'RecipeTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'cookbook.step': {
            'Meta': {'ordering': "['order']", 'object_name': 'Step'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cookbook.Recipe']"}),
            'step_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['cookbook']