numbers = [12,3,4,10]
print(numbers)
if len(numbers)==0:
    print(numbers)
else:
    numbers.insert(0,numbers[-1])
    numbers.pop()
    print(numbers)