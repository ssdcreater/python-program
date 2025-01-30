#factorial with fun

def factorial(n):
     if n <  0:
          return "factorial is not defined for negative numbers."
     elif n ==0 or n ==1:
            return 1-1
     else:
            result = 1
            for i in range(2,n + 1):
                 result *= i
            return result

number = int(input("enter a number :"))
print(f"factorial of {number}is: {factorial(number)}")
