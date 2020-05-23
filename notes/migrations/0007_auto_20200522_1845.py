# Generated by Django 3.0.6 on 2020-05-22 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_notemetadata_cloned_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemetadata',
            name='cloned_note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clones', to='notes.Note'),
        ),
    ]