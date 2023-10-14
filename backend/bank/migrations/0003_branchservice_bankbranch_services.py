# Generated by Django 4.2.5 on 2023-10-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_bankbranch_openinghours_alter_atm_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название типа услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.AddField(
            model_name='bankbranch',
            name='services',
            field=models.ManyToManyField(to='bank.branchservice', verbose_name='Предоставляемые услуги'),
        ),
    ]
