# Generated by Django 3.2.5 on 2021-08-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210817_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='myimages')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageForm',
        ),
    ]