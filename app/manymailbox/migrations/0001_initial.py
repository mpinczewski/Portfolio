# Generated by Django 3.2.6 on 2021-08-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('server', models.CharField(max_length=128)),
                ('port', models.CharField(blank=True, max_length=6, null=True)),
                ('email_user', models.CharField(max_length=128)),
                ('email_password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='RecievedMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_uidl', models.CharField(max_length=128)),
                ('send_date', models.DateTimeField(blank=True, null=True)),
                ('email_sender', models.CharField(max_length=128)),
                ('email_receiver', models.CharField(blank=True, max_length=128, null=True)),
                ('subject', models.CharField(max_length=128)),
                ('email_body', models.TextField(blank=True, max_length=10000, null=True)),
                ('is_forwarded', models.BooleanField(default=False)),
                ('send_to', models.CharField(blank=True, max_length=256, null=True)),
                ('save_to_db_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DestinationInbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128)),
                ('company', models.CharField(blank=True, max_length=64, null=True)),
                ('mailbox', models.ManyToManyField(blank=True, to='manymailbox.Mailbox')),
            ],
        ),
    ]
