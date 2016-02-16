from __future__ import unicode_literals
from django.db import models

class TypeStatus(models.Model):
    id = models.CharField(db_column='ID', max_length=25, primary_key=True)  # Field name made lowercase.
    label = models.CharField(db_column='LABEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    short_label = models.CharField(db_column='SHORT_LABEL', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'type_status'

class Category(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    label = models.CharField(db_column='LABEL', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'category'

class Member(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    cell_phone = models.CharField(db_column='CELL_PHONE', max_length=15)  # Field name made lowercase.
    nick_name = models.CharField(db_column='NICK_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    session_id = models.CharField(db_column='SESSION_ID', max_length=120, blank=True, null=True)  # Field name made lowercase.
    latest_login = models.DateTimeField(db_column='LATEST_LOGIN', blank=True, null=True)  # Field name made lowercase.
    fetch_back_pwd = models.CharField(db_column='FETCH_BACK_PWD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    account_number = models.CharField(db_column='ACCOUNT_NUMBER', max_length=45)  # Field name made lowercase.
    grade = models.CharField(db_column='GRADE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #status = models.CharField(db_column='STATUS', max_length=48)  # Field name made lowercase.
    status = models.ForeignKey('TypeStatus', on_delete= models.DO_NOTHING, db_column='STATUS_ID')
    #is_online = models.CharField(db_column='IS_ONLINE', max_length=48)  # Field name made lowercase. 2016-02-13
    is_online = models.BooleanField(db_column='IS_ONLINE')
    gender = models.CharField(db_column='GENDER', max_length=48, blank=True, null=True)  # Field name made lowercase.
    pic = models.CharField(db_column='PIC', max_length=300, blank=True, null=True)  # Field name made lowercase.
    email_addr = models.CharField(db_column='EMAIL_ADDR', max_length=48, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=48, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'member'

class Shop(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    shop_name = models.CharField(db_column='SHOP_NAME', max_length=255)  # Field name made lowercase.
    floor = models.IntegerField(db_column='FLOOR')  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=255)  # Field name made lowercase.
    logo = models.CharField(db_column='LOGO', max_length=1000)  # Field name made lowercase.
    true_scene = models.CharField(db_column='TRUE_SCENE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='TELEPHONE', max_length=20)  # Field name made lowercase.
    contact = models.CharField(db_column='CONTACT', max_length=32)  # Field name made lowercase.
    contact_tel = models.CharField(db_column='CONTACT_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    introduction = models.TextField(db_column='INTRODUCTION')  # Field name made lowercase.
    category = models.ForeignKey('Category', models.DO_NOTHING, db_column='CATEGORY_ID')  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    opening_time = models.DateTimeField(db_column='OPENING_TIME', blank=True, null=True)  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'shop'

class Product(models.Model):
    id = models.CharField(db_column='ID', max_length=25, primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=80)  # Field name made lowercase.
    picture = models.CharField(db_column='PICTURE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    unit_price = models.DecimalField(db_column='UNIT_PRICE', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    top_carriage_time = models.DateTimeField(db_column='TOP_CARRIAGE_TIME', blank=True, null=True)  # Field name made lowercase.
    shop = models.ForeignKey('Shop', models.DO_NOTHING, db_column='SHOP_ID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'product'
        unique_together = (('id', 'product_name'),)

class Evaluation(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    score = models.FloatField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT')  # Field name made lowercase.
    post_time = models.DateTimeField(db_column='POST_TIME')  # Field name made lowercase.
    member = models.ForeignKey('Member', on_delete = models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    pic = models.CharField(db_column='PIC', max_length=300, blank=True, null=True)  # Field name made lowercase.
    shop = models.ForeignKey('Shop', on_delete = models.DO_NOTHING, db_column='SHOP_ID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'evaluation'

class FavoritShop(models.Model):
    id = models.CharField(db_column='ID', max_length=25, primary_key=True)  # Field name made lowercase.
    shop = models.ForeignKey('Shop', models.DO_NOTHING, db_column='SHOP_ID')  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'favorit_shop'
        unique_together = (('shop', 'member'),)
        app_label = 'codefirst_app'

class Discount(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    picture = models.CharField(db_column='PICTURE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(db_column='DETAILS', max_length=300, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    shop = models.ForeignKey('Shop', on_delete = models.DO_NOTHING, db_column='SHOP_ID')  # Field name made lowercase.
    discount_value = models.IntegerField(db_column='DISCOUNT_VALUE', blank=True, null=True)  # Field name made lowercase.
    discount_unit = models.CharField(db_column='DISCOUNT_UNIT', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'discount'

class DiscountUser(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    member = models.ForeignKey('Member', on_delete = models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    #status_id = models.CharField(db_column='STATUS_ID', max_length=48, blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey('TypeStatus', on_delete= models.DO_NOTHING, db_column='STATUS_ID')
    discount = models.ForeignKey('Discount', on_delete = models.DO_NOTHING, db_column='DISCOUNT_ID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'discount_user'

# separate migration here when making migrations

class Order(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    #order_type_id = models.CharField(db_column='ORDER_TYPE_ID', max_length=48, blank=True, null=True)  # Field name made lowercase.
    order_type = models.ForeignKey('TypeStatus', on_delete= models.DO_NOTHING, db_column='ORDER_TYPE_ID', related_name='Order_set_of_order_type')
    order_datetime = models.DateTimeField(db_column='ORDER_DATETIME', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    member = models.ForeignKey(Member, models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    #status_id = models.CharField(db_column='STATUS_ID', max_length=48, blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey('TypeStatus', on_delete= models.DO_NOTHING, db_column='STATUS_ID', related_name='Order_set_of_status')
    is_used_discount = models.IntegerField(db_column='IS_USED_DISCOUNT', blank=True, null=True)  # Field name made lowercase.
    #discount_id = models.CharField(db_column='DISCOUNT_ID', max_length=48, blank=True, null=True)  # Field name made lowercase.
    discount = models.ForeignKey('discount', on_delete=models.DO_NOTHING, db_column='DISCOUNT_ID')

    class Meta:
        #managed = False
        db_table = 'order'

class OrderProduct(models.Model):
    id = models.CharField(db_column='ID', max_length=25, primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='PRODUCT_ID')  # Field name made lowercase.
    order = models.ForeignKey('Order', models.DO_NOTHING, db_column='ORDER_ID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'order_product'
        unique_together = (('product', 'order'),)

class Groupon(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    shop = models.ForeignKey('Shop', on_delete = models.DO_NOTHING, db_column='SHOP_ID')  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100)  # Field name made lowercase.
    picture = models.CharField(db_column='PICTURE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    original_price = models.DecimalField(db_column='ORIGINAL_PRICE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    current_price = models.DecimalField(db_column='CURRENT_PRICE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    start_time = models.DateField(db_column='START_TIME')  # Field name made lowercase.
    end_time = models.DateField(db_column='END_TIME')  # Field name made lowercase.
    details = models.TextField(db_column='DETAILS')  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'groupon'

class GrouponBackage(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupon_type = models.CharField(db_column='GROUPON_TYPE', max_length=48, blank=True, null=True)  # Field name made lowercase.
    #status_id = models.CharField(db_column='STATUS_ID', max_length=48, blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey('TypeStatus', on_delete= models.DO_NOTHING, db_column='STATUS_ID')
    member = models.ForeignKey('Member', on_delete = models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'goupon_backage'

class GrouponOrder(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    groupon = models.ForeignKey('Groupon', models.DO_NOTHING, db_column='GROUPON_ID')  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME')  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    #status_id = models.CharField(db_column='STATUS_ID', max_length=48)  # Field name made lowercase.
    status = models.ForeignKey('TypeStatus', on_delete= models.DO_NOTHING, db_column='STATUS_ID')
    settlement_time = models.DateTimeField(db_column='SETTLEMENT_TIME', blank=True, null=True)  # Field name made lowercase.
    order_type = models.CharField(db_column='ORDER_TYPE', max_length=48, blank=True, null=True)  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    #shop_id = models.CharField(db_column='SHOP_ID', max_length=48, blank=True, null=True)  # Field name made lowercase.
    shop = models.ForeignKey('Shop', on_delete = models.DO_NOTHING, db_column='SHOP_ID')

    class Meta:
        #managed = False
        db_table = 'groupon_order'

class Integral(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    balance = models.IntegerField(db_column='BALANCE')  # Field name made lowercase.
    expired_date = models.DateTimeField(db_column='EXPIRED_DATE', blank=True, null=True)  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'integral'

class IntegralTransaction(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT')  # Field name made lowercase.
    #trx_type_id = models.CharField(db_column='TRX_TYPE_ID', max_length=48)  # Field name made lowercase.
    trx_type = models.ForeignKey('TypeStatus', on_delete= models.DO_NOTHING, db_column='trx_type_id', related_name='Integraltransaction_set_of_trx_type')
    trx_datetime = models.DateTimeField(db_column='TRX_DATETIME')  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    #status_id = models.CharField(db_column='STATUS_ID', max_length=48, blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey('TypeStatus', on_delete= models.DO_NOTHING, db_column='STATUS_ID', related_name='Integraltransaction_set_of_status')
    #shop_id = models.CharField(db_column='SHOP_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shop = models.ForeignKey('Shop', on_delete = models.DO_NOTHING, db_column='SHOP_ID')

    class Meta:
        #managed = False
        db_table = 'integral_transaction'

class IntegralTransactionProduct(models.Model):
    id = models.CharField(db_column='ID', max_length=25,primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='PRODUCT_ID')  # Field name made lowercase.
    transaction = models.ForeignKey('IntegralTransaction', models.DO_NOTHING, db_column='TRANSACTION_ID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.
    integral_transaction_product_col = models.CharField(db_column='Integral_Transaction_product_col', max_length=45)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'integral_transaction_product'
        unique_together = (('product', 'transaction'),)