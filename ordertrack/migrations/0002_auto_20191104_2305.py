# Generated by Django 2.2.6 on 2019-11-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordertrack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postorderrequest',
            name='deliveryCost',
            field=models.IntegerField(null=True),
        ),
    ]