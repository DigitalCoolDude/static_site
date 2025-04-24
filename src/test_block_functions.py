import unittest

from block import *
from textnode import TextNode, TextType

class TestMarkdown2BlocksFunction(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        )


class TestBlock2BlockTypeFunction(unittest.TestCase):
    
    def test_singleline(self):
        blocktype = block_to_block_type("This is **bolded** paragraph")
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_multiline(self):
        blocktype = block_to_block_type("This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line")
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_unordered_list(self):
        blocktype = block_to_block_type("- This is a list\n- with items")
        self.assertEqual(blocktype, BlockType.UNORDERED_LIST)