# Generated by Django 3.2.5 on 2022-04-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnNorwegianApp', '0005_auto_20220412_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='uregelrette_verb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('infinitiv', models.CharField(max_length=50)),
                ('presens', models.CharField(max_length=50)),
                ('preteritum', models.CharField(max_length=50)),
                ('presens_perfektum', models.CharField(max_length=50)),
                ('polski', models.CharField(max_length=50)),
            ],
        ),
    ]
