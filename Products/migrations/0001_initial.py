# Generated by Django 2.1.7 on 2019-04-04 11:52

import Products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('product_for', models.CharField(choices=[('sell', 'Sell'), ('rent', 'Rent')], max_length=4)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('type', models.CharField(choices=[('cloths', 'Cloths'), ('accessories', 'Accessories')], max_length=11)),
                ('price', models.DecimalField(decimal_places=2, default='99.99', max_digits=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('condition', models.CharField(choices=[('used', 'Used'), ('new', 'New')], max_length=4)),
                ('category', models.CharField(choices=[('traditional', 'Traditional'), ('formal', 'Formal'), ('casual', 'Casual'), ('ethnic', 'Ethnic'), ('sports', 'Sports'), ('western', 'Western'), ('t-shirts', 'T-shirts'), ('denim', 'Denim'), ('kids', 'Kids'), ('winter-wears', 'Winter-wear'), ('jumpsuits', 'Jumpsuits')], max_length=17)),
                ('occasion', models.CharField(choices=[('weddings', 'Weddings'), ('sangeet', 'Sangeet'), ('party', 'Party'), ('everyday', 'Everyday'), ('interview', 'Interview'), ('gym', 'Gym'), ('outings', 'Outings')], max_length=9)),
                ('featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('sold', models.BooleanField(default=False)),
                ('image1', models.ImageField(upload_to=Products.models.upload_image_path)),
                ('image2', models.ImageField(blank=True, null=True, upload_to=Products.models.upload_image_path)),
                ('image3', models.ImageField(blank=True, null=True, upload_to=Products.models.upload_image_path)),
                ('image4', models.ImageField(blank=True, null=True, upload_to=Products.models.upload_image_path)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.Profile')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]