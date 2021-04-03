from app.models.store import StoreModel
from tests.conftest import BaseTest


class StoreTest(BaseTest):
    def test_create_store(self):

        store = StoreModel('test')

        self.assertEqual(store.name, 'test')


    def test_create_store_items_empty(self):
        store = StoreModel('test')

        self.assertListEqual(store.items.all(), [])