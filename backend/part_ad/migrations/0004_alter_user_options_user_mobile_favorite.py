# Generated by Django 4.1.6 on 2023-03-31 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part_ad', '0003_alter_parcel_recipient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('part_ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part_ad.carpart', verbose_name='Favorite AD')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part_ad.user', verbose_name='Added To favorite by')),
            ],
            options={
                'verbose_name': 'Favorite',
                'verbose_name_plural': 'Favorites',
                'ordering': ['-create_date'],
            },
        ),
    ]
