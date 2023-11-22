# Generated by Django 3.1 on 2020-08-17 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaseno', models.IntegerField(default=1)),
                ('purchase_date', models.DateField(verbose_name='purchase date')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('joining_date', models.DateField(auto_now_add=True, verbose_name='joining date')),
                ('address', models.CharField(blank=True, max_length=150)),
                ('mobile_no', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HSNCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn_code', models.CharField(max_length=50)),
                ('rate', models.FloatField(default=18.0)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='None', max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('hsn_code', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='shop.hsncode')),
                ('ingredient', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='shop.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(default='', max_length=50)),
                ('mfgdate', models.DateField(verbose_name='manufacture')),
                ('expirydate', models.DateField(verbose_name='expiry date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetailBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packing', models.CharField(default='', max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('batch_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productbatch')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=50)),
                ('mfgdate', models.DateTimeField(verbose_name='manufacture')),
                ('expirydate', models.DateTimeField(verbose_name='expiry date')),
                ('packing', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='BillTest2',
            fields=[
                ('purchaseno', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateField(verbose_name='purchase date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customerdetail')),
            ],
        ),
        migrations.CreateModel(
            name='BillItemsTest2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productBatch', models.CharField(max_length=50, null=True)),
                ('productPacking', models.CharField(max_length=50, null=True)),
                ('productQuantity', models.IntegerField(default=1)),
                ('productPrice', models.FloatField(default=0)),
                ('productTotalPrice', models.FloatField(default=0)),
                ('productName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills22', to='shop.productdetailbatch')),
                ('purchaseno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills22', to='shop.billtest2')),
            ],
        ),
        migrations.CreateModel(
            name='BillItemsTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productBatch', models.CharField(max_length=50, null=True)),
                ('productPacking', models.CharField(max_length=50, null=True)),
                ('productQuantity', models.IntegerField(default=1)),
                ('productPrice', models.FloatField(default=0)),
                ('productTotalPrice', models.FloatField(default=0)),
                ('productName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills2', to='shop.productdetailbatch')),
                ('purchaseno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills2', to='shop.bill')),
            ],
        ),
        migrations.CreateModel(
            name='BillItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100, null=True)),
                ('productBatch', models.CharField(max_length=50, null=True)),
                ('productPacking', models.CharField(max_length=50, null=True)),
                ('productQuantity', models.IntegerField(default=1)),
                ('productPrice', models.FloatField(default=0)),
                ('productTotalPrice', models.FloatField(default=0)),
                ('purchaseno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='shop.bill')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customerdetail'),
        ),
    ]
