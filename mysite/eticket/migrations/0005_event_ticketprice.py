# Generated by Django 4.2.7 on 2023-11-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eticket', '0004_event_eventname_event_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ticketPrice',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=10),
        ),
    ]
