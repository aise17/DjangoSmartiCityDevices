# Generated by Django 3.0.1 on 2019-12-31 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GpsDevice',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('received_datetime', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('long', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='devicebeatshistory',
            name='gps_info',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='beats.GpsDevice'),
        ),
    ]