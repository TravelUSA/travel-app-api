# Generated by Django 3.1.6 on 2021-02-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(blank=True, max_length=255, null=True)),
                ('tumor_type', models.CharField(blank=True, max_length=255, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('ethnicity', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
