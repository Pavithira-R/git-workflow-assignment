# Small calculator that takes two numbers from the user and divides them
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1/ num2
        print(f"The division of {num1} and {num2} is {result}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
if __name__ == "__main__":
    divide_numbers()   
    print("Calculation completed successfully")
