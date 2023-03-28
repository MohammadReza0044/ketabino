# Generated by Django 4.1.7 on 2023-03-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]