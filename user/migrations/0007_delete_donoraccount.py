# Generated by Django 3.1.6 on 2021-05-23 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_donoraccount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DonorAccount',
        ),
    ]