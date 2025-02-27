# Generated by Django 5.1.2 on 2024-11-03 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_remove_question_correct_answer_question_answer_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answers', models.IntegerField()),
                ('wrong_answers', models.IntegerField()),
                ('total_questions', models.IntegerField()),
                ('easy_questions', models.IntegerField()),
                ('medium_questions', models.IntegerField()),
                ('hard_questions', models.IntegerField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
