# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True
import string
import keyword
row = str(input("Enter a name: "))
count = 0
if row[0].isnumeric():
    count+=1

for upper in range(len(row)):
    if row[upper].isupper():
        count+=1

for punc in row:
    if punc in string.punctuation:
        if punc == "_":
            continue
        count+=1

if row.find("__")!=-1:
    count+=1

for space in range(len(row)):
    if row[space]== " ":
        count+=1

if row in keyword.kwlist:
    count+=1

if count > 0:
    print("False")
else:
    print("True")

