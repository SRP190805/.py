def my_function(x):
  list1 = sorted(list(dict.fromkeys(x)))
  return list1

mylist = my_function(input("enter list items:\n").split())

print(mylist)