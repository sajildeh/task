# Generated by Django 2.0.3 on 2019-07-04 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0003_auto_20190704_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiskAvg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(default=0, max_length=100)),
                ('AvgDiskAvailable', models.FloatField(default=0)),
                ('AvgDiskFree', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'DiskAvg',
                'verbose_name_plural': 'DiskAvgs',
                'db_table': 'DiskAvg',
            },
        ),
        migrations.CreateModel(
            name='MemoryAvg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(default=0, max_length=100)),
                ('AvgMemoryAvailable', models.FloatField(default=0)),
                ('AvgMemoryFree', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'MemoryAvg',
                'verbose_name_plural': 'MemoryAvgs',
                'db_table': 'MemoryAvg',
            },
        ),
        migrations.RenameModel(
            old_name='CPU',
            new_name='CPUAvg',
        ),
        migrations.AlterModelOptions(
            name='cpuavg',
            options={'verbose_name': 'CPUAvg', 'verbose_name_plural': 'CPUAvgs'},
        ),
        migrations.RenameField(
            model_name='cpuavg',
            old_name='cpuColumn',
            new_name='cpuAvgColumn',
        ),
        migrations.AlterModelTable(
            name='cpuavg',
            table='CPUAvg',
        ),
    ]
