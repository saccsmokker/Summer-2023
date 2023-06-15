def main():
    print("Hello!")
    print("I can add three numbers for you")

    # Getting input from the user
    num1 = int(input("Enter one whole number (Ex. 50): "))
    num2 = int(input("Enter one whole number (Ex. 50): "))
    num3 = int(input("Enter one whole number (Ex. 50): "))

    # Performs calculations
    sum_of_numbers = num1 + num2 + num3
    product_of_numbers = num1 * num2 * num3

    # Print the results
    print("The sum of the three numbers is", sum_of_numbers)
    print("The product of the three numbers is", product_of_numbers)
main()