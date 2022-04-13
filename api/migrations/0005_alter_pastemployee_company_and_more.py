# Generated by Django 4.0.4 on 2022-04-13 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_pastemployee_company_alter_pastemployee_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastemployee',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
        migrations.AlterField(
            model_name='presentemployee',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
    ]
