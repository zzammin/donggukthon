# Generated by Django 5.0 on 2023-12-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_member_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelTable(
            name='member',
            table='member',
        ),
    ]
