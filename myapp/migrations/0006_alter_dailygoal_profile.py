# Generated by Django 4.2.4 on 2024-06-06 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_alter_monthlygoal_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailygoal",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.profile"
            ),
        ),
    ]
