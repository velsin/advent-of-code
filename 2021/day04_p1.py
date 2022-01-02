
from typing import Dict, List, Tuple


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
        self.win = False
        self.score = 0

    def create_grid(self, board) -> Dict[Tuple[int],str]:
        "Creates the internal grid structure as a dict, indexed by tuples"
        grid = {}
        for i in range(self.N):
            for j in range(self.N):
                grid[i,j] = board[i][j]
        return grid

    def create_marks(self) -> Dict[Tuple[int],str]:
        "Creates a similar grid strucutre as grid, but for marking numbers that have appeared."
        marks = {}
        for i in range(self.N):
            for j in range(self.N):
                marks[i,j] = 0
        return marks

    def register_number(self, num) -> None:
        "Checks if num is part of the grid. If it is, get the grid position and update score"
        for key, val in self.grid.items():
            if val == num:
                self.marks[key] += 1

        self.check_win(num)

        return None
        # check for win

    def check_win(self, num) -> None:
        # rows:
        for i in range(self.N):
            rowsum = sum([self.marks[i,j] for j in range(self.N)])
            if rowsum == self.N:
                self.win = True
                self.score = int(num)*self.calculate_unmarked_sum()

        # cols
        for j in range(self.N):
            colsum = sum([self.marks[i,j] for i in range(self.N)])
            if colsum == self.N:
                self.win = True
                self.score = int(num)*self.calculate_unmarked_sum()

        return None

    def calculate_unmarked_sum(self) -> int:
        res = 0
        for key, val in self.marks.items():
            if val == 0:
                res += int(self.grid[key])

        return res


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


# bingo_numbers, raw_boards = parse_input(RAW)
# bingo_boards = [BingoBoard(x, N=5) for x in raw_boards]
# has_won = False

# # start looping through the bingo numbers until you hit a win
# for num in bingo_numbers:
#     for idx, board in enumerate(bingo_boards):
#         board.register_number(num)

#         if board.win and not has_won:
#             print(f"win on number {num}, board nr {idx+1}, score: {board.score}")
#             has_won = True
#             winscore = board.score
    
#     if has_won:
#         break

# assert winscore == 4512

if __name__=='__main__':

    with open('./data/day04.txt') as f:
        raw_inp = f.read()

    bingo_numbers, raw_boards = parse_input(raw_inp)

    bingo_boards = [BingoBoard(x, N=5) for x in raw_boards]
    has_won = False

    for num in bingo_numbers:
        for idx, board in enumerate(bingo_boards):
            board.register_number(num)

            if board.win and not has_won:
                print(f"win on number {num}, board nr {idx+1}, score: {board.score}")
                has_won = True
                winscore = board.score
        
        if has_won:
            break