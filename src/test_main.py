import unittest

from main import *
from textnode import TextNode, TextType


# class TestCopy(unittest.TestCase):
#     copy()


# class TestExtractTitle(unittest.TestCase):
#     def gerenal_case(self):
#         extract_title()


# class TestGeneratePage(unittest.TestCase):
#     def gerenal_case(self):
#         generate_page()


class TestGeneratePagesRecursive(unittest.TestCase):

    def test_gerenal_case(self):
        generate_pages_recursive("content", "template.html", "public/index.html")
        self.assertFalse(False)
        