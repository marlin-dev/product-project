# Generated by Django 2.1.5 on 2019-02-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0014_productlar_məzənnə'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlar',
            name='məzənnə',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='productlar',
            name='qiymeti',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]