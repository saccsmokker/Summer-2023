def main():
    print ("Welcome to the Fahrenheit to Celsius converter ")
    #get user input for degrees F
    x = eval (input (" PLease enter the degrees in Fahrenheit that you would like to convert to Celsius: "))
    #extra variables for conversion
    y = 32
    z = 5/9
    #Formula
    sum = (x - y) * z
    #print out the results
    print("Degrees in Celsius is:",sum)
    
main()