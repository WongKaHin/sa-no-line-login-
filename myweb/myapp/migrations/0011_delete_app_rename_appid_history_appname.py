# Generated by Django 4.1.4 on 2023-01-03 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_alter_history_appid"),
    ]

    operations = [
        migrations.DeleteModel(
            name="app",
        ),
        migrations.RenameField(
            model_name="history",
            old_name="appid",
            new_name="appname",
        ),
    ]
