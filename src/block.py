from enum import Enum
import re

class BlockType(Enum):
    HEADING = r"^(#{1,6})\s+(.+)$}"
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