# Generated by Django 2.0 on 2017-12-02 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ax', '0002_axtiming'),
    ]

    operations = [
        migrations.AlterField(
            model_name='axtiming',
            name='axtext',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ax.AxText'),
        ),
    ]