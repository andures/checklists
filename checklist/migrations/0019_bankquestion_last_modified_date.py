# Generated by Django 5.1.7 on 2025-04-04 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0018_bankquestion_question_hash_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankquestion',
            name='last_modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
