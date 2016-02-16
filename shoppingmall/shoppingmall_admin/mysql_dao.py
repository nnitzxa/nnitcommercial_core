from shoppingmall_admin.models import *

class CategoryDAO:
    def add(self,parameter):
        obj = Category()
        obj.id = parameter['id']
        obj.label = parameter['label']
        obj.save()

    def update(self,parameter):
        obj = Category.objects.get(id = parameter['id'])
        obj.label = parameter['label']
        obj.save()

    def delete(self, param_id):
        obj = Category.objects.get(id = param_id)
        obj.delete()

    def get_by(self, param_id):
        qs = Category.objects.filter(id = param_id)
        if qs.count() > 0:
            return qs[0]
        else:
            return None

    def get_all(self):
        return Category.objects.all()

class DiscountDAO:
    def add(self, parameter):
        obj = Discount()
        obj.id = parameter['id']
        obj.title = parameter['title']
        obj.picture = parameter['picture']
        obj.start_date = parameter['start_date']
        obj.end_date = parameter['end_date']
        obj.details = parameter['details']
        obj.create_time = parameter['create_time']
        obj.shop = parameter['shop']
        obj.discount_value = parameter['discount_value']
        obj.discount_unit = parameter['discount_unit']
        obj.save()

    def update(self, parameter):
        obj = Discount.objects.get(id = parameter['id'])
        if 'title' in parameter:
            obj.title = parameter['title']
        if 'picture' in parameter:
            obj.picture = parameter['picture']
        if 'start_date' in parameter:
            obj.start_date = parameter['start_date']
        if 'end_date' in parameter:
            obj.end_date = parameter['end_date']
        if 'details' in parameter:
            obj.details = parameter['details']
        if 'create_time' in parameter:
            obj.create_time = parameter['create_time']
        if 'shop' in parameter:
            obj.shop = parameter['shop']
        if 'discount_value' in parameter:
            obj.discount_value = parameter['discount_value']
        if 'discount_unit' in parameter:
            obj.discount_unit = parameter['discount_unit']
        obj.save()

    def delete(self, param_id):
        Discount.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        qs = Discount.objects.filter(id = param_id)
        if qs.count() > 0:
            return qs[0]
        else:
            return None

    def get_all(self):
        return Discount.objects.all()

class DiscountUserDAO:
    def add(self, parameter):
        obj = DiscountUser()
        obj.id = parameter['id']
        obj.member = parameter['member']
        obj.code = parameter['code']
        obj.status = parameter['status']
        obj.discount = parameter['discount']
        obj.save()

    def update(self, parameter):
        obj = DiscountUser.objects.get(id = parameter['id'])
        if 'member' in parameter:
            obj.member = parameter['member']
        if 'code' in parameter:
            obj.code = parameter['code']
        if 'status' in parameter:
            obj.status = parameter['status']
        if 'discount' in parameter:
            obj.discount = parameter['discount']
        obj.save()

    def delete(self, param_id):
        DiscountUser.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        qs = DiscountUser.objects.get(id = param_id)
        if qs.count() > 0:
            return qs[0]
        else:
            return None

    def get_all(self):
        return DiscountUser.objects.all()

class EvaluationDAO:
    def add(self, parameter):
        obj = Evaluation()
        obj.id = parameter['id']
        obj.score = parameter['score']
        obj.content = parameter['content']
        obj.post_time = parameter['post_time']
        obj.member = parameter['member']
        obj.pic = parameter['pic']
        obj.shop = parameter['shop']
        obj.save()

    def update(self, parameter):
        obj = Evaluation.objects.get(id = parameter['id'])
        if 'score' in parameter:
            obj.score = parameter['score']
        if 'content' in parameter:
            obj.content = parameter['content']
        if 'post_time' in parameter:
            obj.post_time = parameter['post_time']
        if 'member' in parameter:
            obj.member = parameter['member']
        if 'pic' in parameter:
            obj.pic = parameter['pic']
        if 'shop' in parameter:
            obj.shop = parameter['shop']
        obj.save()

    def delete(self, param_id):
        Evaluation.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        qs = Evaluation.objects.filter(id = param_id)
        if qs.count() > 0:
            return qs[0]
        else:
            return None

    def get_all(self):
        return Evaluation.objects.all()

