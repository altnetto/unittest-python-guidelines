from tests.system.conftest import BaseTest
import json


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')

            expected = {'message': 'Hello World!'}

            # modo mais simples de testar a carga da resposta
            self.assertDictEqual(resp.json, expected)
            # modo mais complexo de testar a carga da resposta
            self.assertDictEqual(json.loads(resp.get_data()), expected)
            
            self.assertEqual(resp.status_code, 200)