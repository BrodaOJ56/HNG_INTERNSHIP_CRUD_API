# Generated by Django 4.2.5 on 2023-09-13 00:07

from django.db import migrations, models
import person.models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100, validators=[person.models.validate_string]),
        ),
    ]
