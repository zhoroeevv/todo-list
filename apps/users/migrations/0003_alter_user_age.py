# Generated by Django 4.2.7 on 2024-05-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_age_alter_user_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=255, verbose_name='Возраст'),
        ),
    ]
