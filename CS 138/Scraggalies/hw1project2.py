def main():
    #print("Hello")
    #print("Welcome to the simple grade calculator")
    #get user input 
    num1 = int(input("Enetr the number of correct answers: "))
    num2 = int(input("Enter the total number of questions: "))
    # do math on the user inputs
    sum = num1 / num2 * 100
    #display the grade 
    print("Your score is: " , sum , "%")

main()
