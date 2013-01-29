# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table('vposts_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('date_written', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('vposts', ['Post'])

        # Adding M2M table for field likes on 'Post'
        db.create_table('vposts_post_likes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['vposts.post'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('vposts_post_likes', ['post_id', 'user_id'])

        # Adding model 'Trip'
        db.create_table('vposts_trip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('is_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trips', to=orm['auth.User'])),
        ))
        db.send_create_signal('vposts', ['Trip'])

        # Adding M2M table for field ideas on 'Trip'
        db.create_table('vposts_trip_ideas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trip', models.ForeignKey(orm['vposts.trip'], null=False)),
            ('post', models.ForeignKey(orm['vposts.post'], null=False))
        ))
        db.create_unique('vposts_trip_ideas', ['trip_id', 'post_id'])

        # Adding model 'VisitedCity'
        db.create_table('vposts_visitedcity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city_number', self.gf('django.db.models.fields.IntegerField')()),
            ('trip', self.gf('django.db.models.fields.related.ForeignKey')(related_name='visited_cities', to=orm['vposts.Trip'])),
        ))
        db.send_create_signal('vposts', ['VisitedCity'])

        # Adding M2M table for field ideas on 'VisitedCity'
        db.create_table('vposts_visitedcity_ideas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('visitedcity', models.ForeignKey(orm['vposts.visitedcity'], null=False)),
            ('post', models.ForeignKey(orm['vposts.post'], null=False))
        ))
        db.create_unique('vposts_visitedcity_ideas', ['visitedcity_id', 'post_id'])

        # Adding model 'VisitedDay'
        db.create_table('vposts_visitedday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('day_number', self.gf('django.db.models.fields.IntegerField')()),
            ('visited_city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='visited_days', to=orm['vposts.VisitedCity'])),
        ))
        db.send_create_signal('vposts', ['VisitedDay'])

        # Adding M2M table for field written_posts on 'VisitedDay'
        db.create_table('vposts_visitedday_written_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('visitedday', models.ForeignKey(orm['vposts.visitedday'], null=False)),
            ('post', models.ForeignKey(orm['vposts.post'], null=False))
        ))
        db.create_unique('vposts_visitedday_written_posts', ['visitedday_id', 'post_id'])

        # Adding M2M table for field ideas on 'VisitedDay'
        db.create_table('vposts_visitedday_ideas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('visitedday', models.ForeignKey(orm['vposts.visitedday'], null=False)),
            ('post', models.ForeignKey(orm['vposts.post'], null=False))
        ))
        db.create_unique('vposts_visitedday_ideas', ['visitedday_id', 'post_id'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table('vposts_post')

        # Removing M2M table for field likes on 'Post'
        db.delete_table('vposts_post_likes')

        # Deleting model 'Trip'
        db.delete_table('vposts_trip')

        # Removing M2M table for field ideas on 'Trip'
        db.delete_table('vposts_trip_ideas')

        # Deleting model 'VisitedCity'
        db.delete_table('vposts_visitedcity')

        # Removing M2M table for field ideas on 'VisitedCity'
        db.delete_table('vposts_visitedcity_ideas')

        # Deleting model 'VisitedDay'
        db.delete_table('vposts_visitedday')

        # Removing M2M table for field written_posts on 'VisitedDay'
        db.delete_table('vposts_visitedday_written_posts')

        # Removing M2M table for field ideas on 'VisitedDay'
        db.delete_table('vposts_visitedday_ideas')


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