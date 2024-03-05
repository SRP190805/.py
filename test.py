def zeroes_at_end(arr):
    zeroindex = 0
    nonzero_index = 0
    temp = 0
    for zeroindex in range(len(arr)):
        for nonzero_index in range(zeroindex):
            if arr[nonzero_index] == 0:
               temp = arr[nonzero_index]
               arr[nonzero_index] = arr[zeroindex]
               arr[zeroindex] = temp
    return arr

def main():
    n = int(input("enter number of terms:\n"))
    arr = input("enter {} numbers :\n".format(n))
    k = [n*2]
    b = 0
    for i in range(-n//2,n,-1):
        if arr[i] != ' ':
            a = int(arr[i])
            k.append(a)    
    a = zeroes_at_end(k)
    print(a)

main()