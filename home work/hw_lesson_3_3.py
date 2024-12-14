numbers = [1,2,3,4,5,6]
print(numbers)
if len(numbers)==0:
    print(numbers,numbers)
elif len(numbers)%2==1:
    print(numbers[:(len(numbers)//2+1)],numbers[(len(numbers)//2)+1:])
else:
    print(numbers[:len(numbers)//2],numbers[len(numbers)//2:])





