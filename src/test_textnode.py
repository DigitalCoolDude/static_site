import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_1st_comparsion(self):
        node = TextNode("text node This is", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_2nd_comparsion(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_3rd_comparsion(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.bt.dev")
        self.assertNotEqual(node, node2)

    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")    
 
    def test_text_link(self):
        node = TextNode("Click me!", TextType.LINK, "https://www.boot.dev")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, 'Click me!')    
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_text_image(self):
        node = TextNode("Click me!", TextType.IMAGE, "https://www.boot.dev")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, 'Click me!')    
        self.assertEqual(html_node.props, {"alt": 'Click me!', "src": "https://www.boot.dev"})     

if __name__ == "__main__":
    unittest.main()