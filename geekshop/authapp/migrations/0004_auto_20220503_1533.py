# Generated by Django 3.2.13 on 2022-05-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20220503_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='возраст'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users_avatars'),
        ),
    ]
