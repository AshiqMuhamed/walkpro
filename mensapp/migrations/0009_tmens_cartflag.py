# Generated by Django 3.2.11 on 2022-06-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensapp', '0008_alter_tmens_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmens',
            name='cartflag',
            field=models.BooleanField(default=False),
        ),
    ]