# def narcissistic(num):
#     sumOfDigits = 0
#     digits = [int(ch) for ch in str(num)]
#     power  = len(digits)
    
#     for i in range(len(digits)):
#         sumOfDigits += digits[i]**power
        
#     return (sumOfDigits == num)


# # ------------------ TEST ------------------
# print('7 is narcissistic: ' + str(narcissistic(7) == True))
# print('5 is narcissistic: ' + str(narcissistic(5) == True))
# print('371 is narcissistic: ' + str(narcissistic(371) == True))
# print('1634 is narcissistic: ' + str(narcissistic(371) == True))
# print('153 is narcissistic:' + str(narcissistic(153) == True))
# print('\n')
# print('100 is not narcissistic: ' + str(narcissistic(100) == False))
# print('66378 is not narcissistic: ' + str(narcissistic(66378) == False))
# print('36075 is not narcissistic: ' + str(narcissistic(36075) == False))
# print('122 is not narcissistic: ' + str(narcissistic(122) == False))
# print('4887 is not narcissistic: ' + str(narcissistic(4887) == False))




#this newer code is much more flexible
import math
n = int(input())
x = int(math.log10(n)) + 1

a = 0
rem = 0
temp = n          ## BECAUSE THE VALUE OF N CHANGES EVERYTIME INSIDE THE LOOP SO WE WANT TO STORE IT SOMEWHERE
while temp > 0:
    rem = temp%10
    a = rem**x + a
    temp = temp//10
if a == n:
    print("true")
elif a != n:
    print("false")
