"""Question 03
Write a program in which take two numbers from user by using built-in function and perform folllowing
 arithmetic operation

Addition
Subtraction
Multiplication
Division"""
# def operations(num1,num2):
#     return {
#         "Addition":num1+num2,
#         "Subtraction":num1-num2,
#         "Multiplication":num1*num2,
#         "Division":num1/num2
#     }
# num1=int(input("Enter the num1:"))
# num2=int(input("Enter the num2:"))
# print("Perform the Arithmetic Operations")
# result=operations(num1,num2)
# for operation,value in result.items():
#     print(f"{operation}:{value}")
"""Question 04
Write a program to calculate area of triangle by using following formula , in this program takes all input from 
user by using built-in function.
"""
# import math
# def area_of_triangle(a,b,c):
#     s=(a+b+c)/3
#     if s>a and s>b and s>c:
#         return math.sqrt(s*(s-a)*(s-b)*(s-c))
#     else:
#         raise ValueError("the sides are not valid for a triangle")
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# c=int(input("Enter the value of c:"))
# try:
#     output=area_of_triangle(a,b,c)
#     print(f"the area of triangle:{output}")
# except ValueError as e:
#     print(e)

"""Question 05
Write a program in which take two numbers from user and swap them."""
# number1=int(input("Enter the number 1:"))
# number2=int(input("Enter the number 2:"))
# number1,number2=number2,number1
# print("After Swapping")
# print(f"first_number={number1}")
# print(f"secnd_number={number2}")
"""Question 06

Write a program that prompts the user to input a Celsius temperature and 
outputs the equivalent temperature in Fahrenheit. The formula to convert the temperature is:"""
# def convert_temperature(Celsius):
#     return ((9/5)*Celsius+32)
# Celsius=int(input("Enter the temperature in Celsius:"))
# fahrenheit=convert_temperature(Celsius)
# print(f"{Celsius}°C is equal to {fahrenheit}°F")
"""Question 07 
Write a program that accepts seconds from user as integer. Your program should converts seconds in hours, 
minutes and seconds."""
# total_seconds=int(input("Enter the seconds:"))
# Hours=total_seconds//3600
# Minutes=(total_seconds%3600)//60
# Seconds=total_seconds%60
# print(f"Hours:{Hours}, Minutes:{Minutes}, Seconds:{Seconds}")

"""Question 09. Distance Traveled
Write a program to calculate the distance traveled by a car , assuming there are no accidents or delays, the distance
 that a car travels down the inter-state can be calculated with the following formula:

             Distance=speed*time
A car is traveling at 60 miles per hour. Write a program that displays the following:
• The distance the car will travel in 5 hours
• The distance the car will travel in 8 hours
• The distance the car will travel in 12 hours"""
# def cal_distance(speed,time):
#     return speed*time
# speed=60
# times=[5,8,12]
# for time in times:
#     result=cal_distance(speed,time)
#     print(f"The distance the car will travel in {time} hours= {result}")
"""Question#10"""
no_of_share=1000
purchase_price_per_share=32.87
sale_price_per_share=33.92
commision_rate=0.02

purchase_amount=no_of_share*purchase_price_per_share
purchase_commision=purchase_amount*commision_rate
total_purchase_cost=purchase_amount+purchase_commision
sales_amount=no_of_share*sale_price_per_share
sale_commision=sale_price_per_share*commision_rate
profit=sales_amount-sale_commision-total_purchase_cost
print(f"the purchase amount per share = ${purchase_amount:.2f}")
print(f"commision paid foy buying the stock = ${purchase_commision:.2f}")
print(f"the amount after sales= ${sales_amount:.2f}")
print(f"commision paid on selling= ${sale_commision:.2f}")
print(f"profit = ${profit:.2f}")
if profit>0:
    print("Joe made a profit")
else:
    print("Loss")

   





