from app.models.store import StoreModel
from app.models.item import ItemModel
from tests.conftest import BaseTest
import json

class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/store/test')

                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertEqual(response.status_code, 201)
                self.assertDictEqual(json.loads(response.data),
                                    {'name': 'test', 'items': []})


    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                resp1 = client.post('/store/test')

                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertEqual(resp1.status_code, 201)
                self.assertDictEqual(json.loads(resp1.data),
                                    {'name': 'test', 'items': []})


                resp2 = client.post('/store/test')

                self.assertEqual(resp2.status_code, 400)
                self.assertDictEqual(json.loads(resp2.data),
                                    {'message': "A store with name 'test' already exists."})


    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')

                resp = client.delete('/store/test')

                self.assertDictEqual(json.loads(resp.data),
                                    {'message': 'Store deleted'})


    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')

                resp = client.get('/store/test')

                self.assertDictEqual(json.loads(resp.data),
                                    {'name': 'test', 'items': []})


    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/store/test')

                self.assertEqual(resp.status_code, 404)
                self.assertDictEqual(json.loads(resp.data),
                                    {'message': 'Store not found'})
                self.assertIsNone(StoreModel.find_by_name('test'))


    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                resp1 = client.get('/stores')

                self.assertDictEqual(json.loads(resp1.data),
                                    {'stores': []})

                client.post('/store/test')
                
                resp2 = client.get('/stores')

                expected = {'stores': [ { 'name': 'test', 'items': [] } ] }

                self.assertDictEqual(json.loads(resp2.data), expected)

                client.post('/store/test2')
                
                resp3 = client.get('/stores')

                self.assertEqual(len(json.loads(resp3.data)['stores']), 2)

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                
                resp = client.get('/stores')

                store_test_info = json.loads(resp.data)['stores'][0]
                items_store_test_info = store_test_info['items']

                self.assertIsNotNone(store_test_info)
                self.assertListEqual(items_store_test_info, [])

                ItemModel('item1', 19.99, 1).save_to_db()

                resp1 = client.get('/stores')
                store_test_info = json.loads(resp1.data)['stores'][0]
                items_store_test_info = store_test_info['items']

                self.assertListEqual(items_store_test_info,
                                    [ { 'name': 'item1', 'price': 19.99 } ])