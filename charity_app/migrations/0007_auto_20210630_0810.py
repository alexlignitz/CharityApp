# Generated by Django 3.2.4 on 2021-06-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0006_donation_closing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='closing_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_comment',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]
