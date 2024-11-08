class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = []
        for file_name_i in file_names:
            self.file_names.append(file_name_i)

    def get_all_words(self):
        all_words = {}
        punc_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_self in self.file_names:
            with open(file_self, encoding='utf-8') as file:
                words = []
                for line in file:
                    new_line = ''
                    for char in line:
                        if char not in punc_list:
                            new_line += char.lower()
                        else:
                            new_line += ' '
                    words += new_line.split()
                all_words[file.name] = words
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            first_position = 0
            for word_ in words:
                first_position += 1
                if word_ == word.lower():
                    return {name: first_position}
        return 0

    def count(self, word):
        name_num_w = {}
        for name, words in self.get_all_words().items():
            number_w = 0
            for word_ in words:
                if word_ == word.lower():
                    number_w += 1
            if number_w != 0:
                name_num_w[name] = number_w
        return name_num_w


finder2 = WordsFinder('Mother Goose - Monday’s Child.txt', 'test_file.txt')
print(finder2.get_all_words())  # Все слова

print(finder2.find('TEXT'))
print(finder2.count('teXT'))



print(finder2.find('Child'))
print(finder2.count('Child'))


finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))