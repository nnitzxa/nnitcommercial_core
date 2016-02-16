from django.test import TestCase
from datetime import *
from shoppingmall_admin.mysql_dao import *
import shortuuid
from shoppingmall_admin.models import *
from dateutil import tz


class TypeStatusDAOTestCase(TestCase):
    def setUp(self):
        pass

    def test_add(self):
        dao = TypeStatusDAO()
        #add
        id = shortuuid.uuid()
        parameter = {'id':id, 'label':'label', 'short_label':'short'}
        dao.add(parameter)

        #get
        result = TypeStatus.objects.filter(id=id).count()

        #delete
        TypeStatus.objects.get(id = id).delete()

        #assert
        self.assertTrue(result == 1)
        pass


    def test_update(self):
        dao = TypeStatusDAO()
        #add
        id = shortuuid.uuid()
        parameter = {'id':id, 'label':'label', 'short_label':'short'}
        dao.add(parameter)

        #udpate
        parameter = {'id':id, 'label':'label1', 'short_label':'short1'}
        dao.update(parameter)

        #get
        result = TypeStatus.objects.get(id=id)

        #delete
        result.delete()

        #print(result.label,result.short_label)
        #assert
        self.assertTrue(result.label == 'label1')
        self.assertTrue(result.short_label == 'short1')
        pass

    def test_delete(self):
        dao = TypeStatusDAO()
        #add
        id = shortuuid.uuid()
        parameter = {'id':id, 'label':'label', 'short_label':'short'}
        dao.add(parameter)

        #delete
        dao.delete(id)

        #get
        result = TypeStatus.objects.filter(id=id).count()
        #print(result)
        #assert
        self.assertTrue(result == 0)

        pass

    def test_get_all(self):
        dao = TypeStatusDAO()
        #add 2
        parameters = []
        parameters.append( {'id':shortuuid.uuid(), 'label':'label', 'short_label':'short'})
        parameters.append({'id':shortuuid.uuid(), 'label':'label1', 'short_label':'short1'})
        for parameter in parameters:
            dao.add(parameter)

        #get all
        qs = dao.get_all()
        result = qs.count()

        #delete all
        for parameter in parameters:
            TypeStatus.objects.get(id = parameter['id']).delete()

        self.assertTrue(result == 2)
        pass

    def test_get_by(self):
        dao = TypeStatusDAO()

         #add
        id = shortuuid.uuid()
        parameter = {'id':id, 'label':'label', 'short_label':'short'}
        dao.add(parameter)

        result = dao.get_by(id)

        self.assertIsNotNone(result) #will throw an exception

