# Generated by Django 4.1 on 2022-09-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0015_alter_internships_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internships',
            name='employer',
            field=models.CharField(default=None, max_length=60),
        ),
    ]