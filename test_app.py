from flask_testing import TestCase
from flask import Flask
import unittest
import api_requests

class test_cases(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_single_ticket_request(self):
        ticket_response = api_requests.get_single_ticket(1)
        data = ticket_response['ticket']
        self.assertEqual(data["subject"], "Sample ticket: Meet the ticket")

    def test_tickets_list_size(self):
        ticket_response = api_requests.get_page_of_tickets(1)
        data = ticket_response['tickets']
        self.assertEqual(len(data), 25)

if __name__ == '__main__':
    unittest.main()
