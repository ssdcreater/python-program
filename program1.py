#write a program to point all prime number 1 to100

for num in range(1,101):
  is_prime=True
 for i in range(2,num):
  if num %i==0:
      is_prime = False
      break
    if is_prime:
        print num)
