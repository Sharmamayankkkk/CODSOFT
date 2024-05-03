#python 3.7.1
"""Design a simple calculator with basic arithmetic
operations. Prompt the user to input two numbers
and an operation choice. Perform the calculation 
and display the result."""

#Arithmetic operators in Python
#1. Addition Example: a + b
#2. Subtraction  Example: a - b
#3. Multiplication Example: a * b
#4. Division Example: a / b
#5. Floor Division i.e. Divides and returns the quotient as an integer (floor value). Example: a//b
#6. Modulus i.e Divides and returns the remainder of the division. Example: a%b
#7. Exponentiation Example: a**b

print("CALCULATOR")
operations = int(input("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Floor Division \n6. Modulus \n7. Exponentiation \nSelect one of the option (0 - 7): "))

if (operations == 1):
  numberOne = int(input("Enter the First Number: "))
  numberTwo = int(input("Enter the Second Number: "))
  add = numberOne + numberTwo
  print("Addition of", numberOne, "and", numberTwo, "=", add)

elif (operations == 2):
  numberOne = int(input("Enter the First Number: "))
  numberTwo = int(input("Enter the Second Number: "))
  sub = numberOne - numberTwo
  print("Subtracting", numberOne, "from", numberTwo, "=", sub)
  
elif (operations == 3):
  numberOne = int(input("Enter the First Number: "))
  numberTwo = int(input("Enter the Second Number: "))
  multi = numberOne * numberTwo
  print("Multiplication of", numberOne, "and", numberTwo, "=", multi)
  
elif (operations == 4):
  numberOne = int(input("Enter the Numerator: "))
  numberTwo = int(input("Enter the Denominator: "))
  if (numberOne == 0):
    print("When 0 is divided by any non-zero number, the result is always 0.")
  elif (numberTwo == 0):
    print ("undefined")
  else:     
    division = numberOne / numberTwo
    print("Dividing", numberOne, "from", numberTwo, "=", division)

elif (operations == 5):
  numberOne = int(input("Enter the Numerator: "))
  numberTwo = int(input("Enter the Denominator: "))
  fdiv = numberOne // numberTwo
  print("Dividing", numberOne, "from", numberTwo, "gives quotient =", fdiv) 

elif (operations == 6):
  numberOne = int(input("Enter the Numerator: "))
  numberTwo = int(input("Enter the Denominator: "))
  rem = numberOne % numberTwo
  print("Dividing", numberOne, "from", numberTwo, "gives remainder =", rem) 

elif (operations == 7):
  base = int(input("Enter the Base Number: "))
  exponent = int(input("Enter the Exponent Number: "))
  result = base**exponent
  print(base, "to the power of",exponent,"=",result)

else:
  print("Wrong Operation Selected\nPlease Select an option between 1 - 7")
