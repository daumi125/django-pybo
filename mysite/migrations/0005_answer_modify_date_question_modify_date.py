# Generated by Django 5.0 on 2024-01-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0004_answer_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
