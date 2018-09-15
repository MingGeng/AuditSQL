# Generated by Django 2.1.1 on 2018-09-15 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshell', '0004_webshellinfo_envi_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webshellgrant',
            options={'default_permissions': (), 'verbose_name': 'webshell授权', 'verbose_name_plural': 'webshell授权'},
        ),
        migrations.AlterModelOptions(
            name='webshellinfo',
            options={'default_permissions': (), 'verbose_name': 'webshell', 'verbose_name_plural': 'webshell'},
        ),
        migrations.AlterField(
            model_name='webshellinfo',
            name='command',
            field=models.CharField(default='', max_length=1024, verbose_name='命令'),
        ),
        migrations.AlterField(
            model_name='webshellinfo',
            name='comment',
            field=models.CharField(max_length=128, null=True, verbose_name='描述'),
        ),
    ]