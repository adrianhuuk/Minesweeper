import random as rd

diff = int(input("Enter your difficulty (1-3): "))

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
    #select = squares[rd.randrange(size[1])][rd.randrange(size[0])]
    select = [rd.randrange(size[1]), rd.randrange(size[0])]
    if squares[select[0]][select[1]] != 1:
        select = squares[select[0]][select[1]]
        print(select)

total = 0
for i in squares:
    print(i)
    total += 1
print(total)


