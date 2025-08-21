#Addition
def add(a, b):
    return a+b
#Subtraction
def subtract(a, b):
    return a-b
#Division
def divide(a, b):
    return a / b
#Multiplication
def multiply(a, b):
    return a * b
#Main calculator function
import time
def calculator():
    while True:
        try:
            print("####### Calculator CLI #######")
            print("Select your Operation:")
            print("1. Addition")
            print("2. Substract")
            print("3. Divide")
            print("4. Multiply")
            print("Q. Quit")
            print("##############################")
            operation = input("Enter your option: ")

            if operation in ['1', '2', '3', '4']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operation == '1':
                    print(f"The result of addition is: {add(num1, num2)}")
                elif operation == '2':
                    print(f"The result of subtraction is: {subtract(num1, num2)}")
                elif operation == '3':
                    print(f"The result of division is: {divide(num1, num2)}")
                elif operation == '4':
                    print(f"The result of multiplication is: {multiply(num1, num2)}")
            elif operation.lower() == 'q':
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Invalid operation. Please try again.")
        
        except Exception as e:
            print("An error occurred: ", e)
    
        # Create new empty line for better readability
        print("##############################")
        print("\n")
        # Pause for awhile before menu appears up again
        time.sleep(2)

#Run calculator function if called
if __name__ == "__main__":
    calculator()