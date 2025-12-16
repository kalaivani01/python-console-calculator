def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation (1/2/3/4): ")

    numbers = input("Enter numbers separated by space: ").split()
    numbers = [float(n) for n in numbers]

    if choice == "1":          # Add
        result = sum(numbers)

    elif choice == "2":        # Subtract
        result = numbers[0]
        for n in numbers[1:]:
            result -= n

    elif choice == "3":        # Multiply
        result = 1
        for n in numbers:
            result *= n

    elif choice == "4":        # Divide
        result = numbers[0]
        for n in numbers[1:]:
            result /= n

    else:
        print("Invalid choice")
        return

    print("Result:", result)


calculator()
