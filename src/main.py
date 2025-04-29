import os, re, shutil, sys
from block import markdown_to_html_node

def main():
   dest_dir_path = "docs"
   copy(dest_dir_path)
   basepath = sys.argv
   generate_pages_recursive(basepath, "content", "template.html", dest_dir_path)

def copy(dest_dir_path):
   if os.path.exists(dest_dir_path):
      shutil.rmtree(dest_dir_path)

   dir_list = [("static", dest_dir_path)]
   
   for s_item, p_item in dir_list:
      if os.path.isfile(s_item):
         shutil.copy(s_item, p_item)
      else:
         os.mkdir(p_item)
         for sub in os.listdir(s_item):
            dir_list.append((os.path.join(s_item, sub), os.path.join(p_item, sub)))

def extract_title(md):
   if md.read(1).strip() != "#":
      raise
   return md.readline().strip()

def generate_page(basepath, from_path, template_path, dest_path):
   print(f"Generation page from {from_path} to {dest_path} using {template_path}.")
   
   with open(from_path, "r") as content:
      new_title = extract_title(content)
      content.seek(0)
      body = markdown_to_html_node(content.read()).to_html()
   
   with open(template_path, "r") as temp:
      file_string = temp.read()
      updated1 = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', file_string)
      updated2 = re.sub(r'<article>.*?</article>', f'<article>{body}</article>', updated1)
      updated3 = re.sub(r'herf="/', f'href="{basepath}', updated2)
      updated4 = re.sub(r'src="/', f'src="{basepath}', updated3)

   with open(dest_path, 'w') as new:
      new.write(updated4)

def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
   md_list = []

   dir_list = [(dir_path_content, dest_dir_path)]
   
   for s_item, p_item in dir_list:
      if os.path.isfile(s_item):
         md_list.append((s_item, p_item.replace("md", "html")))
      else:
         if p_item != dest_dir_path:
            os.mkdir(p_item)
         for sub in os.listdir(s_item):
            dir_list.append((os.path.join(s_item, sub), os.path.join(p_item, sub)))

   for (md, dest) in md_list:
      generate_page(basepath, md, template_path, dest)


main()