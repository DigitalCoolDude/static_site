from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"
    
class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        # if text_type != TextType:
        #     raise
        self.text_type = text_type
        self.url = url

    def text_node_to_html_node(self):
        prop = None
        if self.text_type == TextType.LINK:
            prop = {"href": self.url}
        if self.text_type == TextType.IMAGE:
            prop_text = self.text
            prop = {
                "src": self.url,
                "alt": prop_text
            }
            self.text = None
        return LeafNode(self.text_type.value, self.text, prop)

    def __eq__(self, other):
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"