class MemberDAOTestCase(TestCase):

    parameter = {}
    dao = ''
    flag = True

    def setUp(self):
        self.dao = MemberDAO()
        self.parameter = self.get_new_parameter()
        self.dao.add(self.parameter)

        # self.parameter['id'] = shortuuid.uuid()
        # self.parameter['cell_phone'] = '182-0000-1111'
        # self.parameter['nick_name'] = 'jasmine'
        # self.parameter['password'] = 'initial'
        # self.parameter['session_id'] = '1234'
        # self.parameter['latest_login'] = datetime.now() + timedelta(days = -1) #yesterday
        # self.parameter['fetch_back_pwd'] = 'test'
        # self.parameter['account_number'] = '1234567890'
        # self.parameter['grade'] = 'test'
        # #insert a typestatus first
        # status = TypeStatus.objects.get_or_create(id = shortuuid.uuid(), label = 'member status', short_label = 'normal')
        # self.parameter['status'] = status[0]
        # self.parameter['is_online'] = True
        # self.parameter['gender'] = 'F'
        # self.parameter['pic'] = 'http://test/jasmine.jpg'
        # self.parameter['email_addr'] = 'zxa@nnit.com'
        # self.parameter['type'] = 'test type'
        pass

    def test_add(self):
        qs = Member.objects.filter(id = self.parameter['id'])

        expected = self.parameter
        result = qs[0]


        local_latest_login = result.latest_login.astimezone(tz.gettz('CST'))
        local = datetime.strftime(local_latest_login,"%Y-%m-%d %H:%M:%S")


        self.assertEquals(result.cell_phone, expected['cell_phone'])
        self.assertEquals(result.nick_name, expected['nick_name'])
        self.assertEquals(result.password, expected['password'])
        self.assertEquals(result.session_id, expected['session_id'])

        self.assertEquals(local, datetime.strftime(expected['latest_login'],"%Y-%m-%d %H:%M:%S"))
        self.assertEquals(result.fetch_back_pwd, expected['fetch_back_pwd'])
        self.assertEquals(result.account_number, expected['account_number'])
        self.assertEquals(result.grade, expected['grade'])
        self.assertEquals(result.status, expected['status'])
        self.assertEquals(result.is_online, expected['is_online'])
        self.assertEquals(result.gender, expected['gender'])
        self.assertEquals(result.pic, expected['pic'])
        self.assertEquals(result.email_addr, expected['email_addr'])
        self.assertEquals(result.type, expected['type'])

        result.delete()

    def test_update(self):
        new_parameter = self.get_new_parameter()
        new_parameter['id'] = self.parameter['id']

        # self.parameter['cell_phone'] = '182-0000-1111_1'
        # self.parameter['nick_name'] = 'jasmine_1'
        # self.parameter['password'] = 'initial_1'
        # self.parameter['session_id'] = '1234_1'
        # self.parameter['latest_login'] = datetime.now() + timedelta(days = -2)
        # self.parameter['fetch_back_pwd'] = 'test_1'
        # self.parameter['account_number'] = '1234567890_1'
        # self.parameter['grade'] = 'test_1'
        # #insert a typestatus first
        # status = TypeStatus.objects.get_or_create(id = shortuuid.uuid(), label = 'member status', short_label = 'abnormal')
        # self.parameter['status'] = status[0]
        # self.parameter['is_online'] = False
        # self.parameter['gender'] = 'M'
        # self.parameter['pic'] = 'http://test/jasmine_1.jpg'
        # self.parameter['email_addr'] = 'zxa_1@nnit.com'
        # self.parameter['type'] = 'test type_1'

        self.dao.update(self.parameter)

        qs = Member.objects.filter(id = self.parameter['id'])

        expected = self.parameter
        result = qs[0]

        local_format = '%Y-%m-%d %H:%M:%S'
        local_latest_login = result.latest_login.astimezone(tz.gettz('CST'))
        local_latest_login = datetime.strftime(local_latest_login,local_format)

        self.assertEquals(result.cell_phone, expected['cell_phone'])
        self.assertEquals(result.nick_name, expected['nick_name'])
        self.assertEquals(result.password, expected['password'])
        self.assertEquals(result.session_id, expected['session_id'])

        self.assertEquals(local_latest_login, datetime.strftime(expected['latest_login'],local_format))
        self.assertEquals(result.fetch_back_pwd, expected['fetch_back_pwd'])
        self.assertEquals(result.account_number, expected['account_number'])
        self.assertEquals(result.grade, expected['grade'])
        self.assertEquals(result.status, expected['status'])
        self.assertEquals(result.is_online, expected['is_online'])
        self.assertEquals(result.gender, expected['gender'])
        self.assertEquals(result.pic, expected['pic'])
        self.assertEquals(result.email_addr, expected['email_addr'])
        self.assertEquals(result.type, expected['type'])

        result.delete()

    def get_new_parameter(self):
        new_parameter = {}
        new_parameter['id'] = shortuuid.uuid()

        random_str = datetime.strftime(datetime.now(),"%H%M%S")

        new_parameter['cell_phone'] = random_str
        new_parameter['nick_name'] = random_str
        new_parameter['password'] = random_str
        new_parameter['session_id'] = random_str
        new_parameter['latest_login'] = datetime.now() + timedelta(days = -1) #yesterday
        new_parameter['fetch_back_pwd'] = random_str
        new_parameter['account_number'] = random_str
        new_parameter['grade'] = random_str
        #insert a typestatus first
        status = TypeStatus.objects.get_or_create(id = shortuuid.uuid(), label = 'member status', short_label = random_str)
        new_parameter['status'] = status[0]
        new_parameter['is_online'] = not self.flag
        new_parameter['gender'] = random_str
        new_parameter['pic'] = random_str
        new_parameter['email_addr'] = random_str
        new_parameter['type'] = random_str

        return new_parameter


    def test_delete(self):
        self.dao.delete(self.parameter['id'])
        qs = Member.objects.filter(id = self.parameter['id'])
        result = qs.count()
        expected = 0
        self.assertEquals(result, expected)

    def test_get_by(self):
        result = self.dao.get_by(self.parameter['id'])
        self.assertIsNotNone(result)

    def test_get_all(self):
        new_parameter = self.get_new_parameter()
        self.dao.add(new_parameter)

        qs = self.dao.get_all()
        result = qs.count()
        expected = 2
        self.assertEquals(result, expected)