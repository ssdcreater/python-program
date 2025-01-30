#krishnamurthy Number For

import math
num = int(input("enter the Number :"))
org_num =num
sum_num =0

for digit in str(num):
    sum_num +=math.factorial(int(digit))

if sum_num == org_num:
    print(f"{org_num}is a krishnamurthy number.")
else:
    print("f{org_num}is not a krishnamurthy number.")
