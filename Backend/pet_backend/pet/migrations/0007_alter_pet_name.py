# Generated by Django 4.0.6 on 2023-01-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_alter_review_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
