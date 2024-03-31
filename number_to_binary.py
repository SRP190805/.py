import math as m

def num_to_binary(n):
    bin_num = 0
    pow = 0
    while(n!=0):
       rem = n % 2
       num = m.pow(10,pow)
       bin_num = int(bin_num + rem * num)
       n = n // 2
       pow += 1
    return bin_num

def main():
    n = int(input("enter an int number:\n"))
    my_num = n
    a = num_to_binary(n)
    print("the binary number:\t{}".format(a) + "\n" + "for the integer number:\t{}".format(my_num))
    
import math as m

def num_to_binary(n):
    bin_num = 0
    pow = 0
    while(n!=0):
       rem = n % 2
       num = m.pow(10,pow)
       bin_num = int(bin_num + rem * num)
       n = n // 2
       pow += 1
    return bin_num

def main():
    n = int(input("enter an int number:\n"))
    my_num = n
    a = num_to_binary(n)
    print("the binary number:\t{}".format(a) + "\n" + "for the integer number:\t{}".format(my_num))
    
main()