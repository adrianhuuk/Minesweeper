import random as rd

diff = int(input("Enter your difficulty (1-3): "))
#diff = 1

if diff < 3:
    size = [diff * 8 for i in range(2)]
    if size == 1:
        mines = 10
    else:
        mines = 40
else:
    size = [16, 30]
    mines = 99

squares = [[0 for i in range(size[0])] for i in range(size[1])]

for i in range(mines):
    select = [rd.randrange(size[1]), rd.randrange(size[0])]
    while squares[select[0]][select[1]] == 1:
        select = [rd.randrange(size[1]), rd.randrange(size[0])]
    squares[select[0]][select[1]] = 1

#total = 0
for i in squares:
    line = []
    for j in i:
        if j == 1:
            line.append(1)
        else:
            line.append(0)
    print(line)


