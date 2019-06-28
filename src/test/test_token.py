import unittest
from .input_gen import rString
from ..main.token import Token

class TestToken(unittest.TestCase):

    def setUp(self):
        self.type_string, self.value_string = rString(10), rString(10)
        self.test_token = Token(self.type_string, self.value_string)

    def test_init(self):
        self.assertEqual(self.test_token, Token(self.type_string, self.value_string))
        self.assertNotEqual(self.test_token, None)
        self.assertEqual(type(self.test_token), type(Token("type", "value")))

    def test_type(self):
        self.assertEqual(self.test_token.type, self.type_string)
        self.assertNotEqual(self.test_token.type, None)
        self.assertEqual(type(self.test_token.type), type(self.type_string))

    def test_value(self):
        self.assertEqual(self.test_token.value, self.value_string)
        self.assertNotEqual(self.test_token.value, None)
        self.assertEqual(type(self.test_token.value), type(self.value_string))

    def test_equal(self):
        self.assertEqual(self.test_token, Token(self.type_string, self.value_string))
        self.assertNotEqual(self.test_token, None)
        self.assertNotEqual(self.test_token, Token("type", self.value_string))
        self.assertNotEqual(self.test_token, Token(self.type_string, "value"))

    def test_string(self):
        self.assertEqual(str(self.test_token), "Token({type}, {value})".format(
            type = self.type_string,
            value = self.value_string
        ))
        self.assertNotEqual(str(self.test_token), None)
        self.assertNotEqual(str(self.test_token), "Token(, )")

    def test_copy(self):
        test_token2 = Token(self.type_string, "value")
        # Tests
        self.assertEqual(self.test_token, self.test_token.copy(None))
        self.assertEqual(self.test_token, test_token2.copy(self.value_string))
        self.assertEqual(test_token2, self.test_token.copy("value"))
        self.assertNotEqual(self.test_token, test_token2.copy(None))