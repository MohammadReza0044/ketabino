# Generated by Django 4.1.7 on 2023-03-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='active_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('A', 'Available'), ('U', 'Unavailable')], max_length=1),
        ),
    ]
