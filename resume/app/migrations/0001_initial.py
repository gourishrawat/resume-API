# Generated by Django 4.1.7 on 2023-03-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('Bihar', 'Bihar'), ('Jharkhand', 'Jharkhand'), ('West bengal', 'West bengal')], max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('pimage', models.ImageField(blank=True, upload_to='pimage')),
                ('rdoc', models.FileField(blank=True, upload_to='rdocs')),
            ],
        ),
    ]
