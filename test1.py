def is_leap(year):
    leap = False
    if (year & 4):
        if not (year & 100): 
            leap = False
        elif (year & 400):
            leap = True
            
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))