class FavoriteShopDAO:
    def add(self, parameter):
        obj = FavoritShop()
        obj.id = parameter['id']
        obj.shop = parameter['shoop']
        obj.member = parameter['member']
        obj.save()

    def update(self, parameter):
        obj = FavoritShop.objects.get(id = parameter['id'])
        if 'shop' in parameter:
            obj.shop = parameter['shoop']
        if 'member' in parameter:
            obj.member = parameter['member']
        obj.save()

    def delete(self, param_id):
        FavoritShop.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        qs = FavoritShop.objects.get(id = param_id)
        if qs.count() > 0:
            return qs[0]
        else:
            return None

    def get_all(self):
        return FavoritShop.objects.all()

class GrouponBackageDAO:
    def add(self, parameter):
        obj = GrouponBackage()
        obj.id = parameter['id']
        obj.code = parameter['code']
        obj.groupon_type = parameter['groupon_type']
        obj.status = parameter['status']
        obj.member = parameter['member']
        obj.save()

    def update(self, parameter):
        obj = GrouponBackage.objects.get(id = parameter['id'])
        if 'code' in parameter:
            obj.code = parameter['code']
        if 'groupon_type' in parameter:
            obj.groupon_type = parameter['groupon_type']
        if 'status' in parameter:
            obj.status = parameter['status']
        if 'member' in parameter:
            obj.member = parameter['member']
        obj.save()

    def delete(self, param_id):
        GrouponBackage.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        return GrouponBackage.objects.get(id = param_id)

    def get_all(self):
        return GrouponBackage.objects.all()

class GrouponDAO:
    def add(self, parameter):
        obj = Groupon()
        obj.id = parameter['id']
        obj.shop = parameter['shop']
        obj.title = parameter['title']
        obj.picture = parameter['picture']
        obj.original_price = parameter['original_price']
        obj.current_price = parameter['current_price']
        obj.start_time = parameter['start_time']
        obj.end_time = parameter['end_time']
        obj.details = parameter['details']
        obj.create_time = parameter['create_time']
        obj.save()

    def update(self, parameter):
        obj = Groupon.objects.get(id = parameter['id'])
        if 'shop' in parameter:
            obj.shop = parameter['shop']
        if 'title' in parameter:
            obj.title = parameter['title']
        if 'picture' in parameter:
            obj.picture = parameter['picture']
        if 'original_price' in parameter:
            obj.original_price = parameter['original_price']
        if 'current_price' in parameter:
            obj.current_price = parameter['current_price']
        if 'start_time' in parameter:
            obj.start_time = parameter['start_time']
        if 'end_time' in parameter:
            obj.end_time = parameter['end_time']
        if 'details' in parameter:
            obj.details = parameter['details']
        if 'create_time' in parameter:
            obj.create_time = parameter['create_time']
        obj.save()

    def delete(self, param_id):
        Groupon.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        return Groupon.objects.get(id = param_id)

    def get_all(self):
        return Groupon.objects.all()

