""" app.parser.Parser test """

# -*- coding: utf-8 -*-
from app.parser import Parser

class TestParser():

    def test_transform_to_lowercase(self):
        a = .SentenceParse()
        b = "TEST"
        assert a.transform_to_lowercase(b) == "test"