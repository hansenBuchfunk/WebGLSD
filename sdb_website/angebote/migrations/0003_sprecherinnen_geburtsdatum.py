# Generated by Django 4.2 on 2023-04-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angebote', '0002_alter_sprecherinnen_emailadresse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprecherinnen',
            name='geburtsdatum',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