class GrouponOrderDAO:
    def add(self, parameter):
        obj = GrouponOrder()
        obj.id = parameter['id']
        obj.groupon = parameter['groupon']
        obj.create_time = parameter['create_time']
        obj.amount = parameter['amount']
        obj.status = parameter['status']
        obj.settlement_time = parameter['settlement_time']
        obj.order_type = parameter['order_type']
        obj.member = parameter['member']
        obj.shop = parameter['shop']
        obj.save()


    def update(self, parameter):
        obj = GrouponOrder.objects.get(id = parameter['id'])
        if 'groupon' in parameter:
            obj.groupon = parameter['groupon']
        if 'create_time' in parameter:
            obj.create_time = parameter['create_time']
        if 'amount' in parameter:
            obj.amount = parameter['amount']
        if 'status' in parameter:
            obj.status = parameter['status']
        if 'settlement_time' in parameter:
            obj.settlement_time = parameter['settlement_time']
        if 'order_type' in parameter:
            obj.order_type = parameter['order_type']
        if 'member' in parameter:
            obj.member = parameter['member']
        if 'shop' in parameter:
            obj.shop = parameter['shop']
        obj.save()

    def delete(self, param_id):
        GrouponOrder.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        return GrouponOrder.objects.get(id = param_id)

    def get_all(self):
        return GrouponOrder.objects.all()

class IntegralDAO:
    def add(self, parameter):
        obj = Integral()
        obj.id = parameter['id']
        obj.balance = parameter['balance']
        obj.expired_date = parameter['expired_date']
        obj.member = parameter['member']
        obj.save()

    def update(self, parameter):
        obj = Integral.objects.get(id = parameter['id'])
        if 'balance' in parameter:
            obj.balance = parameter['balance']
        if 'expired_date' in parameter:
            obj.expired_date = parameter['expired_date']
        if 'member' in parameter:
            obj.member = parameter['member']
        obj.save()

    def delete(self, param_id):
        Integral.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        return Integral.objects.get(id = param_id)

    def get_all(self):
        return Integral.objects.all()

class IntegralTransactionDAO:
    def add(self, parameter):
        obj = IntegralTransaction()
        obj.id = parameter['id']
        obj.amount = parameter['amount']
        obj.trx_type = parameter['trx_type']
        obj.trx_datetime = parameter['trx_datetime']
        obj.member = parameter['member']
        obj.status = parameter['status']
        obj.shop = parameter['shop']
        obj.save()

    def update(self, parameter):
        obj = IntegralTransaction.objects.get(id = parameter['id'])
        if 'amount' in parameter:
            obj.amount = parameter['amount']
        if 'trx_type' in parameter:
            obj.trx_type = parameter['trx_type']
        if 'trx_datetime' in parameter:
            obj.trx_datetime = parameter['trx_datetime']
        if 'member' in parameter:
            obj.member = parameter['member']
        if 'status' in parameter:
            obj.status = parameter['status']
        if 'shop' in parameter:
            obj.shop = parameter['shop']
        obj.save()

    def delete(self, param_id):
        IntegralTransaction.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        return IntegralTransaction.objects.get(id = param_id)

    def get_all(self):
        return IntegralTransaction.objects.all()

class IntegralTrasactionProductDAO:
    def add(self, parameter):
        obj = IntegralTransactionProduct()
        obj.id = parameter['id']
        obj.product = parameter['product']
        obj.transaction = parameter['transaction']
        obj.quantity = parameter['quantity']
        obj.integral_transaction_product_col = parameter['integral_transaction_product_col']
        obj.save()

    def update(self, parameter):
        obj = IntegralTransactionProduct.objects.get(id = parameter['id'])
        if 'product' in parameter:
            obj.product = parameter['product']
        if 'transaction' in parameter:
            obj.transaction = parameter['transaction']
        if 'quantity' in parameter:
            obj.quantity = parameter['quantity']
        if 'integral_transaction_product_col' in parameter:
            obj.integral_transaction_product_col = parameter['integral_transaction_product_col']
        obj.save()

    def delete(self, param_id):
        IntegralTransactionProduct.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        return IntegralTransactionProduct.objects.get(id = param_id)

    def get_all(self):
        return IntegralTransactionProduct.objects.all()

