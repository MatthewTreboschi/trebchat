import unittest
import unittest.mock as mock
import app

KEY_MESSAGE = 'test_message'
KEY_EXPECTED = 'expected'
KEY_USER = 'user'

class MockedQueryResponse:
    def __init__(self, username,):
        self.username = username

class appTest(unittest.TestCase):
    def setUp(self):
            self.message_sent_params = [
            {
                KEY_MESSAGE: "Hello, mattbot!",
                KEY_EXPECTED: {
                    KEY_USER: "Anonymous"
                }
            }
            #self.emit_all_params = []
            #self.connect_params ={}
            #self.new_name_params = {}
        ]
    
    def mocked_
    
    def test_message_sent(self):
        for test_case in self.message_sent_params:
            with mock.patch(
                'flask_sqlalchemy.SQLAlchemy.session.query.filter.first',
                self.mocked)
                message = test_case[KEY_MESSAGE]
        
if __name__ == '__main__':
    unittest.main()