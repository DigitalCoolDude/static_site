import os, shutil
from textnode import TextNode, TextType

def main():
   # ex = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
   # print(ex)
   copy()

def copy():
   if os.path.exists("public"):
      shutil.rmtree("public")

   dir_list = [("static", "public")]
   
   for s_item, p_item in dir_list:
      if os.path.isfile(s_item):
         shutil.copy(s_item, p_item)
      else:
         os.mkdir(p_item)
         for sub in os.listdir(s_item):
            dir_list.append((os.path.join(s_item, sub), os.path.join(p_item, sub)))

main()