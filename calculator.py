def calculator():
    print("Welcome to the Python Calculator!")
    print("You can perform operations like addition (+), subtraction (-), multiplication (*), division (/), or any valid expression.")
    print("Type 'exit' to quit the calculator.")

    while True:
        expression = input("\nEnter your expression: ")
        
        if expression.lower() == "exit":
            print("Exiting the calculator. Goodbye!")
            break

        try:
            # Evaluate the mathematical expression
            result = eval(expression)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"Error: Invalid expression. Please try again. ({e})")

# Run the calculator
calculator()
