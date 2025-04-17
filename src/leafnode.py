from enum import Enum
from htmlnode import HTMLNode

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "Code text"
    LINK = "Link"
    IMAGE = "Image"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f'{self.value}'
        html_props = self.props_to_html()
        return f'<{self.tag}{html_props}>{self.value}</{self.tag}>'


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"