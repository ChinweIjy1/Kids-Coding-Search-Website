import unittest
import json
from app import create_app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_api(self):
        # Test GET request to /api/levels
        response = self.client.get('/api/levels')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn('levels', data)

        # Test POST request to /api/levels with valid data
        data = {'age': 10, 'completed_projects': 0, 'completed_courses': 0, 'languages': ['Scratch'], 'tools': [], 'complexity': 1}
        headers = {'Content-Type': 'application/json'}
        response = self.client.post('/api/levels', data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn('level', data)
        self.assertEqual(data['level'], 'Beginner')

        # Test POST request to /api/levels with invalid data
        data = {'age': 0, 'completed_projects': 0, 'completed_courses': 0, 'languages': ['Scratch'], 'tools': [], 'complexity': 1}
        headers = {'Content-Type': 'application/json'}
        response = self.client.post('/api/levels', data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 400)
