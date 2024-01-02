# Generated by Django 4.2.8 on 2024-01-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=255)),
                ('website', models.URLField(blank=True, default='https://google.com', null=True)),
                ('phone_num', models.CharField(max_length=255)),
                ('tin', models.CharField(max_length=255)),
                ('trade_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('sector', models.CharField(choices=[('Manufacturing', 'Manufacturing'), ('Factory', 'Factory'), ('Hotel', 'Hotel')], max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]