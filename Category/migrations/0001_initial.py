# Generated by Django 4.0.6 on 2022-11-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
                ('categoryCode', models.CharField(max_length=20)),
                ('categoryParent', models.BigIntegerField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]
