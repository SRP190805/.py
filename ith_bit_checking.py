def check_ith_bit(n,i):
   return n&(1<<i)
def main():
   n =int(input("enter int number:\n"))
   i = int(input("enter bit position to be checked:\n"))
   a = check_ith_bit(n,i)
   print(a)
main()