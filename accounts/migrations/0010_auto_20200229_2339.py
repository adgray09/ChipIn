# Generated by Django 3.0.2 on 2020-02-29 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200229_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlydonation',
            old_name='monthly_donation',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='monthlydonation',
            name='title',
        ),
    ]
