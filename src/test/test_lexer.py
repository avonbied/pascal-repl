import unittest
from .input_gen import rString
from ..main.lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_init(self):
        test_string, test_string2 = rString(10), rString(10)
        self.assertEqual(Lexer(test_string), Lexer(test_string))
        self.assertNotEqual(Lexer(test_string), None)
        self.assertNotEqual(Lexer(test_string), Lexer(test_string2))

    def test_error(self):
        test_lexer = Lexer(rString(10))
        self.assertRaises(Exception, test_lexer.error)

    def test_symbolSeq(self):
        test_string = rString(10)
        test_lexer = Lexer(test_string)
        # Tests
        self.assertEqual(test_lexer.symbolSeq, Lexer(test_string).symbolSeq)
        self.assertEqual(test_lexer.symbolSeq, test_string)
        self.assertEqual(type(test_lexer.symbolSeq), type(test_string))
        self.assertNotEqual(test_lexer.symbolSeq, None)
        self.assertNotEqual(test_lexer.symbolSeq, "symbolSeq")

    def test_eq(self):
        test_string = rString(10)
        test_lexer = Lexer(test_string)
        self.assertEqual(test_lexer, Lexer(test_string))
        self.assertNotEqual(test_lexer, None)
        self.assertNotEqual(test_lexer, Lexer("symbolSeq"))