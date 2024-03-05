count = 0
n = int(input("enter an integr number:\n"))
while n > 0:
   if (n&1==1): 
      count+=1 
   n=n>>1
print(count) 