# Introduction to Python Programming

'''
Problem : Ask user to enter two numbers and then print the addition of those numbers.

pseudo-code

0. create two variable -- num1 and num2
1. Ask user to input numbers
2. store input into variable
3. calcuate sum of variables
4. print sum
'''

num1 = 0 # first variable with a default value of zero
num2 = 0 # second variable with a default value of zero
result = 0

num1 = int(input("Enter First Number: ")) # taking input of first variable
opp = input("Choose an operation --> + - * / : ")
num2 = int(input("Enter Second Number: ")) # taking input of second varable

if(opp == '+' ):
    result =  num1+num2
elif(opp == '-'):
    result = num1-num2
elif(opp == '*'):
    result = num1*num2
elif(opp == '/'):
    result = num1/num2
else:
    print("Wrong Input!!!")

# = assignment operator
# == is comparison operator


    
print("The result is of Two Numbers is ", result)

#sum = num1 + num2 # converting the type of varaible and them adding them

# Airthemic Operators
# +, -, *, /, %

#print("The result is  of Two Numbers is ", sum) # printing the sum of variables -- 1
#print("The Sum of Two Numbers is %d" %sum) # printing in a different way -- 2
#print("%d + %d = %d " %(num1, num2, sum)) # --3
#print(f"{num1} + {num2} = {sum}") #-- 4










