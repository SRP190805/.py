n = int(input())
m=0
x=0
for i in range(1,n+1):
    for j in range(0,i):
        print(j+1,end=" ")
        if j == i-2:
            x =j-2
            break
    m = x
    for k in range(x,0,-1):
        print(k,end=" ")
    print()