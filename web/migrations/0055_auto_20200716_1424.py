# Generated by Django 3.0.7 on 2020-07-16 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0054_auto_20200710_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('pet_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='web.Pet')),
            ],
            options={
                'verbose_name': 'Katė',
                'verbose_name_plural': 'Katės',
            },
            bases=('web.pet',),
        ),
        migrations.CreateModel(
            name='CatProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Katės savybė')),
                ('cats', models.ManyToManyField(blank=True, related_name='_catproperty_cats_+', to='web.Cat',
                                                verbose_name='Katės')),
            ],
            options={
                'verbose_name': 'Katės savybė',
                'verbose_name_plural': 'Kačių savybės',
                'ordering': ['name'],
                'default_related_name': '+',
            },
        ),
        migrations.AddField(
            model_name='cat',
            name='properties',
            field=models.ManyToManyField(blank=True, related_name='_cat_properties_+', to='web.CatProperty',
                                         verbose_name='Savybės'),
        ),
    ]
