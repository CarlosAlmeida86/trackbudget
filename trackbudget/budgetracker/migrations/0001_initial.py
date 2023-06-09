# Generated by Django 4.2.1 on 2023-06-05 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('value', models.FloatField()),
                ('date', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
