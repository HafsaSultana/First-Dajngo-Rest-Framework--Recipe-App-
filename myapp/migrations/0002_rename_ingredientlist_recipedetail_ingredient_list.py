# Generated by Django 4.2.1 on 2023-05-30 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipedetail',
            old_name='ingredientList',
            new_name='ingredient_list',
        ),
    ]
