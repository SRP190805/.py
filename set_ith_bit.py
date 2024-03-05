def set_i_bit(n,i):
   return n|(1<<i)
def main():
   n =int(input("enter int number:\n"))
   i = int(input("enter bit to be set:\n"))
   a = set_i_bit(n,i)
   print(a)
main()