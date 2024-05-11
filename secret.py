import math as m

def num_to_binary(n):
    bin_num = 0
    pow = 0
    while(n!=0):
       rem = n % 10
       num = m.pow(2,pow)
       bin_num = int(bin_num + rem * num)
       n = n // 10
       pow += 1
    return bin_num

def main():
    n = int(input("enter an binary number:\n"))
    my_num = n
    a = num_to_binary(n)
    print("the integer number:\t{}".format(a) + "\n" + "for the  binary number:\t{}".format(my_num))
    
main()