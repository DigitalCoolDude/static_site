from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "Code text"
    LINK = "Link"
    IMAGE = "Image"
    
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise

    def props_to_html(self):
        if self.props == None:
            return ""
        text = ""
        for key, value in self.props.items():
            text += f' {key}="{value}"'
        return text


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"