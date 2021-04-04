from app.models.item import ItemModel
from app.models.store import StoreModel
from app.models.user import UserModel
from tests.conftest import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        
        # on that point, we build a bridge to the BaseTest.setUp(),
        # so, we can access his properties, because, without that,
        # the ItemTest setUp() will override the BaseTest setUp()

        super(ItemTest, self).setUp()

        with self.app() as client:
            with self.app_context():
                auth_data = {'username': 'test', 'password': '1234'}
                auth_header = {'Content-Type': 'application/json'}
                
                StoreModel('test store').save_to_db()
                UserModel('test', '1234').save_to_db()

                auth_response = client.post('/auth',
                                            data = json.dumps(auth_data),
                                            headers = auth_header)

                auth_token = json.loads(auth_response.data)['access_token']

                self.access_token = f'JWT {auth_token}'
                self.header = { 'Authorization': self.access_token }



    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test')

                self.assertEqual(resp.status_code, 400)


    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test', headers = self.header)
                self.assertEqual(resp.status_code, 404)


    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                item_data = {'price': 19.99, 'store_id': 1}

                client.post('/item/test', headers = self.header, data = item_data)
                resp = client.get('/item/test', headers = self.header)

                expected = {'name': 'test', 'price': 19.99}

                self.assertDictEqual(json.loads(resp.data), expected)
                self.assertEqual(resp.status_code, 200)

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                item_data = {'price': 19.99, 'store_id': 1}

                client.post('/item/test', headers = self.header, data = item_data)
                resp = client.delete('/item/test')
                
                self.assertDictEqual(json.loads(resp.data), {'message': 'Item deleted'})


    def test_create_duplicated_item(self):
        with self.app() as client:
            with self.app_context():
                item_data = {'price': 19.99, 'store_id': 1}

                client.post('/item/test', headers = self.header, data = item_data)
                resp = client.post('/item/test', headers = self.header, data = item_data)

                expected = {'message': "An item with name 'test' already exists."}

                self.assertEqual(resp.status_code, 400)
                self.assertDictEqual(json.loads(resp.data), expected)


    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                item_data = {'price': 19.99, 'store_id': 1}

                resp = client.put('/item/test', headers = self.header, data = item_data)

                self.assertDictEqual(json.loads(resp.data), {'name': 'test', 'price': 19.99})


    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                original_item_data = {'price': 19.99, 'store_id': 1}
                updated_item_data = {'price': 15.99, 'store_id': 1}

                original_expected_response = {'name': 'test', 'price': 19.99}
                updated_expected_response = {'name': 'test', 'price': 15.99}

                resp1 = client.put('/item/test', headers = self.header, data = original_item_data)
                self.assertDictEqual(json.loads(resp1.data), original_expected_response)

                resp2 = client.put('/item/test', headers = self.header, data = updated_item_data)
                self.assertDictEqual(json.loads(resp2.data), updated_expected_response)


    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                ItemModel('test1', 15.99, 1).save_to_db()
                ItemModel('test2', 10.99, 1).save_to_db()
                ItemModel('test3', 17.99, 1).save_to_db()

                expected = { 'items': [ {'name': 'test1', 'price': 15.99},
                                        {'name': 'test2', 'price': 10.99}, 
                                        {'name': 'test3', 'price': 17.99} ] }

                resp = client.get('/items', headers = self.header)

                self.assertDictEqual(json.loads(resp.data), expected)

