def lonely_int(arr):
    ans = 0
    for item in arr:
        ans = ans^item
    return ans
def main():
    #n = int(input().split())
    a = list(map(int, input().rstrip().split()))
    result = lonely_int(a)
    print(result)
main()    