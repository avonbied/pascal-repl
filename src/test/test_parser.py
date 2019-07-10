import unittest
from .input_gen import rString
from ..core.lexer import Lexer
from ..core.parser import Parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.test_buffer = Lexer(rString(10)).buffer
        self.test_parser = Parser(self.test_buffer)