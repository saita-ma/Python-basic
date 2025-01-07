def is_palindrome(text):
    import string
    text_low = text.lower()
    result = []
    for i in range(len(text_low)):
        if text_low[i] not in string.punctuation and not text_low[i] == " ":
            result.append(text_low[i])
    return result[:] == result[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
