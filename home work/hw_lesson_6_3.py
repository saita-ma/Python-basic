# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1
number = input("Enter the number: ")
while True:
    multi = 1
    for i in range(0,len(number)):
        multi *= int(number[i])

    if multi > 9:
        number = str(multi)

    else:
        print(multi)
        break