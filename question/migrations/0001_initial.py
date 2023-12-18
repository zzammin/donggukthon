# Generated by Django 5.0 on 2023-12-18 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0005_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('user', models.OneToOneField(db_column='User_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='login.member')),
                ('content', models.CharField(db_column='CONTENT', max_length=350)),
                ('flag', models.IntegerField(blank=True, db_column='FLAG', null=True)),
            ],
            options={
                'db_table': 'answer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('num', models.IntegerField(db_column='Num', primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, db_column='CONTENT', max_length=100, null=True)),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
    ]
