# Generated by Django 3.2.6 on 2021-08-06 18:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='csvs')),
                ('upload', models.DateField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SalesBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=3)),
                ('full_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='SalesManager',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=64)),
                ('area', models.CharField(max_length=128)),
                ('position', models.CharField(max_length=128)),
                ('supervisor', models.CharField(blank=True, max_length=128, null=True)),
                ('phone_number', models.CharField(max_length=18)),
                ('email', models.EmailField(max_length=254)),
                ('id_number', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('sales_branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sheet.salesbranch', verbose_name='Oddzial')),
            ],
        ),
    ]
