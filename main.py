import random as rd

import time

diff = int(input("Enter your difficulty (1-3): "))

# Grid Class Script

class Grid:
    def __init__(self):
        
        # Mines Grid Setup

        setup = {1:[10, [8, 8]], 2:[40, [16, 16]], 3:[99, [16, 30]]}

        self.size = setup[diff][1]
        self.minesnum = setup[diff][0]

        self.mines = [[0 for i in range(self.size[0])] for i in range(self.size[1])]

        for i in range(self.minesnum):
            select = [rd.randrange(self.size[1]), rd.randrange(self.size[0])]
            while self.mines[select[0]][select[1]] == 1:
                select = [rd.randrange(self.size[1]), rd.randrange(self.size[0])]
            self.mines[select[0]][select[1]] = 1
        
        # Layout Grid Setup

        self.layout = []

        for i in range(len(self.mines)):
                line = []
                for j in range(len(self.mines[i])):
                    temp = 0
                    for k in range(3):
                        for l in range(3):
                            if not (k == 1 and l == 1) and not (i == 0 and k == 0):
                                try:
                                    temp += self.mines[i+(k-1)][j+(l-1)]
                                except IndexError:
                                    pass
                    line.append(str(temp))
                self.layout.append(line)

        # Display Grid Setup

        self.display = [["x" for j in range(self.size[0])] for i in range(self.size[1])]

        # Other Setup

        self.gridKey = {"l":self.layout, "m":self.mines, "d":self.display}

    def prt(self, type):
        for i in self.gridKey[type]:
            print(i)
        
# Game Script

dGrid = Grid()
on = True
move = 0

dGrid.prt("l")
print("\n")
dGrid.prt("m")
print("\n")

while on == True:
    dGrid.prt("d")

    # Input Script
    
    if not move == 0:
        action = input("Chose your action (\"dig\" or \"flag\")")
        while not ((action == "dig" or action == "flag")):
            action = input("Please re-enter your action - INPUT IS CASE SENSATIVE (\"dig\" or \"flag\")")
    else:
        action = "dig"

    coords = [0, 99]
    while not ((0 <= coords[0]) and (coords[0] < dGrid.size[0]) and (0 <= coords[1]) and (coords[1] < dGrid.size[1])):
        coords = [int(input("Please enter an x coordinate at least 0 and less than " + str(dGrid.size[0]) + ". ")), int(input("Please enter an y coordinate at least 0 and  less than " + str(dGrid.size[1]) + ". "))]
    
    # First-move Mine relocation Script

    # BUG IF USER SELECTS 0, 0 AS FIRST COORDINATE - Can lose on first move.

    if dGrid.mines[coords[1]][coords[0]] == 1 and move == 0:
        dGrid.mines[coords[1]][coords[0]] = 0
        square = 0

        while dGrid.mines[int(square - (square % dGrid.size[0]) / dGrid.size[0])][square - int(square - (square % dGrid.size[0]) / dGrid.size[0]) * dGrid.size[1]] == 1:
            square += 1
        
        dGrid.mines[int(square - (square % dGrid.size[0]) / dGrid.size[0])][square - int(square - (square % dGrid.size[0]) / dGrid.size[0]) * dGrid.size[1]] = 1
    
    # Display Grid Ammendments

    if action == "dig":
        if dGrid.mines[coords[1]][coords[0]] == 0:
            dGrid.display[coords[1]][coords[0]] = dGrid.layout[coords[1]][coords[0]]
            if dGrid.layout[coords[1]][coords[0]] == "0":
                queue = []
                for i in range(3):
                    for j in range(3):
                        try:
                            if not (i == 1 and j == 1) and not (coords[1] == 0 and i == 0) and dGrid.layout[coords[1]-1+i][coords[0]-1+j] == "0":
                                queue.append([coords[1]-1+i, coords[0]-1+j])
                        except IndexError:
                            pass

                queueremoved = []

                while queue:
                    print(queue)

                    # Removes all dupliates from queue. (Now done by following scipt by not adding duplicates in the first place)

                    # queue = [tuple(i) for i in queue]
                    # queue = list(dict.fromkeys(queue))
                    # queue = [list(i) for i in queue]

                    # Selects Active Square

                    coords = [queue[0][1], queue[0][0]]

                    # Queues all squares surrouunding active square with a zero not previously queued.

                    for i in range(3):
                        for j in range(3):
                            try:
                                if not (i == 1 and j == 1) and not (coords[1] == 0 and i == 0) and dGrid.layout[coords[1]-1+i][coords[0]-1+j] == "0":
                                    if not ([coords[1]-1+i, coords[0]-1+j] in queue):
                                        queue.append([coords[1]-1+i, coords[0]-1+j])
                            except IndexError:
                                pass
                    
                    # Removes all squares previously removed from queue

                    for i in queueremoved:
                        try:
                            queue.remove(i)
                        except ValueError:
                            pass

                    # Reveals all squares surrounding active square

                    for i in range(3):
                        for j in range(3):
                            try:
                                if not (coords[1] == 0 and i == 0):
                                    dGrid.display[coords[1]-1+i][coords[0]-1+j] = dGrid.layout[coords[1]-1+i][coords[0]-1+j]
                            except IndexError:
                                pass 

                    # Removes active square from queue and log removal to ensure that the same square cannot be revisited.
                    
                    queueremoved.append(queue[0])
                    queue.remove(queue[0])
                    

        else:
            print("GAME OVER")
            on = False
    else:
        dGrid.display[coords[1]][coords[0]] = "f"

    # End of Turn
    move += 1
    #on = False

