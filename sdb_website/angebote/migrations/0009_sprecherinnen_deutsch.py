# Generated by Django 4.2 on 2023-04-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angebote', '0008_alter_sprecherinnen_honorarkategorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprecherinnen',
            name='deutsch',
            field=models.CharField(blank=True, choices=[('keine', 'keine'), ('Vorkenntnisse', 'Vorkenntnisse'), ('Gut', 'Gut'), ('Fliessend', 'Fliessend'), ('Muttersprache', 'Muttersprache')], default='', max_length=13),
        ),
    ]
