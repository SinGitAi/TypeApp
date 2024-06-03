import random

with open('/Users/daniilnovoselcev/Downloads/russian-words-master/russian.utf-8', 'r', encoding='utf-8') as file:
    words = file.readlines()

words = [word.strip() for word in words]

random.shuffle(words)

with open('/Users/daniilnovoselcev/Downloads/russian-words-master/shuffle_words.txt', 'w', encoding='utf-8') as file:
    for word in words:
        file.write(word + '\n')
