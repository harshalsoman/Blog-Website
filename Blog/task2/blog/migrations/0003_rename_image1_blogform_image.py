# Generated by Django 3.2.5 on 2021-08-07 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210807_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogform',
            old_name='Image1',
            new_name='Image',
        ),
    ]
