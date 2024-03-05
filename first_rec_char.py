n = input("enter any string\n:")
def first_recursive_char(n):
    s = []
    k = []
    for i in n:
        if i in s:
            #return i
            if i not in k:
                if i != ' ':
                  k.append(i)
        else:
            s.append(i)
    return k        

def main(n):
    a = first_recursive_char(n)
    print(a)
    
main(n)