# Generated by Django 3.1.7 on 2021-04-08 05:53

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=31)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=31, populate_from=['location'])),
            ],
            options={
                'ordering': ['location'],
            },
        ),
    ]
