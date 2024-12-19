# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]
import random
NUMS_SIZE = random.randint(3, 10)
numbers = []
for i in range(NUMS_SIZE):
    numbers.append(random.randint(1, 10))
print(numbers)
numbers2 = [numbers[0],numbers[2],numbers[-2]]
print(numbers2)