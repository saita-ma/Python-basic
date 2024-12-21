while True:
    first_number = int(input("First number "))
    second_number = int(input("Second number "))
    math_operation = int(input("1. Math operation '+'\n2. Math operation '-'\n3. Math operation '*'\n4. Math operation '/'\n"))

    match math_operation:
        case 1:
            print(first_number + second_number)
        case 2:
            print(first_number - second_number)
        case 3:
            print(first_number * second_number)
        case 4:
            if second_number == 0:
                print("The divisor cannot be zero")
            else:
                print(first_number / second_number)
        case _:
            print("Invalid math operation please try again")
    next_math = input("\nDo you want to continue?\nY for 'Yes'\n")
    if next_math.lower() == "y":
        continue
    else:
        break