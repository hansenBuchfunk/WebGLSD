# Generated by Django 4.2 on 2023-04-11 17:20

from django.db import migrations
import multiselectfield.db.fields
import multiselectfield.validators


class Migration(migrations.Migration):

    dependencies = [
        ('angebote', '0005_sprecherinnen_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprecherinnen',
            name='charakter',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('sonor', 'sonor'), ('klar', 'klar'), ('rauh', 'rauh'), ('weich', 'weich')], default=None, max_length=21, validators=[multiselectfield.validators.MaxValueMultiFieldValidator(4)]),
        ),
    ]
