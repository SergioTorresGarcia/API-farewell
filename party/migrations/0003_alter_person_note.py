# Generated by Django 4.0.3 on 2022-06-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_person_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='note',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
