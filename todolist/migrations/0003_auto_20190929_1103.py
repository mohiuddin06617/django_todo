# Generated by Django 2.2.5 on 2019-09-29 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolist_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='category',
            field=models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todolist.Category'),
        ),
    ]