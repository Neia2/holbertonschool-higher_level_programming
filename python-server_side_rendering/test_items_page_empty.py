import unittest
from flask import Flask, render_template
from flask.testing import FlaskClient
import json
import os

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = Flask(__name__)
        self.client = self.app.test_client()

        # Define a route for the test
        @self.app.route('/items')
        def items():
            with open('items.json') as f:
                data = json.load(f)
            return render_template('items.html', items=data['items'])

        # Create an empty items.json file
        with open('items.json', 'w') as f:
            json.dump({"items": []}, f)

    def test_items_page_empty(self):
        # Send a request to the /items route
        response = self.client.get('/items')
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200, "Failed: Items page did not return status code 200")
        
        # Check that the response contains "No items found"
        self.assertIn(b'No items found', response.data, "Failed: Items page did not display 'No items found' for an empty list")

    def tearDown(self):
        # Remove the items.json file after test
        os.remove('items.json')

if __name__ == '__main__':
    unittest.main()
