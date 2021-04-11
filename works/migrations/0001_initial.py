# Generated by Django 3.2 on 2021-04-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]