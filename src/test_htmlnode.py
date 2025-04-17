import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(None, None, None, props)
        solution = node.props_to_html()
        self.assertEqual(solution, ' href="https://www.google.com" target="_blank"')


 

if __name__ == "__main__":
    unittest.main()