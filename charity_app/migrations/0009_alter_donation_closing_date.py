# Generated by Django 3.2.4 on 2021-06-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0008_alter_donation_is_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='closing_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
