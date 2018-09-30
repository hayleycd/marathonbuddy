# Generated by Django 2.1.1 on 2018-09-30 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0002_auto_20180929_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coaching',
            name='run_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coaching.RunEvent'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='description',
            field=models.CharField(default='', max_length=240),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='url',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='runevent',
            name='city',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='runevent',
            name='cutoff_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='runevent',
            name='distance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='runevent',
            name='goal_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='runevent',
            name='state',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
