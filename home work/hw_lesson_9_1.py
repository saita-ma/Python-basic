def popular_words (text, words):
    import string
    text_low = " " + text.lower() + " "
    repl_char = " "
    for chr in string.punctuation:
        text_low = text_low.replace(chr, repl_char)
    new_words = map(lambda x: " " + x + " ", words)
    count = map(lambda x: text_low.count(x), new_words)
    zipped_data = zip(words, count)
    result = dict(zipped_data)
    return result


# print(popular_words('''When I! was One I had just begun When I was Two I was, nearly new ''', ['i', 'was', 'three', 'near']))

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

################
'''
Чтобы найти корректное количество 'near' используя материал, который мы приходили использовал костыли с добавлением пробелов
к словам в words функции popular_words
Также если бы искомые слова были бы в начале или в конце предложения добавил к нему пробелы и заменил знаки пунктуации на пробелы
Правильнее было бы наверное использовать регулярные выражения RegEx, но мы их не проходили, придумывал велосипед
'''