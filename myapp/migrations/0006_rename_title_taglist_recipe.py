# Generated by Django 4.2.1 on 2023-06-06 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_taglist_name_taglist_hash_tag_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taglist',
            old_name='title',
            new_name='recipe',
        ),
    ]