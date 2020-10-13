# Generated by Django 3.1.2 on 2020-10-13 10:45

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostUserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=264)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('isbn', models.CharField(max_length=13)),
                ('bookTitle', models.CharField(max_length=100, null=True)),
                ('bookAuthor', models.CharField(max_length=100, null=True)),
                ('date_Added', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
