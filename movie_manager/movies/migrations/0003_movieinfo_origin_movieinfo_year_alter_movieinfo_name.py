# Generated by Django 4.2.6 on 2023-10-16 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movieinfo_origin_remove_movieinfo_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='origin',
            field=models.TextField(default='south'),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
