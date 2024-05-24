while True:
    try:
        # Asking user to enter three numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        # Check if all three numbers are positive
        if num1 > 0 and num2 > 0 and num3 > 0:
            total_sum = num1 + num2 + num3
            print(f"The sum of the numbers is: {total_sum}")
        else:
            print("Only positive numbers are accepted.")
        
        # Asking user if they want to perform the operation again
        repeat = input("Do you want to perform the operation again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Terminating the program.")
            break
            
    except ValueError:
        print("Invalid input. Please enter numerical values.")
