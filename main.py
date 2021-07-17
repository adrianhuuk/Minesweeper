import random as rd

diff = int(input("Enter your difficulty (1-3): "))
#diff = 1

setup = {1:[10, [8, 8]], 2:[40, [16, 16]], 3:[99, [16, 30]]}

size = setup[diff][1]
mines = setup[diff][0]

squares = [[0 for i in range(size[0])] for i in range(size[1])]

for i in range(mines):
    select = [rd.randrange(size[1]), rd.randrange(size[0])]
    while squares[select[0]][select[1]] == 1:
        select = [rd.randrange(size[1]), rd.randrange(size[0])]
    squares[select[0]][select[1]] = 1

for i in squares:
    line = []
    for j in i:
        if j == 1:
            line.append(1)
        else:
            line.append(0)
    print(line)


