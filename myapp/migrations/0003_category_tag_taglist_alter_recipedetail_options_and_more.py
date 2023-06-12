# Generated by Django 4.2.1 on 2023-06-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_ingredientlist_recipedetail_ingredient_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TagList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterModelOptions(
            name='recipedetail',
            options={'ordering': ['created_time']},
        ),
        migrations.RenameField(
            model_name='recipedetail',
            old_name='createdTime',
            new_name='created_time',
        ),
        migrations.AddField(
            model_name='recipedetail',
            name='category',
            field=models.ManyToManyField(to='myapp.category_tag'),
        ),
        migrations.AddField(
            model_name='recipedetail',
            name='tags',
            field=models.ManyToManyField(to='myapp.taglist'),
        ),
    ]