# Generated by Django 4.0.6 on 2022-11-11 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0003_rename_categoryimg_category_categoryimg1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryImg1',
            new_name='categoryImg',
        ),
    ]
