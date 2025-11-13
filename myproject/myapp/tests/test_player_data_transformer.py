from django.test import TestCase

def simple_add(a, b):
    return a + b

class PlayerDataTransformerTest(TestCase):
    def test_simple_add(self):
        self.assertEqual(simple_add(2, 3), 5)
