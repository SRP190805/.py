import re as r

txt = input("enter a string:\n") #it takes a string input.

 #the [] here means a set of characters now 0-9 means single digit numbers, also the findall function returns a list of all the occurences of a single digit number in a string.
    
b = bool(r.findall("[0-9]",txt))
c = bool(r.findall("[0-9]",txt))
y = [x for x in r.findall("[0-9]", txt) if (c != b)]

 #to find any two digit number in a string, we use
x = r.findall("[0-9][0-9]", txt)
 #similarly you can do for three digit numbers.

 #also to find any particular number in a given range of numbers, for example (56,70), yhen we use
s = r.findall("[0-5][0-5]", txt) #this splitting is above the given range for numbers 0-55
a = r.findall("[7-9][1-9]", txt) #this splitting is above the given range for numbers 71-99
t = [x for x in r.findall("[5-7][0-9]", txt) if (s != a)] #now this function will add only those numbers two list which are in 56-70

#now lets do it for characters
p = r.findall("[a-z]",txt)
q = r.findall("[A-Z]",txt)
u = [x for x in r.findall("[A-Z]", txt) if (p != q)]

print(y)
print(x)
print(t)
print(u)
print("the number of capital letters in string are: {}".format(len(u)))
