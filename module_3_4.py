def single_root_words(root_word, *other_words):
    same_words = []
    for i_word in other_words:
        if root_word.lower() in i_word.lower() or i_word.lower() in root_word.lower():
            same_words.append(i_word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('Лен', 'поленивавшийся', 'Лень', 'ПОЛЕНО', 'СУЧЕК', 'лиса', 'len', 'Полдень', 'разленивающийся')
print(result1)
print(result2)
print(result3)
