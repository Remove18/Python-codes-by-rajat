matrix = []
rows = int(input("enter number of rows: "))
cols = int(input("enter number os collums: "))
for i in range (rows):
    a = []
    for j in range (cols):
        val = input()
        a.append(val)
    matrix.append(a)
for i in range (rows):
    for j in range (cols):
        print(matrix[i,j],"   ")
    print()
print(type(matrix))