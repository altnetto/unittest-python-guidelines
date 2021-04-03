from unittest import TestCase
from unittest.mock import patch
from app.models.item import ItemModel
from app.app import create_app


class ItemTest(TestCase):

    def setUp(self):
        self.item = ItemModel('Caneta', 1.5)
        
        # app = create_app()
        # app.testing = True
        # self.app = app.test_client


    def test_create_item(self):
        self.assertEqual(self.item.name, 'Caneta')
        self.assertEqual(self.item.price, 1.5)

        
    def test_save_item(self):
        with patch('app.models.item.db.session.add') as mocked_db_add:
            with patch('app.models.item.db.session.commit') as mocked_db_commit:
                self.item.save_to_db()

                mocked_db_add.assert_called()
                mocked_db_commit.assert_called()


    def test_delete_item(self):
        with patch('app.models.item.db.session.delete') as mocked_db_delete:
            with patch('app.models.item.db.session.commit') as mocked_db_commit:
                self.item.delete_from_db()

                mocked_db_delete.assert_called()
                mocked_db_commit.assert_called()


    def test_find_by_name(self):
        pass
        # with self.app:
        #     self.item.save_to_db()
        #     resp = ItemModel.find_by_name('Caneta')
        #     self.assertEqual(resp, 'Caneta')