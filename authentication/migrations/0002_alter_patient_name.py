# Generated by Django 3.2.9 on 2021-11-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
