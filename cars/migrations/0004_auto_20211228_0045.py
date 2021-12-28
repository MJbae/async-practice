# Generated by Django 3.1.13 on 2021-12-28 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20211228_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='customers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.customer'),
        ),
        migrations.AlterField(
            model_name='car',
            name='owners',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.owner'),
        ),
    ]