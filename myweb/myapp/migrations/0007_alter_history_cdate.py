# Generated by Django 4.1.4 on 2023-01-03 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_alter_history_hisid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="history",
            name="cdate",
            field=models.DateField(auto_now=True),
        ),
    ]