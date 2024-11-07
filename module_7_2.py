from pprint import pprint

from encodings.utf_7 import encode


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    con = 1
    strings_positions = {}
    for str_i in strings:
        key_ = (con, file.tell())
        strings_positions[key_] = str_i
        con += 1
        file.write(str_i+"\n")
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
