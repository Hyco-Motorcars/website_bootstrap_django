# Generated by Django 2.1.7 on 2021-06-14 20:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('type', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=120)),
                ('model', models.CharField(max_length=120)),
                ('VIN', models.CharField(max_length=120)),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True)),
                ('for_sale', models.BooleanField(default=True)),
                ('listing_price', models.DecimalField(blank=True, decimal_places=2, default=50000, max_digits=1000, null=True)),
                ('exterior_color', models.TextField(blank=True, default='Black', null=True)),
                ('interior', models.TextField(blank=True, default='Beige', null=True)),
                ('num_doors', models.IntegerField(blank=True, default=4, null=True)),
                ('num_seats', models.IntegerField(blank=True, default=5, null=True)),
                ('engine', models.CharField(blank=True, default='V8 Inline-Six', max_length=120, null=True)),
                ('transmission', models.CharField(blank=True, default='Manual', max_length=120, null=True)),
                ('wheels', models.CharField(blank=True, default='chrome wire', max_length=120, null=True)),
                ('tires', models.CharField(blank=True, default='Firestone', max_length=120, null=True)),
                ('brakes', models.CharField(blank=True, default='Disc', max_length=120, null=True)),
                ('steering_wheel', models.CharField(blank=True, default='3-spoke', max_length=120, null=True)),
                ('sunroof', models.BooleanField(blank=True, default=False, null=True)),
                ('convertible', models.BooleanField(blank=True, default=False, null=True)),
                ('speedometer', models.IntegerField(blank=True, default=100, null=True)),
                ('torque', models.IntegerField(blank=True, default=250, null=True)),
                ('horsepower', models.IntegerField(blank=True, default=300, null=True)),
                ('audio_system', models.TextField(blank=True, default='Stock', null=True)),
                ('cooling_system', models.BooleanField(blank=True, default=True, null=True)),
                ('heating_system', models.BooleanField(blank=True, default=True, null=True)),
                ('id', models.CharField(default=uuid.uuid4, max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='vehicle_image',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.Vehicle'),
        ),
    ]