import random


words_new = []
with open('/Users/daniilnovoselcev/Downloads/words_chastot.utf-8', 'r', encoding="utf-8") as file:
    words = file.readlines()
    for word in words:
        word_new = word.split()
        words_new.append(word_new[2])

random.shuffle(words_new)
with open('/Users/daniilnovoselcev/Downloads/chastot_shuffle.txt', 'w', encoding='utf-8') as file:
    for word in words_new:
        file.write(word + '\n')


