# Generated by Django 3.0.4 on 2020-04-15 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_addcourse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addcourse',
            old_name='subject1',
            new_name='subjects',
        ),
        migrations.RenameField(
            model_name='addcourse',
            old_name='teacher1',
            new_name='teachers',
        ),
        migrations.RemoveField(
            model_name='addcourse',
            name='subject2',
        ),
        migrations.RemoveField(
            model_name='addcourse',
            name='subject3',
        ),
        migrations.RemoveField(
            model_name='addcourse',
            name='subject4',
        ),
        migrations.RemoveField(
            model_name='addcourse',
            name='teacher2',
        ),
        migrations.RemoveField(
            model_name='addcourse',
            name='teacher3',
        ),
        migrations.RemoveField(
            model_name='addcourse',
            name='teacher4',
        ),
    ]
