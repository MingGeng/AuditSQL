# Generated by Django 2.0.2 on 2018-02-24 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0008_auto_20180224_1011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roles',
            options={'default_permissions': (), 'verbose_name': '用户角色', 'verbose_name_plural': '用户角色'},
        ),
    ]