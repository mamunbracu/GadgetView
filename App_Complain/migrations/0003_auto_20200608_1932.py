# Generated by Django 3.0.3 on 2020-06-09 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Complain', '0002_auto_20200608_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomplain',
            name='full_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='usercomplain',
            name='order_code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='usercomplain',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='usercomplain',
            name='your_complain',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]