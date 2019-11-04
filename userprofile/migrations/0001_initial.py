# Generated by Django 2.2.6 on 2019-11-04 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayPicture', models.ImageField(upload_to='dp')),
                ('hallName', models.CharField(choices=[('YKSG East', 'YKSG East'), ('YKSG West', 'YKSG West'), ('YKSG New Buliding', 'YKSG New Building'), ('YKSG Extension 1', 'YKSG Extension 1')], max_length=1055)),
                ('roomNumber', models.CharField(max_length=3)),
                ('contact1', models.CharField(max_length=11)),
                ('contact2', models.CharField(blank=True, max_length=11, null=True)),
                ('profileAuthor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]