# Generated by Django 5.0.6 on 2024-07-01 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recepie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recepie_name', models.CharField(max_length=100)),
                ('recepie_description', models.TextField()),
                ('recepie_image', models.ImageField(upload_to='recepie')),
            ],
        ),
        migrations.DeleteModel(
            name='Receipe',
        ),
    ]
