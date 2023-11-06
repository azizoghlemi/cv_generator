# Generated by Django 4.1 on 2022-08-24 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('adress', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('nationality', models.CharField(max_length=30)),
                ('license', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training', models.CharField(max_length=30)),
                ('establishment', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=30)),
                ('Client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.client')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('skill', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.client')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('language', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.client')),
            ],
        ),
        migrations.CreateModel(
            name='Internships',
            fields=[
                ('internship', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('employer', models.CharField(max_length=40)),
                ('town', models.CharField(max_length=30)),
                ('Client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.client')),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.client')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=30)),
                ('establishment', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=30)),
                ('Client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.client')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=30)),
                ('establishment', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=30)),
                ('Client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.client')),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('experience', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('establishment', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=30)),
                ('Client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.client')),
            ],
        ),
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('certificate', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('period', models.CharField(max_length=30)),
                ('Client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.client')),
            ],
        ),
    ]