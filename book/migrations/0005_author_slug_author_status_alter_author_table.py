# Generated by Django 4.1.7 on 2023-03-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_options_author_birth_author_death_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterModelTable(
            name='author',
            table='Author',
        ),
    ]