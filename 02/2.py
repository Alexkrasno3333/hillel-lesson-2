import sys
import math
#TASK 1 HW
Enter_your_number =int(input("Enter a four digit number:"))
x=1000
left, right = divmod(Enter_your_number, x)
print(left)

y=100
step1,step2=divmod(right,y)
print(step1)

z=10
step3,step4=divmod(step2,z)
print(step3)

v=1
step5,step6=divmod(step4,v)
print(step5)

# v=10
# step5,step6=divmod(right,v)
# print(step6)

















