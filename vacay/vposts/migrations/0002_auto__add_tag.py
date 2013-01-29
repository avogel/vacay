# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('vposts_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('vposts', ['Tag'])

        # Adding M2M table for field tagged_posts on 'Tag'
        db.create_table('vposts_tag_tagged_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm['vposts.tag'], null=False)),
            ('post', models.ForeignKey(orm['vposts.post'], null=False))
        ))
        db.create_unique('vposts_tag_tagged_posts', ['tag_id', 'post_id'])

        # Adding M2M table for field tagged_days on 'Tag'
        db.create_table('vposts_tag_tagged_days', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm['vposts.tag'], null=False)),
            ('visitedday', models.ForeignKey(orm['vposts.visitedday'], null=False))
        ))
        db.create_unique('vposts_tag_tagged_days', ['tag_id', 'visitedday_id'])

        # Adding M2M table for field tagged_cities on 'Tag'
        db.create_table('vposts_tag_tagged_cities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm['vposts.tag'], null=False)),
            ('visitedcity', models.ForeignKey(orm['vposts.visitedcity'], null=False))
        ))
        db.create_unique('vposts_tag_tagged_cities', ['tag_id', 'visitedcity_id'])

        # Adding M2M table for field tagged_trips on 'Tag'
        db.create_table('vposts_tag_tagged_trips', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm['vposts.tag'], null=False)),
            ('trip', models.ForeignKey(orm['vposts.trip'], null=False))
        ))
        db.create_unique('vposts_tag_tagged_trips', ['tag_id', 'trip_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('vposts_tag')

        # Removing M2M table for field tagged_posts on 'Tag'
        db.delete_table('vposts_tag_tagged_posts')

        # Removing M2M table for field tagged_days on 'Tag'
        db.delete_table('vposts_tag_tagged_days')

        # Removing M2M table for field tagged_cities on 'Tag'
        db.delete_table('vposts_tag_tagged_cities')

        # Removing M2M table for field tagged_trips on 'Tag'
        db.delete_table('vposts_tag_tagged_trips')


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
        'vposts.post': {
            'Meta': {'object_name': 'Post'},
            'contents': ('django.db.models.fields.TextField', [], {}),
            'date_written': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'likes'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'vposts.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tagged_cities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tagged_cities'", 'symmetrical': 'False', 'to': "orm['vposts.VisitedCity']"}),
            'tagged_days': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tagged_days'", 'symmetrical': 'False', 'to': "orm['vposts.VisitedDay']"}),
            'tagged_posts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tagged_posts'", 'symmetrical': 'False', 'to': "orm['vposts.Post']"}),
            'tagged_trips': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tagged_trips'", 'symmetrical': 'False', 'to': "orm['vposts.Trip']"})
        },
        'vposts.trip': {
            'Meta': {'object_name': 'Trip'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ideas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'trip_ideas'", 'symmetrical': 'False', 'to': "orm['vposts.Post']"}),
            'is_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trips'", 'to': "orm['auth.User']"})
        },
        'vposts.visitedcity': {
            'Meta': {'ordering': "['city_number', 'id']", 'object_name': 'VisitedCity'},
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city_number': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ideas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'city_ideas'", 'symmetrical': 'False', 'to': "orm['vposts.Post']"}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visited_cities'", 'to': "orm['vposts.Trip']"})
        },
        'vposts.visitedday': {
            'Meta': {'ordering': "['day_number', 'id']", 'object_name': 'VisitedDay'},
            'date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'day_number': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ideas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'ideas'", 'symmetrical': 'False', 'to': "orm['vposts.Post']"}),
            'visited_city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visited_days'", 'to': "orm['vposts.VisitedCity']"}),
            'written_posts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'written_posts'", 'symmetrical': 'False', 'to': "orm['vposts.Post']"})
        }
    }

    complete_apps = ['vposts']