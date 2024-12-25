# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA
import string

while True:
    letters = input("Input your letters using '-' between them: ")
    if len(letters) == 3:
        first_letter = string.ascii_letters.find(letters[0])
        second_letter = string.ascii_letters.find(letters[2])
        if letters[0] in string.ascii_letters and letters[2] in string.ascii_letters:
            if first_letter > second_letter:
                print("Your letters should be in alphabetical order from 'a' to 'Z':  ")
            else:
                print(string.ascii_letters[first_letter:second_letter+1])
                break
        else:
            print("Your two letters must be in range from 'a' to 'Z'")
    else:
        print("You need to input two letters")