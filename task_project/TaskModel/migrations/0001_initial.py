# Generated by Django 4.2.7 on 2023-12-21 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TaskCategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=100)),
                ('taskDescription', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('Assign_Date', models.DateField()),
                ('category', models.ManyToManyField(to='TaskCategory.category')),
            ],
        ),
    ]