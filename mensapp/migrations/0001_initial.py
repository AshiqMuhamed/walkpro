# Generated by Django 3.2.11 on 2022-04-17 08:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tmens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='picture')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('category', models.CharField(choices=[('casual', 'CASUAL'), ('formal', 'FORMALE'), ('semi-formal', 'SEMI-FORMAL')], default='casual', max_length=20)),
            ],
        ),
    ]
