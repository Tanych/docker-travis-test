
import unittest
from helloworld import HelloTravic


class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = HelloTravic()
        self.assertEqual(greeter.message, 'Hello Travis!')

if __name__ == '__main__':
    unittest.main()
