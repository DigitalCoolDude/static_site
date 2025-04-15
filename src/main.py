from textnode import TextNode, TextType

def main():
   ex = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
   print(ex)

main()