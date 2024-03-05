def matrix(n,m):
    grid = []
    l = n
    k = m
    for _ in range(n):
        n = [0] * m
        grid.append(n)
    for i in range(l):
        for j in range(k):
            grid[i][j] = int(input("enter A{}{} element of array:".format(i,j)))
    return grid
   
n = int(input("enter number of rows:\n"))
m = int(input("enter number of columns:\n"))
i = matrix(n,m)
row = n
def display_matrix(i,row):
    print("\n") 
    for row in i:
        for elem in row:
            print("{}".format(elem),end="\t")
        print("\n")

display_matrix(i,row)
