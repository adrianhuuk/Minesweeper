# Initial Script

import random as rd

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
        
            # Displayed Grid Setup

        self.display = []

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
                self.display.append(line)
        # Other Setup

        self.gridKey = {"d":self.display, "m":self.squares}

    def prt(self, type):
        for i in self.gridKey[type]:
            print(i)
        
dGrid = Grid()

dGrid.prt("d")