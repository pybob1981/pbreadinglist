# Generated by Django 2.0.7 on 2018-07-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180729_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbook',
            old_name='added',
            new_name='inserted',
        ),
        migrations.AddField(
            model_name='userbook',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userbook',
            name='status',
            field=models.CharField(choices=[('r', 'I am reading this book'), ('c', 'I have completed this book'), ('t', 'I want to read this book')], default='reading', max_length=1),
        ),
    ]
