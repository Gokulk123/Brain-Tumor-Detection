# Generated by Django 3.0.4 on 2020-04-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agent_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('street', models.CharField(default='SOME STRING', max_length=20)),
                ('hname', models.CharField(default='SOME STRING', max_length=20)),
                ('district', models.CharField(default='SOME STRING', max_length=50)),
                ('state', models.CharField(default='SOME STRING', max_length=20)),
                ('pincode', models.CharField(default='SOME STRING', max_length=20)),
                ('country', models.CharField(default='SOME STRING', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('license_num', models.CharField(max_length=100)),
            ],
        ),
    ]