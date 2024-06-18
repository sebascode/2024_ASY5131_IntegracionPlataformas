# test Factura.py
import unittest
import json

from app import app


class FacturaTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()
    
    def test_successful_boleta(self):
        # Given
        payload = json.dumps({
            "id_producto": 0,
            "precio": 0,
            "cantidad": 0,
            "total_venta": 0,
            "id_cliente": 0,
            "nombre_cliente": "",
            "direccion_cliente": ""
        })

        # when
        response = self.app.post('/api/boleta', headers={"Content-Type": "application/json"}, data=payload)
        
        # Then
        self.assertEqual(200, response.status_code)
