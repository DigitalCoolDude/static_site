import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    solution_list = []
    for node in old_nodes:
        n_text = node.text
        text_list = n_text.split(delimiter)
        delimiter_1st = n_text.find(delimiter)
        delimiter_last = n_text.rfind(delimiter)
        if len(text_list) % 2 == 0:
            raise
        if delimiter_1st == -1:
            solution_list.append(node)
            continue  
        for i, text in enumerate(text_list):
            if i % 2 == 0:
                solution_list.append(TextNode(text, TextType.TEXT))
            else:
                solution_list.append(TextNode(text, text_type))
        if delimiter_1st == 0:
            solution_list.remove(TextNode('', TextType.TEXT))
        if delimiter_last == len(n_text) - 1:
            solution_list.remove(TextNode('', TextType.TEXT))
    return solution_list

def extract_markdown_link(text):
    return re.findall(r"(?<!\!)\[([\w|\"|<|\.]+(?:\s[\w|\"]+)*)\]\(((?:https:/){0,1}(?:/(?:[\w|\-]*@*\w*)(?:\.\w*)*)*)\)", text)

def split_nodes_link(nodes):
    return split_nodes_url(nodes, TextType.LINK)

def extract_markdown_image(text):
    return re.findall(r"\!\[(\w+(?:\s\w+)*)\]\(((?:https:/){0,1}(?:/(?:\w*@*\w*)(?:\.\w*)*)*)\)", text)

def split_nodes_image(nodes):
    return split_nodes_url(nodes,TextType.IMAGE)

def split_nodes_url(nodes, texttype):
    solution_list = []
    for node in nodes:
        n_text = node.text   
        match texttype:
            case TextType.LINK:
                urls = extract_markdown_link(n_text)
                diff = -1
            case TextType.IMAGE:
                urls = extract_markdown_image(n_text)
                diff = -2
        if len(urls) > 0:
            curser = 0 
            for url in urls:
                loc_url = n_text.find(url[0])
                solution_list.append(TextNode(node.text[curser:loc_url+diff], TextType.TEXT))
                solution_list.append(TextNode(url[0], texttype, url[1]))
                curser = loc_url+len(url[0])+2+len(url[1])+1
            if curser != len(n_text):
                solution_list.append(TextNode(node.text[curser:], TextType.TEXT))
        else:
            solution_list.append(node)
    return solution_list

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    type_list = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]
    for tup in type_list:
        nodes = split_nodes_delimiter(nodes, tup[0], tup[1])
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    for node in nodes:
        if node == TextNode('', TextType.TEXT):
            nodes.remove(TextNode('', TextType.TEXT))
    return nodes