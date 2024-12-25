# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59
number = int(input("Enter seconds from '0' to '864000': "))
days = number // (24*60*60)
hours = (number-days*(24*60*60)) // (60*60)
minutes = (number-days*(24*60*60)-hours*(60*60)) // 60
seconds = (number-days*(24*60*60)-hours*(60*60)) % 60
h = str(hours).zfill(2)
m = str(minutes).zfill(2)
s = str(seconds).zfill(2)
if days % 10 == 1 and days != 11:
    day = "день,"
elif days % 10 in [2,3,4] and days not in [12,13,14]:
    day = "дні,"
else:
    day = "днів,"
print(f"{days} {day} {h}:{m}:{s}")
