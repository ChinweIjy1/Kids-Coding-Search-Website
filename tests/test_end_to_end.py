import unittest
import json
import subprocess
import time
import requests

class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        self.process = subprocess.Popen(['python', 'run.py'])
        time.sleep(1)  # Wait for server to start up

    def tearDown(self):
        self.process.terminate()

    def test_api(self):
        # Test GET request to /api/levels
        response = requests.get('http://localhost:5000/api/levels')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertIn('levels', data)

        # Test POST request to /api/levels with valid data
        data = {'age': 10, 'completed_projects': 0, 'completed_courses': 0, 'languages': ['Scratch'], 'tools': [], 'complexity': 1}
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://localhost:5000/api/levels', headers=headers, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertIn('level', data)
        self.assertIn('message', data)

        # Test POST request to /api/levels with invalid data
        data = {'age': 'not a number', 'completed_projects': 'not a number', 'completed_courses': 'not a number', 'languages': ['Scratch'], 'tools': [], 'complexity': 'not a number'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://localhost:5000/api/levels', headers=headers, data=json.dumps(data))
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.text)
        self.assertIn('message', data)
