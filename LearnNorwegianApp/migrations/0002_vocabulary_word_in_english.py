# Generated by Django 3.2.5 on 2022-04-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnNorwegianApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='word_in_english',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
