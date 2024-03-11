import math as m

def game(n,m):
    for j in range(n,m+1):
        bin_num = 0
        po = 0
        while(n!=0):
            rem = n % 2
            num = m.pow(10,po)
            bin_num = int(bin_num + rem * num)
            n = n // 2
            pow += 1
        print(bin_num)
    return 0
         

def main():
    n = int(input("enter an int number:\n"))
    m = int(input("enter another int number:\n"))
    game(n,m)
    
main()