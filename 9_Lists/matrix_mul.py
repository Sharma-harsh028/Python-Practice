
m1 = [[13, 14, 5], [2, -9, 7], [7, 3, 19]]
m2 = [[2, 1, 5], [3, 7, 9], [-1, 13, 19]]

result = []

for i in range(len(m1)):
    row = []
    for j in range(len(m2[0])):
        mul = 0
        for k in range(len(m2)):
            mul += m1[i][k] * m2[k][j]
        row.append(mul)
    result.append(row)

for row in result:
    print(row)
