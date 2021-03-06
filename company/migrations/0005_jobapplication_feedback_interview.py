# Generated by Django 4.0.4 on 2022-06-16 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_field'),
        ('company', '0004_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='feedback',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('type', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.internjob')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
