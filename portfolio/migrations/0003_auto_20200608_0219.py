# Generated by Django 3.0.7 on 2020-06-07 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200608_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='', upload_to='portfolio/imagelab/'),
        ),
    ]
