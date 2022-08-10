# Generated by Django 3.2.11 on 2022-04-20 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensapp', '0002_alter_tmens_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmens',
            name='maincategory',
            field=models.CharField(choices=[('mens', 'MENS'), ('ladies', 'LADIES'), ('girls', 'GIRLS'), ('boys', 'BOYS'), ('kids', 'KIDS')], default='mens', max_length=20),
        ),
    ]