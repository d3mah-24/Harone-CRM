# Generated by Django 4.2.8 on 2024-01-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderRequest', '0004_orderrequest_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderrequest',
            name='date',
        ),
        migrations.AddField(
            model_name='orderrequest',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
