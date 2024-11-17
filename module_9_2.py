first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(str_) for str_ in first_strings if len(str_) >= 5]
second_result = [(w1, w2) for w1 in first_strings for w2 in second_strings if len(w1) == len(w2)]
third_result = {str_all: len(str_all) for str_all in first_strings + second_strings if not len(str_all) % 2 }

print(first_result)
print(second_result)
print(third_result)