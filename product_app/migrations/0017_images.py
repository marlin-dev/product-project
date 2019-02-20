# Generated by Django 2.1.5 on 2019-02-16 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0016_auto_20190216_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(default='default.jpg', max_length=250, upload_to='pictures')),
                ('sekil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Productlar')),
            ],
        ),
    ]