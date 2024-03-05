def power_of_two(n):
   if n==0: return False
   return not n&(n-1)
def main():
   n =int(input("enter int number:\n"))
   a = power_of_two(n)
   print(a)
main()