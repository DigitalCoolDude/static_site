import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    solution_list = []
    for node in old_nodes:
        node_text = node.text
        text_list = node_text.split(delimiter)
        delimiter_1st = node_text.find(delimiter)
        delimiter_last = node_text.rfind(delimiter)
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
        if delimiter_last == len(node_text) - 1:
            solution_list.remove(TextNode('', TextType.TEXT))

    return solution_list

# def extract_markdown_link(text):
#     return re.findall(r"[^\!]\[(\w+(?:\s\w+)*)\]\((https:/(?:/(?:\w*@*\w*)(?:\.\w*)*)*)\)", text)

# def split_nodes_link(nodes):
#     return split_nodes_url(nodes, TextType.LINK)

# def extract_markdown_image(text):
#     return re.findall(r"\!\[(\w+(?:\s\w+)*)\]\((https:/(?:/(?:\w*@*\w*)(?:\.\w*)*)*)\)", text)

# def split_nodes_image(nodes):
#     return split_nodes_url(nodes, TextType.IMAGE)

# def split_nodes_url(nodes, texttype):
#     solution_list = []
#     for node in nodes:   
#         match texttype:
#             case TextType.LINK:
#                 urls = extract_markdown_link(node.text)
#                 diff = -1
#             case TextType.IMAGE:
#                 urls = extract_markdown_image(node.text)
#                 diff = -2
#         if len(urls) > 0:
#             curser = 0 
# #            for url in urls:
#             loc_url = node.text.find(urls[0][0])
#             solution_list.append(TextNode(node.text[0:loc_url+diff], TextType.TEXT))
#             solution_list.append(TextNode(urls[0][0], texttype, urls[0][1]))
#             solution_list.append(TextNode(node.text[loc_url+len(urls[0][0])+2+len(urls[0][1])+1:], TextType.TEXT))
#         else:
#             solution_list.append(node)
#     return solution_list

# def text_to_textnodes(text):
#     nodes = [TextNode(text, TextType.TEXT)]
#     type_list = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]
#     for tup in type_list:
#         nodes = split_nodes_delimiter(nodes, tup[0], tup[1])
#     nodes = split_nodes_image(nodes)
#  #   nodes = split_nodes_link(nodes)
#     return nodes