first_num = int (input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
oppration = input("Choose the operation (+, -, *, /): ")
match oppration:
    case "+":
        print(f"The result is {first_num + second_num}")
    case "-":
        print(f"The result is {first_num - second_num}")
    case "*":
        print(f"The result is {first_num * second_num}")
    case "/":
        if second_num != 0:
            print(f"The result is {first_num / second_num}")
        else:
            print("Cannot divide by zero")

