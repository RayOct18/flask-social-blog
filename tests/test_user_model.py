import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'hey')
        self.assertTrue(u.password_hash is not None)

    def test_password_getter(self):
        u = User(password = 'hey')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'hey')
        self.assertTrue(u.verify_password('hey'))
        self.assertFalse(u.verify_password('yo'))

    def test_password_salts_are_random(self):
        u = User(password = 'hey')
        u2 = User(password = 'hey')
        self.assertTrue(u.password_hash != u2.password_hash)
