# Generated by Django 2.0 on 2018-01-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0002_auto_20180123_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Totaling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins_id', models.CharField(max_length=12)),
                ('amount_fee', models.DecimalField(decimal_places=0, max_digits=8)),
            ],
        ),
    ]
