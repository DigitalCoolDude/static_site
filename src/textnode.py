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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for node in old_nodes:
        solution_list = []
        text_list = node.text.rsplit(delimiter)
        solution_list.append(TextNode(text_list[0], TextType.TEXT))
        solution_list.append(TextNode(text_list[1], text_type))
        solution_list.append(TextNode(text_list[2], TextType.TEXT))
    return solution_list       
