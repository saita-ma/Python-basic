# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
import string
row = input("Enter a hashtag: ")
row1 = row.title()
result = []
for punc in range(len(row1)):
    if row1[punc] not in string.punctuation and not row1[punc] == " ":
        result.append(row1[punc])
print("#"+"".join(result[:139])) # первый символ hashtag + 139 символов из рядка