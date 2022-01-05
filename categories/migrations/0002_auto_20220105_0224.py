# Generated by Django 3.2.9 on 2022-01-04 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='category',
            new_name='a_category',
        ),
        migrations.AddField(
            model_name='category',
            name='a_theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.theme'),
        ),
    ]
