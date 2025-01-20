import codecs
import re
import os

def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
          html = file.read()
          cleantext = re.sub(r'<[^>]+>', "", html)
          with open('temp.txt', 'w+',encoding='utf-8') as temp_file, open(result_file, 'w', encoding='utf-8') as res_file:
            temp_file.write(cleantext)
            temp_file.seek(0)
            for line in temp_file:
                 if line.strip():
                    line = re.sub(' +', ' ', line)
                    res_file.write(line)
            temp_file.close()
            os.remove("temp.txt")



delete_html_tags("draft.html")