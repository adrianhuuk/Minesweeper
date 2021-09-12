import random as rd

import time

diff = int(input("Enter your difficulty (1-3): "))

# Grid Class Script

class Grid:
    def __init__(self):
        
        # Mines Grid Setup

        setup = {1:[10, [8, 8]], 2:[40, [16, 16]], 3:[99, [16, 30]]}

        self.size = setup[diff][1]
        self.mines = setup[diff][0]

        self.squares = [[0 for i in range(self.size[0])] for i in range(self.size[1])]

        for i in range(self.mines):
            select = [rd.randrange(self.size[1]), rd.randrange(self.size[0])]
            while self.squares[select[0]][select[1]] == 1:
                select = [rd.randrange(self.size[1]), rd.randrange(self.size[0])]
            self.squares[select[0]][select[1]] = 1
        
        # Layout Grid Setup

        self.layout = []

        for i in range(len(self.squares)):
                line = []
                for j in range(len(self.squares[i])):
                    #line.append((self.squares[i-1][j-1] + self.squares[i-1][j] + self.squares[i-1][j+1]) + (self.squares[i][j-1] + self.squares[i][j+1]) + (self.squares[i+1][j-1] + self.squares[i+1][j] + self.squares[i+1][j+1]))
                    temp = 0
                    for k in range(3):
                        for l in range(3):
                            if not (k == 1 and l == 1) and not (i == 0 and k == 0):
                                try:
                                    temp += self.squares[i+(k-1)][j+(l-1)]
                                except IndexError:
                                    pass
                    line.append(temp)
                self.layout.append(line)

        # Display Grid Setup

        self.display = [[0 for j in range(self.size[0])] for i in range(self.size[1])]


        # Other Setup

        self.gridKey = {"l":self.layout, "s":self.squares, "d":self.display}

    def prt(self, type):
        for i in self.gridKey[type]:
            print(i)
        
# Game Script

dGrid = Grid()
on = True
move = 0

while on == True:
    dGrid.prt("d")

    # Input Script

    action = input("Chose your action (\"dig\" or \"flag\")")
    while not (action == "dig" or action == "flag"):
        action = input("Please re-enter your action - INPUT IS CASE SENSATIVE (\"dig\" or \"flag\")")

    coords = [0, 99]
    while not ((0 <= coords[0]) and (coords[0] < dGrid.size[0]) and (0 <= coords[1]) and (coords[1] < dGrid.size[1])):
        coords = [int(input("Please enter an x coordinate at least 0 and  less than " + str(dGrid.size[0]) + ".")), int(input("Please enter an y coordinate at least 0 and  less than " + str(dGrid.size[1]) + "."))]
    
    # First-move Mine relocation Script

    if dGrid.squares[coords[1]][coords[0]] == 1 and move == 0:
        dGrid.squares[coords[1]][coords[0]] = 0
        square = 0

        while dGrid.squares[int(square - (square % dGrid.size[0]) / dGrid.size[0])][square - int(square - (square % dGrid.size[0]) / dGrid.size[0]) * dGrid.size[1]] == 1:
            square += 1
        
        dGrid.squares[int(square - (square % dGrid.size[0]) / dGrid.size[0])][square - int(square - (square % dGrid.size[0]) / dGrid.size[0]) * dGrid.size[1]] = 1
    
    # End of Turn

    move += 1
    on = False

