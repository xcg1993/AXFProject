# Generated by Django 2.0.6 on 2018-11-29 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0008_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPrice', models.FloatField()),
                ('ordertime', models.DateTimeField(auto_now=True)),
                ('orderstate', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.User')),
            ],
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='orders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Orders'),
        ),
    ]
