dividend =input("Number to be divided?  ")
divisor = input("The number that will divide?  ")

if divisor > dividend[0]:
    modify1 = dividend[:]
    quotient1 =  int( modify1) // int(divisor)
    remainder1= int(modify1) % int(divisor)
    print(f"The result of dividing: " + str(dividend) +" " + "by" + " " +str(divisor) + " " + "is" + " "+ str(quotient1) + ", "+ "and the remainder is " +" " + str(remainder1) )
    
elif divisor <= dividend :
   
    modify2 = dividend[:]
    quotient2 = int(modify2) // int(divisor)
    remainder2 = int(modify2) % int(divisor)
