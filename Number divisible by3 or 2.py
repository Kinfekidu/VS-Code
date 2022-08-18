#Enter two integers: 15, 30
#Divisible By 2 Or 3(15, 30) → 450
#Enter two integers: 2, 90
#Divisible By 2 Or 3(2, 90) → 180
#Enter two integers: 7, 12
#Divisible By 2 Or 3(7, 12) → 19



num1 = int(input("integer"))
num2 = int(input("integer"))



if(num1 % 2 == 0 or num1 % 3 == 0 and num2 % 2 == 0 or num2 % 3 == 0):
    result = num1*num2

else:
    result= num1+num2
print(result)


