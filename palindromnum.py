#check number is palindrom or not

num = (input("enter the number :"))

if num == num[::-1]:
    print(f"{num} is palindrom.")
else:
    print(f"{num} is not palindrom.")
    
         
         
