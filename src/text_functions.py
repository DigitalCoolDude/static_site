import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for node in old_nodes:
        solution_list = []
        text_list = node.text.rsplit(delimiter)
        solution_list.append(TextNode(text_list[0], TextType.TEXT))
        solution_list.append(TextNode(text_list[1], text_type))
        solution_list.append(TextNode(text_list[2], TextType.TEXT))
    return solution_list

def extract_markdown_urls(text):
    return re.findall(r"\[(\w+(?:\s\w+)*)\]\((https:/(?:/(?:\w*@*\w*)(?:\.\w*)*)*)\)", text)