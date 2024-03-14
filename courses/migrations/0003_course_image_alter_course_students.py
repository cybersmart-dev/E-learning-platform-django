# Generated by Django 5.0.1 on 2024-03-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='static/courses/images/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='students', to='courses.student'),
        ),
    ]