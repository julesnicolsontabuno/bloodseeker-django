# Generated by Django 3.1.6 on 2021-05-23 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_donoraccount_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DonorAccount',
        ),
    ]