class MemberDAO:
    def add(self, parameter):
        obj = Member()
        obj.id = parameter['id']
        obj.cell_phone = parameter['cell_phone']
        obj.nick_name = parameter['nick_name']
        obj.password = parameter['password']
        obj.session_id = parameter['session_id']
        obj.latest_login = parameter['latest_login']
        obj.fetch_back_pwd = parameter['fetch_back_pwd']
        obj.account_number = parameter['account_number']
        obj.grade = parameter['grade']
        obj.status = parameter['status']
        obj.is_online = parameter['is_online']
        obj.gender = parameter['gender']
        obj.pic = parameter['pic']
        obj.email_addr = parameter['email_addr']
        obj.type = parameter['type']
        obj.save()
        pass

    def update(self, parameter):
        obj = Member.objects.get(id = parameter['id'])
        if 'cell_phone' in parameter:
            obj.cell_phone = parameter['cell_phone']
        if 'nick_name' in parameter:
            obj.nick_name = parameter['nick_name']
        if 'password' in parameter:
            obj.password = parameter['password']
        if 'session_id' in parameter:
            obj.session_id = parameter['session_id']
        if 'latest_login' in parameter:
            obj.latest_login = parameter['latest_login']
        if 'fetch_back_pwd' in parameter:
            obj.fetch_back_pwd = parameter['fetch_back_pwd']
        if 'account_number' in parameter:
            obj.account_number = parameter['account_number']
        if 'grade' in parameter:
            obj.grade = parameter['grade']
        if 'status' in parameter:
            obj.status = parameter['status']
        if 'is_online' in parameter:
            obj.is_online = parameter['is_online']
        if 'gender' in parameter:
            obj.gender = parameter['gender']
        if 'pic' in parameter:
            obj.pic = parameter['pic']
        if 'email_addr' in parameter:
            obj.email_addr = parameter['email_addr']
        if 'type' in parameter:
            obj.type = parameter['type']

        obj.save()

        pass

    def delete(self, param_id):
        obj = Member.objects.get(id = param_id)
        obj.delete()
        pass

    def get_all(self):
        return Member.objects.all()
        pass

    def get_by(self, param_id):
        qs = Member.objects.filter(id = param_id)
        if qs.count() > 0:
            return qs[0]
        else:
            return None

class OrderDAO:
    def add(self, parameter):
        obj = Order()
        obj.id = parameter['id']
        obj.order_type = parameter['order_type']
        obj.order_datetime = parameter['order_datetime']
        obj.amount = parameter['amount']
        obj.member = parameter['member']
        obj.status = parameter['status']
        obj.is_used_discount = parameter['is_used_discount']
        obj.discount = parameter['discount']
        obj.save()

    def update(self, parameter):
        obj = Order.objects.get(id = parameter['id'])
        if 'order_type' in parameter:
            obj.order_type = parameter['order_type']
        if 'order_datetime' in parameter:
            obj.order_datetime = parameter['order_datetime']
        if 'amount' in parameter:
            obj.amount = parameter['amount']
        if 'member' in parameter:
            obj.member = parameter['member']
        if 'status' in parameter:
            obj.status = parameter['status']
        if 'is_used_discount' in parameter:
            obj.is_used_discount = parameter['is_used_discount']
        if 'discount' in parameter:
            obj.discount = parameter['discount']
        obj.save()

    def delete(self, param_id):
        Order.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        return Order.objects.get(id = param_id)

    def get_all(self):
        return Order.objects.all()

class OrderProductDAO:
    def add(self, parameter):
        obj = OrderProduct()
        obj.id = parameter['id']
        obj.product = parameter['product']
        obj.order = parameter['order']
        obj.quantity = parameter['quantity']
        obj.save()

    def update(self, parameter):
        obj = OrderProduct.objects.get(id = parameter['id'])
        if 'product' in parameter:
            obj.product = parameter['product']
        if 'order' in parameter:
            obj.order = parameter['order']
        if 'quantity' in parameter:
            obj.quantity = parameter['quantity']
        obj.save()

    def delete(self, param_id):
        OrderProduct.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        return OrderProduct.objects.get(id = param_id)

    def get_all(self):
        return OrderProduct.objects.all()

