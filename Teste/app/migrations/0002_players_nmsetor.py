# Generated by Django 3.2.7 on 2021-09-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='nmSetor',
            field=models.CharField(default='null', max_length=400),
            preserve_default=False,
        ),
    ]