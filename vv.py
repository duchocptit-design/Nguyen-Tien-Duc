n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
total = 0
for i in range(n):
    total += matrix[i][i]
print(total)