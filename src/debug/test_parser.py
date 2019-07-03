import unittest
from .input_gen import rString
from ..main.lexer import Lexer
from ..main.parser import Parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.test_buffer = Lexer(rString(10)).buffer
        self.test_parser = Parser(self.test_buffer)