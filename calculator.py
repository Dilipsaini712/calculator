print("*******Welcome To My Calculator*******")
while True:
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit\n")

    choice=input("Enter your choice for calculation: ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Addition of two numbers is: ", num1 + num2)
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Subtraction of two numbers is: ", num1 - num2)
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Multiplication of two numbers is: ", num1 * num2)
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("Division of two numbers is: ", num1 / num2)
        else:
            print("Error! Division by zero is not allowed")
    elif choice == '5':
        print("Thank you for using my calculator!")
        break
    
    else:
        print("Invalid choice. Please choose a valid option in 1-5!")