# Generated by Django 3.2.5 on 2021-08-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210817_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(null=True, upload_to='myimages')),
            ],
        ),
        migrations.RemoveField(
            model_name='blogform',
            name='Image',
        ),
    ]
