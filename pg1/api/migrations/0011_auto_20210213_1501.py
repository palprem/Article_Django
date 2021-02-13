# Generated by Django 3.0.8 on 2021-02-13 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210213_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(upload_to='artical'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.USER'),
        ),
    ]
