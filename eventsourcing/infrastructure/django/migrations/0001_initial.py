# Generated by Django 2.0 on 2017-12-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntegerSequencedItemRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_id', models.UUIDField()),
                ('position', models.BigIntegerField()),
                ('topic', models.CharField(max_length=255)),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'integer_sequenced_items',
            },
        ),
        migrations.CreateModel(
            name='SnapshotRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_id', models.UUIDField()),
                ('position', models.BigIntegerField()),
                ('topic', models.CharField(max_length=255)),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'snapshots',
            },
        ),
        migrations.CreateModel(
            name='StoredEventRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TimestampSequencedItemRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_id', models.UUIDField()),
                ('position', models.DecimalField(decimal_places=6, max_digits=24)),
                ('topic', models.CharField(max_length=255)),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'timestamp_sequenced_items',
            },
        ),
        migrations.AlterUniqueTogether(
            name='timestampsequenceditemrecord',
            unique_together={('sequence_id', 'position')},
        ),
        migrations.AlterUniqueTogether(
            name='snapshotrecord',
            unique_together={('sequence_id', 'position')},
        ),
        migrations.AlterUniqueTogether(
            name='integersequenceditemrecord',
            unique_together={('sequence_id', 'position')},
        ),
    ]
