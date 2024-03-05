def long_palindromic_substring(n):
    s =[]
    k = []
    l = len(n)
    for i in range(l):
        for j in range(i):
            if n[i] == n[l-1]:
               k.append(n[i:l//2]) 
            else:
               pass
    return k

def main():
    n = input("enter a string:\n")   
    str = " "
    a = long_palindromic_substring(n)          
    for j in a:
        str = str + j
    print(str)    

main()    