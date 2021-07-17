# Initial Script

import random as rd

diff = int(input("Enter your difficulty (1-3): "))
#diff = 2

# Setup Script

setup = {1:[10, [8, 8]], 2:[40, [16, 16]], 3:[99, [16, 30]]}

size = setup[diff][1]
mines = setup[diff][0]

squares = [[0 for i in range(size[0])] for i in range(size[1])]

for i in range(mines):
    select = [rd.randrange(size[1]), rd.randrange(size[0])]
    while squares[select[0]][select[1]] == 1:
        select = [rd.randrange(size[1]), rd.randrange(size[0])]
    squares[select[0]][select[1]] = 1


# for i in squares:
#      line = []
#      for j in i:
#          if j == 1:
#              line.append(1)
#          else:
#              line.append(0)
#      print(line)

# Display Script

display = []
for i in range(len(squares)):
    line = []
    for j in range(len(squares[i])):
        #line.append((squares[i-1][j-1] + squares[i-1][j] + squares[i-1][j+1]) + (squares[i][j-1] + squares[i][j+1]) + (squares[i+1][j-1] + squares[i+1][j] + squares[i+1][j+1]))
        temp = 0
        for k in range(3):
            for l in range(3):
                if not (k == 1 and l == 1) and not (i == 0 and k == 0):
                    try:
                        temp += squares[i+(k-1)][j+(l-1)]
                    except IndexError:
                        pass
        line.append(temp)
    display.append(line)
for i in display:
    print(i)
