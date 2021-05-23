# Generated by Django 3.1.6 on 2021-05-23 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestappointment',
            name='appointmentType',
            field=models.CharField(choices=[('Requesting for Blood Donation', 'Requesting for Blood Donation'), ('Requesting for Immediate Transfusion', 'Requesting for Immediate Transfusion')], max_length=100),
        ),
        migrations.CreateModel(
            name='DonorAccount',
            fields=[
                ('donorID', models.AutoField(primary_key=True, serialize=False)),
                ('setStatus', models.CharField(choices=[('Ready to Donate', 'Ready to Doante'), ('Has Donated', 'Has Donated'), ('Waiting Appointment', 'Waiting Appointment')], max_length=100)),
                ('writeReminder', models.TextField(max_length=300)),
                ('requestDonorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.donor')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
