import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
          html = file.read()
          cleantext = re.sub(r'<[^>]+>', "", html)
          with open(result_file, 'w+', encoding='utf-8') as res_file:
            res_file.write(cleantext)
            res_file.seek(0)
            for line in res_file:
                 if line.strip():
                    line = re.sub(' +', ' ', line)
                    res_file.write(line)
            




delete_html_tags("draft.html")
