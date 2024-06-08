while True:
    # 1 first number
    while True:
        try:
            first_number = float(input("Enter the first number : "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # 2 operation type
    while True:
        try:
            operation_type = input("Enter operation type (+, -, /, *): ")
            if operation_type in ("+", "-", "/", "*"):
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid operator.")

    # 3 second number
    while True:
        try:
            second_number = float(input("Enter The second number : "))
            if second_number == 0 and operation_type == "/":
                raise ZeroDivisionError
            break
        except ValueError:
            print("Please enter a numeric value.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter another number.")

    # 4 print the result
    match operation_type:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number
        case "/":
            result = first_number / second_number
        case _:
            result = None
    if result is not None:
        print("The result is:", result)
    else:
        print("Unexpected Error")
    #repeat
    while True:
        try:
            repeat = input("Do you want to repeat the operation again ? (y/n) : ")
            if repeat in ("y", "yes", "n", "no"):
                break
            else:raise ValueError
        except ValueError:
            print("please answer by Y or N ")
    if repeat in ("n","no"):
        print("program excited")
        break







