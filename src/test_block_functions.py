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

    def test_quote(self):
        blocktype = block_to_block_type("> This is a list\n\n-- t.t.")
        self.assertEqual(blocktype, BlockType.QUOTE)
    
    def test_heading(self):
        blocktype = block_to_block_type("# This is a Heading")
        self.assertEqual(blocktype, BlockType.HEADING)


class TestMarkdown2HTMLNodeFunction(unittest.TestCase):

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
    > "This is a quote."
    >
    > -- B.N.M
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote><p>"I am in fact a Hobbit in all but size."</p><p></p><p>-- J.R.R. Tolkien</p></blockquote></div>',
        )