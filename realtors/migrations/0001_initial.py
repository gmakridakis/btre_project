# Generated by Django 3.2.9 on 2021-11-19 15:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('photo', models.ImageField(upload_to='photos/realtors/%Y%m%d/')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=64)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]