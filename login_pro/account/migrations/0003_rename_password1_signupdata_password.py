# Generated by Django 3.2.8 on 2022-01-21 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_signupdata_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupdata',
            old_name='password1',
            new_name='password',
        ),
    ]