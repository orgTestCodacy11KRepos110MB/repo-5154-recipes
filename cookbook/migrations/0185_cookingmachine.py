# Generated by Django 4.0.7 on 2022-10-02 11:51

import cookbook.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0184_alter_userpreference_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookingMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('HOMECONNECT_COOKIT', 'HomeConnect CookIt')], max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('serial', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('access_token', models.CharField(blank=True, max_length=4096, null=True)),
                ('access_token_expiry', models.DateTimeField(blank=True, null=True)),
                ('refresh_token', models.CharField(blank=True, max_length=4096, null=True)),
                ('refresh_token_expiry', models.DateTimeField(blank=True, null=True)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.space')),
            ],
            bases=(models.Model, cookbook.models.PermissionModelMixin),
        ),
    ]
