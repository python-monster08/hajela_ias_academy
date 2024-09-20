# Generated by Django 5.1 on 2024-09-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_bank', '0007_quoteidiomphrase_meaning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteidiomphrase',
            name='topic',
        ),
        migrations.AddField(
            model_name='quoteidiomphrase',
            name='topics',
            field=models.ManyToManyField(to='question_bank.topicname'),
        ),
    ]
