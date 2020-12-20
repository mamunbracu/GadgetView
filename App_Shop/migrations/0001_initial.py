# Generated by Django 3.0.3 on 2020-06-07 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(upload_to='product_pics')),
                ('name', models.CharField(max_length=100)),
                ('detailes', models.TextField(max_length=1000, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('preview_text', models.TextField(max_length=200, verbose_name='Preview')),
                ('price', models.FloatField()),
                ('old_price', models.FloatField(default=0.0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='App_Shop.Category')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]