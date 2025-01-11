def first_word(text):
    import string
    repl_char = " "
    for chr in string.punctuation:
        if chr == "'":
            continue
        text = text.replace(chr, repl_char)
    text = text.strip()
    first = text.split()
    return first[0]


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
