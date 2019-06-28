import unittest
from .input_gen import rString
from ..main.token import Token

class TestToken(unittest.TestCase):
    def test_init(self):
        type_string, value_string = rString(10), rString(10)
        test_token = Token(type_string, value_string)
        # Tests
        self.assertEqual(test_token, Token(type_string, value_string))
        self.assertNotEqual(test_token, None)
        self.assertEqual(type(test_token), type(Token("type", "value")))

    def test_type(self):
        type_string = rString(10)
        test_token = Token(type_string, "value")
        # Tests
        self.assertEqual(test_token.type, type_string)
        self.assertNotEqual(test_token.type, None)
        self.assertEqual(type(test_token.type), type(type_string))

    def test_value(self):
        value_string = rString(10)
        test_token = Token("type", value_string)
        # Tests
        self.assertEqual(test_token.value, value_string)
        self.assertNotEqual(test_token.value, None)
        self.assertEqual(type(test_token.value), type(value_string))

    def test_equal(self):
        type_string, value_string, string2 = rString(10), rString(10), rString(10)
        test_token = Token(type_string, value_string)
        test_token_clone = Token(type_string, value_string)
        test_token2 = Token(string2, value_string)
        test_token3 = Token(type_string, string2)
        # Tests
        self.assertEqual(test_token == Token(type_string, value_string), True)
        self.assertEqual(test_token == test_token_clone, True)
        self.assertNotEqual(test_token == None, True)
        self.assertNotEqual(test_token == test_token2, True)
        self.assertNotEqual(test_token == test_token3, True)
        self.assertNotEqual(test_token2 == test_token3, True)

    def test_string(self):
        type_string, value_string = rString(10), rString(10)
        test_token = Token(type_string, value_string)
        # Tests
        self.assertEqual(str(test_token), "Token({type}, {value})".format(
            type = type_string,
            value = value_string
        ))
        self.assertNotEqual(str(test_token), None)
        self.assertNotEqual(str(test_token), "Token(, )")

    def test_copy(self):
        type_string, value_string, string2 = rString(10), rString(10), rString(10)
        test_token = Token(type_string, value_string)
        test_token2 = Token(type_string, string2)
        # Tests
        self.assertEqual(test_token, test_token.copy(None))
        self.assertEqual(test_token, test_token2.copy(value_string))
        self.assertEqual(test_token2, test_token.copy(string2))
        self.assertNotEqual(test_token, test_token2.copy(None))