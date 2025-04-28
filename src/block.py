import re
from enum import Enum
from text_functions import text_to_textnodes
from parentnode import ParentNode
from textnode import TextNode, TextType
from leafnode import LeafNode

class BlockType(Enum):
    HEADING = r"^#{1,6}\s+(.+)$"
    CODE = r"```(?:[\s\S]*?)```"
    QUOTE = r"(^|\n)>[^\n]*(\n>[^\n]*)*"
    UNORDERED_LIST = r"(^|\n)-\s+[^\n]*(\n-\s+[^\n]*)*"
    ORDERED_LIST = r"(^|\n)\d+\.\s.+[^\n]*(\n\d+\.\s.+[^\n]*)*"
    PARAGRAPH = f'(?!{HEADING}|{CODE}|{QUOTE}|{UNORDERED_LIST}|{ORDERED_LIST})'


def markdown_to_blocks(md):
    md_list = md.split('\n\n')
    md_new = []
    for block in md_list:
        md_new.append(re.sub(r'[ ]{4}','', block.strip()))
    return md_new

def block_to_block_type(block):
    for enum in BlockType:
        if re.findall(enum.value, block) != []:
            return enum
        
def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    child_nodes = []
    for block in blocks:
        if block == '':
            continue
        blocktype = block_to_block_type(block)
        match blocktype:
            case BlockType.HEADING:
                child_nodes.append(
                    ParentNode(f"h{block.find(" ")}", 
                        [TextNode(block.replace("#", "").strip(), TextType.TEXT).text_node_to_html_node()])
                )
            case BlockType.CODE:
                child_nodes.append(
                    ParentNode("pre", 
                        [TextNode(block.replace("```", ""), TextType.CODE).text_node_to_html_node()])
                )
            case BlockType.QUOTE:
                textnodes = text_to_textnodes(block.replace(">", ""))
                grandchild_nodes = []
                for node in textnodes:
                    grandchild_nodes.append(node.text_node_to_html_node())
                child_nodes.append(ParentNode("blockquote", grandchild_nodes))
            case BlockType.UNORDERED_LIST:
                text_list = block.split("- ")
                grandchild_nodes = []
                for text in text_list:
                    if text == "":
                        continue
                    textnodes = text_to_textnodes(text)                
                    ggchild_nodes = []
                    for node in textnodes:
                        ggchild_nodes.append(node.text_node_to_html_node())
                    grandchild_nodes.append(ParentNode("li", ggchild_nodes))
                child_nodes.append(ParentNode("ul", grandchild_nodes))
            case BlockType.ORDERED_LIST:
                text_list = re.split(r'\d+\.\s', block)
                grandchild_nodes = []
                for text in text_list:
                    if text == "":
                        continue
                    textnodes = text_to_textnodes(text)                
                    ggchild_nodes = []
                    for node in textnodes:
                        ggchild_nodes.append(node.text_node_to_html_node())
                    grandchild_nodes.append(ParentNode("li", ggchild_nodes))
                child_nodes.append(ParentNode("ol", grandchild_nodes))             
            case _:
                textnodes = text_to_textnodes(block.replace("\n", " "))
                grandchild_nodes = []
                for node in textnodes:
                    grandchild_nodes.append(node.text_node_to_html_node())
                child_nodes.append(ParentNode("p", grandchild_nodes))
        

               
    
    return ParentNode("div", child_nodes)
