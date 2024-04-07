#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

def __init__(nums,target):
    list = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if int(nums[i]) + int(nums[j]) == target:
                list += (i,j)
    return list

def main():
    nums = list(input("enter any amount of numbers:\n ").split())
    target = int(input("enter the target number:\n "))
    a = __init__(nums,target)
    for i in range(len(a)):
        list1=[]
        for j in range(i,i+2):
            list1.append(a[j])
        print(list1)
    
main()