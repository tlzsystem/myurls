# Generated by Django 2.0.4 on 2018-06-22 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myurl', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myurl',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='myurl',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
