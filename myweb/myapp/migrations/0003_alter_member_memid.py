# Generated by Django 4.1.4 on 2022-12-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_app_behavior_exchange_history_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="memid",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]