class ProductDAO:
    def add(self, parameter):
        obj = Product()
        obj.id = parameter['id']
        obj.product_name = parameter['product_name']
        obj.picture = parameter['picture']
        obj.unit_price = ['unit_price']
        obj.top_carriage_time = parameter['top_carriage_time']
        obj.shop = parameter['shop']
        obj.save()

    def update(self, parameter):
        obj = Product.objects.get(id = parameter['id'])
        if 'product_time' in parameter:
            obj.product_name = parameter['product_name']
        if 'picture' in parameter:
            obj.picture = parameter['picture']
        if 'unit_price' in parameter:
            obj.unit_price = ['unit_price']
        if 'top_carriage_time' in parameter:
            obj.top_carriage_time = parameter['top_carriage_time']
        if 'shop' in parameter:
            obj.shop = parameter['shop']
        obj.save()

    def delete(self, param_id):
        Product.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        return Product.objects.get(id = param_id['id'])

    def get_all(self):
        return Product.objects.all()

class ShopDAO:
    def add(self, parameter):
        shop = Shop()
        shop.id = parameter['id']
        shop.shop_name = parameter['shop_name']
        shop.floor = parameter['floor']
        shop.location = parameter['location']
        shop.logo = parameter['logo']
        shop.true_scene = parameter['true_scene']
        shop.telephone = parameter['telephone']
        shop.contact = parameter['contact']
        shop.contact_tel = parameter['contact_tel']
        shop.introduction = parameter['introduction']
        shop.category = parameter['category']
        shop.create_time = parameter['create_time']
        shop.opening_time = parameter['opening_time']
        shop.member = parameter['member']
        shop.save()

    def update(self, parameter):
        obj = Shop.objects.get(id = parameter['id'])
        if 'shop_name' in parameter:
            obj.shop_name = parameter['shop_name']
        if 'floor' in parameter:
            obj.floor = parameter['floor']
        if 'location' in parameter:
            obj.location = parameter['location']
        if 'logo' in parameter:
            obj.logo = parameter['logo']
        if 'true_scene' in parameter:
            obj.true_scene = parameter['true_scene']
        if 'telephone' in parameter:
            obj.telephone = parameter['telephone']
        if 'contact' in parameter:
            obj.contact = parameter['contact']
        if 'contact_tel' in parameter:
            obj.contact_tel = parameter['contact_tel']
        if 'introduction' in parameter:
            obj.introduction = parameter['introduction']
        if 'category' in parameter:
            obj.category = parameter['category']
        if 'create_time' in parameter:
            obj.create_time = parameter['create_time']
        if 'opening_time' in parameter:
            obj.opening_time = parameter['opening_time']
        if 'member' in parameter:
            obj.member = parameter['member']

        obj.save()

    def delete(self, param_id):
        Shop.objects.get(id = param_id).delete()

    def get_by(self, param_id):
        qs = Shop.objects.filter(id = param_id)
        if qs.count() > 0:
            return qs[0]
        else:
            return None

    def get_all(self):
        return Shop.objects.all()

class TypeStatusDAO:
    def add(self, parameter):
        obj = TypeStatus()
        obj.id = parameter['id']
        obj.label = parameter['label']
        obj.short_label = parameter['short_label']
        obj.save()

    def update(self, parameter):
        obj = TypeStatus.objects.get(id = parameter['id'])
        obj.label = parameter['label']
        obj.short_label = parameter['short_label']
        obj.save()

    def delete(self, param_id):
        obj = TypeStatus.objects.get(id = param_id)
        obj.delete()

    def get_all(self):
        return TypeStatus.objects.all()

    def get_by(self, param_id):
        return TypeStatus.objects.get(id = param_id)