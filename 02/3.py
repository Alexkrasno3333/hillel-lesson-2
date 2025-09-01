import sys
import math
#TASK 2 HW
Enter_number=int(input("Enter your number:"))

divider=10

left, right = divmod(Enter_number, divider)
step1, step2 = divmod(left, divider)
step3, step4 = divmod(step1, divider)
step5, step6 = divmod(step3, divider)
step7, step8 = divmod(step5, divider)

print(right*10000 + step2*1000 + step4 * 100 + step6*10 + step8)