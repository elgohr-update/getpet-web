# Generated by Django 2.2.2 on 2019-06-23 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20190623_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelter',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shelters', to='web.Region', verbose_name='Regionas'),
        ),
    ]
