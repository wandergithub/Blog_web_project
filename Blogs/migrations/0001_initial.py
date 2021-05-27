# Generated by Django 3.2.3 on 2021-05-15 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=40)),
                ('Text', models.CharField(max_length=1000)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]