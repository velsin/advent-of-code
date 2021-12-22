
from typing import List, Tuple


RAW = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

class BingoBoard:
    "Data structure for the bingo boards in the problem. Each bingo baord will contain the layout, keep track of which cells have been marked, check for wins, etc."

    def __init__(self, board, N) -> None:
        self.N = N # board size
        self.grid = self.create_grid(board)
        self.marks = self.create_marks()

    def create_grid(self, board):
        "Creates the internal grid structure as a dict, indexed by tuples"
        grid = {}
        for i in range(self.N):
            for j in range(self.N):
                grid[i,j] = board[i][j]
        return grid

    def create_marks(self):
        "Creates a similar grid strucutre as grid, but for marking numbers that have appeared."
        marks = {}
        for i in range(self.N):
            for j in range(self.N):
                marks[i,j] = 0
        return marks

    def register_number(self, num):
        "Checks if num is part of the grid. If it is, get the grid position and update score"
        for key, val in self.grid.items():
            if val == num:
                self.marks[key] += 1


def parse_input(raw_input: str) -> Tuple[List[int], List[List[List[str]]]]: # this looks so strange
    "Parses the input string into a first line of bingo numbers, and a list of list, where each sublist represents one of the boards."

    N = 5  # bingo grid size

    lines = [x for x in raw_input.rstrip().splitlines() if x.rstrip() != ""]
    bingo_numbers = lines[0].split(',')

    idx = 1
    reading = True
    boards = []

    while reading:
        try:
            board_input = [lines[i] for i in range(idx,idx+N)]
            boards.append([x.split() for x in board_input])
        except IndexError:
            print(f"end of input, read a total of {len(boards)} boards.")
            reading = False
        idx += N

    return bingo_numbers, boards

TEST_INPUT = [x for x in RAW.rstrip().splitlines() if x.rstrip() != ""]

print(TEST_INPUT)
N = 5
bingo_numbers = TEST_INPUT[0].split()
idx = 1
reading = True
boards = [[], [], []]
board = 0
while reading:
    try:
        board_input = [TEST_INPUT[i] for i in range(idx,idx+N)]
        for x in board_input:
            boards[board].append(x.split())
    except IndexError:
        print(f"end of input, read a total of {board} boards.")
        reading = False
        break
    idx += N
    board += 1
    # print(boards)



b_nums, boards2 = parse_input(RAW)


assert boards == boards2
assert b_nums == bingo_numbers

g1 = BingoBoard(boards[0],N)
print(g1.grid)

# Real run
# with open('./data/day04.txt') as f:
#     raw_inp = f.read()

# bingo_nums, boards3 = parse_input(raw_inp)

# print(boards3, bingo_nums)