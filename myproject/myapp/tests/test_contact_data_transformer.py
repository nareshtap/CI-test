from django.test import TestCase

def multiply(a, b):
    return a * b

class ContactDataTransformerTest(TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6) ## abcdefgh1234
