# Generated by Django 2.2.1 on 2019-08-08 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': '客户', 'verbose_name_plural': '客户系统'},
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': '合同', 'verbose_name_plural': '合同系统'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '产品', 'verbose_name_plural': '产品系统'},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name': '资源', 'verbose_name_plural': '资源系统'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': '员工', 'verbose_name_plural': '员工系统'},
        ),
    ]