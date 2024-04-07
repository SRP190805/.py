def zigzag(n,elements):
    mid = n//2
    elements[mid:] = sorted(elements[mid:], reverse= True)
def main():
    n = int(input("enter number of terms:\n"))
    for i in range(n):
        elements =  int(input("enter {} number:\n".format(i+1)))
    zigzag(n,elements)
    for i in range(n):
        print(elements[i])

main()