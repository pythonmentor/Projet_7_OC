""" app.parser.Parser test """

# -*- coding: utf-8 -*-
from app import parser

class TestParser:

    def test_transform_to_lowercase(self):
        ab = parser.Parser_Question("TEST")
        assert ab.transform_to_lowercase() == "test"
        
    def test_delete_spaces(self):
        ab = parser.Parser_Question("   bla bla   ")
        assert ab.delete_spaces("   bla bla   ") == "bla bla"