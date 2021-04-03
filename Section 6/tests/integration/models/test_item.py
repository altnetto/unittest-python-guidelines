from app.models.item import ItemModel
from tests.conftest import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)

            # verifica se o item não existe no banco de dados
            # o terceiro argumento é uma mensagem de erro personalizada, que pode ajudar muito no decorrer das execuções de testes
            self.assertIsNone(ItemModel.find_by_name('test'), f'Found an item with name {item.name!r} on database, but expected not to.')

            item.save_to_db()
            # verifica se o item existe no banco de dados
            self.assertIsNotNone(ItemModel.find_by_name('test'), f'Not found an item with name {item.name!r} on database, but expected to.')


            item.delete_from_db()
            # verifica se o item não existe no banco de dados
            self.assertIsNone(ItemModel.find_by_name('test'), f'Found an item with name {item.name!r} on database, but expected not to.')
