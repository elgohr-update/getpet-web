# Generated by Django 3.0.6 on 2020-05-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_auto_20200512_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Laukia šeimininko'), (2, 'Laikinai paimtas per GetPet'), (3, 'Paimtas visam laikui per GetPet'), (4, 'Paimtas ne per GetPet'), (5, 'Laikinai neieško namų')], db_index=True, default=1, help_text='Gyvūnai su statusu laukiantys šeimininko yra rodomi programėlėje.', verbose_name='Gyvūno statusas'),
        ),
    ]
