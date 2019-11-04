# Generated by Django 2.2.6 on 2019-11-04 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
        ('ordertrack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptOrderRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acceptTime', models.DateTimeField(auto_now=True)),
                ('delivered', models.BooleanField(default=False)),
                ('deliveryTime', models.DateTimeField(blank=True, null=True)),
                ('pickParcel', models.BooleanField()),
                ('getDelivery', models.BooleanField()),
                ('deliveryMan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.ProfileEdit')),
                ('orderDetails', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ordertrack.PostOrderRequest')),
            ],
        ),
    ]
