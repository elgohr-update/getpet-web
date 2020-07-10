# Generated by Django 3.0.7 on 2020-07-10 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0051_auto_20200709_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.Pet')),
                ('dog_size', models.SmallIntegerField(choices=[(None, 'Nepatikslinta'), (1, 'Mažas'), (2, 'Vidutinis'), (3, 'Didelis')], verbose_name='Dydis')),
            ],
            options={
                'verbose_name': 'Šuo',
                'verbose_name_plural': 'Šunys',
            },
            bases=('web.pet',),
        ),
        migrations.CreateModel(
            name='DogProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Šuns savybė')),
                ('dogs', models.ManyToManyField(blank=True, related_name='_dogproperty_dogs_+', to='web.Dog', verbose_name='Gyvūnai')),
            ],
            options={
                'verbose_name': 'Šuns savybė',
                'verbose_name_plural': 'Šuns savybės',
                'ordering': ['name'],
                'default_related_name': '+',
            },
        ),
        migrations.AddField(
            model_name='dog',
            name='dog_properties',
            field=models.ManyToManyField(blank=True, related_name='_dog_dog_properties_+', to='web.DogProperty', verbose_name='Šuns savybės'),
        ),
    ]
