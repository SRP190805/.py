n = int(input("enter lower limit:\n"))
m = int(input("enter the upper limit:\n"))
o = list(filter(lambda x : x%2==1,range(n,m)))
print()
for i in o:
    print(i)