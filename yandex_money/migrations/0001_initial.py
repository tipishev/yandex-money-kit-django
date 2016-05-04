# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import yandex_money.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='Время создания', auto_now_add=True)),
                ('shop_id', models.PositiveIntegerField(verbose_name='ID магазина', default=0)),
                ('scid', models.PositiveIntegerField(verbose_name='Номер витрины', default=0)),
                ('customer_number', models.CharField(max_length=64, verbose_name='Идентификатор плательщика', default=yandex_money.models.uuid4_replaced)),
                ('order_amount', models.DecimalField(max_digits=15, verbose_name='Сумма заказа', decimal_places=2)),
                ('article_id', models.PositiveIntegerField(null=True, verbose_name='Идентификатор товара', blank=True)),
                ('payment_type', models.CharField(max_length=2, verbose_name='Способ платежа', choices=[('PC', 'Кошелек Яндекс.Деньги'), ('AC', 'Банковская карта'), ('GP', 'Наличными через кассы и терминалы'), ('MC', 'Счет мобильного телефона'), ('WM', 'Кошелек WebMoney'), ('SB', 'Сбербанк: оплата по SMS или Сбербанк Онлайн'), ('AB', 'Альфа-Клик'), ('MA', 'MasterPass'), ('PB', 'Интернет-банк Промсвязьбанка'), ('QW', 'QIWI Wallet'), ('QP', 'Доверительный платеж (Куппи.ру)')], default='PC')),
                ('order_number', models.CharField(max_length=64, verbose_name='Номер заказа', default=yandex_money.models.uuid4_replaced)),
                ('cps_email', models.EmailField(max_length=100, verbose_name='Email плательщика', blank=True, null=True)),
                ('cps_phone', models.CharField(max_length=15, verbose_name='Телефон плательщика', blank=True, null=True)),
                ('success_url', models.URLField(verbose_name='URL успешной оплаты', default='')),
                ('fail_url', models.URLField(verbose_name='URL неуспешной оплаты', default='')),
                ('status', models.CharField(max_length=16, verbose_name='Статус', choices=[('processed', 'Processed'), ('success', 'Success'), ('fail', 'Fail')], default='processed')),
                ('invoice_id', models.PositiveIntegerField(null=True, verbose_name='Номер транзакции оператора', blank=True)),
                ('shop_amount', models.DecimalField(null=True, verbose_name='Сумма полученная на р/с', blank=True, help_text='За вычетом процента оператора', max_digits=15, decimal_places=2)),
                ('order_currency', models.PositiveIntegerField(verbose_name='Валюта', choices=[(643, 'Рубли'), (10643, 'Тестовая валюта')], default=643)),
                ('shop_currency', models.PositiveIntegerField(null=True, verbose_name='Валюта полученная на р/с', blank=True, choices=[(643, 'Рубли'), (10643, 'Тестовая валюта')], default=643)),
                ('performed_datetime', models.DateTimeField(null=True, verbose_name='Время выполнение запроса', blank=True)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь', blank=True)),
            ],
            options={
                'verbose_name_plural': 'платежи',
                'ordering': ('-pub_date',),
                'verbose_name': 'платёж',
            },
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together=set([('shop_id', 'order_number')]),
        ),
    ]
