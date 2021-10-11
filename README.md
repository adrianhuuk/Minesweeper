# Minesweeper
This is a terminal-based re-creation of the classic game Minesweeper.

When you begin the game, you will be asked to choose your difficulty. This will affect the number of mines as well as the area that you will be playing in. The difficulties are as follows:
    1. 10 mines, 8x8
    2. 40 mines, 16x16
    3. 99 mines, 16x30
Once you have chosen your difficulty, you will be asked to enter coordinates. This will be the first square revealed. After this, on each go you will be asked whether you or dig or flag before entering coordinates.

PLEASE NOTE THAT COORDINATES ARE 0-INDEXED AND SHOULD BE COUNTED STARTING FROM THE TOP-LEFT.

EG. In the grid below, the x is in the coordinate position (0,4)

    . . . . .
    . . . . .
    . . . . .
    . . . . .
    x . . . .