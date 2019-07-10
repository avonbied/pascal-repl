import unittest
from .input_gen import rString
from ..core.lexer import Lexer

class TestLexer(unittest.TestCase):

    def setUp(self):
        self.test_string = rString(10)
        self.test_lexer, self.test_lexer2 = Lexer(self.test_string), Lexer(rString(10))

    def test_init(self):
        self.assertEqual(self.test_lexer, Lexer(self.test_string))
        self.assertNotEqual(self.test_lexer, None)
        self.assertNotEqual(self.test_lexer, self.test_lexer2)

    def test_error(self):
        self.assertRaises(Exception, self.test_lexer.error)

    def test_symbolSeq(self):
        self.assertEqual(self.test_lexer.symbolSeq, Lexer(self.test_string).symbolSeq)
        self.assertEqual(self.test_lexer.symbolSeq, self.test_string)
        self.assertEqual(type(self.test_lexer.symbolSeq), type("string"))
        self.assertNotEqual(self.test_lexer.symbolSeq, None)
        self.assertNotEqual(self.test_lexer.symbolSeq, "")
    
    def test_buffer(self):
        self.assertEqual(self.test_lexer.buffer, Lexer(self.test_string).buffer)

    def test_eq(self):
        self.assertEqual(self.test_lexer, Lexer(self.test_string))
        self.assertNotEqual(self.test_lexer, None)
        self.assertNotEqual(self.test_lexer, Lexer(""))

    def test_sizeof(self):
        self.assertEqual(len(self.test_lexer), len(self.test_lexer.buffer))
        self.assertEqual(type(len(self.test_lexer)), type(0))