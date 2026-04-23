try:
    a = int(input())
    b = int(input())
    print(a + b)
except:
    exit()

    # ----- Extra calculator features -----

try:
    print("\nCalculator options:")
    print("1 - Subtract two numbers")
    print("2 - Multiply two numbers")
    print("3 - Divide two numbers")
    print("4 - Modulus of two numbers")
    print("5 - Add three numbers")
    print("6 - Evaluate expression (example: 2 + 4 - 3)")

    option = input("Choose an option: ")

    if option == "1":
        x = float(input("First number: "))
        y = float(input("Second number: "))
        print("Result:", x - y)

    elif option == "2":
        x = float(input("First number: "))
        y = float(input("Second number: "))
        print("Result:", x * y)

    elif option == "3":
        x = float(input("First number: "))
        y = float(input("Second number: "))
        if y != 0:
            print("Result:", x / y)
        else:
            print("Error: division by zero")

    elif option == "4":
        x = float(input("First number: "))
        y = float(input("Second number: "))
        print("Result:", x % y)

    elif option == "5":
        x = float(input("First number: "))
        y = float(input("Second number: "))
        z = float(input("Third number: "))
        print("Result:", x + y + z)

    elif option == "6":
        expression = input("Enter expression: ")
        print("Result:", eval(expression))

except:
    pass