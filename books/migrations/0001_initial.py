# Generated by Django 2.0.7 on 2018-07-28 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=100)),
                ('published', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=15)),
                ('pages', models.CharField(max_length=5)),
                ('language', models.CharField(max_length=2)),
                ('description', models.TextField()),
                ('inserted', models.DateTimeField(auto_now_add=True, verbose_name='inserted')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='last modified')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=20)),
                ('inserted', models.DateTimeField(auto_now_add=True, verbose_name='inserted')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
