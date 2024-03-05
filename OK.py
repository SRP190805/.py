def substring(n):
    s = []
    k = []
    m = []
    l = 0
    for i in n:
        if i not in s:
            s.append(i) 
           # s.clear()  
        else:
            k.append(i)    
    return len(s)
def main():
    n = input("enter a string:\n")
    a = substring(n)
    print(a)
main()    