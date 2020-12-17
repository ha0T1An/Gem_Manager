# Generated by Django 3.1.3 on 2020-11-27 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gem_Manage_App', '0011_auto_20201127_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlesample',
            name='require',
        ),
        migrations.RemoveField(
            model_name='singlesample',
            name='status',
        ),
        migrations.AddField(
            model_name='sample',
            name='require',
            field=models.CharField(blank=True, max_length=50, verbose_name='检测要求'),
        ),
        migrations.AddField(
            model_name='sample',
            name='sampletype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gem_Manage_App.sampletype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='status',
            field=models.CharField(blank=True, max_length=50, verbose_name='样品状况'),
        ),
    ]
