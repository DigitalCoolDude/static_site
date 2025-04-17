import unittest

from leafnode import LeafNode 


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node, '<a href="https://www.google.com">Click me!</a>')
 
    def test_leaf_to_html_text(self):
        node = LeafNode(None, "This is a paragraph of text.").to_html()
        self.assertEqual(node, 'This is a paragraph of text.')

if __name__ == "__main__":
    unittest.main()