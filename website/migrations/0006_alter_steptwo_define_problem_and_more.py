# Generated by Django 5.0.6 on 2024-05-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_steptwo_selected_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steptwo',
            name='define_problem',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='steptwo',
            name='desired_solution',
            field=models.TextField(blank=True, null=True),
        ),
    ]