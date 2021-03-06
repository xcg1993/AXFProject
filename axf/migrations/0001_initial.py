# Generated by Django 2.0.6 on 2018-11-26 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mainshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('categoryid', models.CharField(max_length=30)),
                ('brandname', models.CharField(max_length=30)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=30)),
                ('productid1', models.CharField(max_length=30)),
                ('longname1', models.CharField(max_length=50)),
                ('price1', models.FloatField()),
                ('marketprice1', models.FloatField()),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=30)),
                ('productid2', models.CharField(max_length=30)),
                ('longname2', models.CharField(max_length=50)),
                ('price2', models.FloatField()),
                ('marketprice2', models.FloatField()),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=30)),
                ('productid3', models.CharField(max_length=30)),
                ('longname3', models.CharField(max_length=50)),
                ('price3', models.FloatField()),
                ('marketprice3', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Mustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('trackid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('trackid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('trackid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('trackid', models.CharField(max_length=30)),
            ],
        ),
    ]
