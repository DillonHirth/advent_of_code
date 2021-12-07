# PART 1
# pulled parts heavily from https://www.codespeedy.com/create-bingo-game-using-python/
class BingoBoard:
    def __init__(self, input_board):
        self.position = {}
        self.playBoard = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.bingo = {
            "row": [0, 0, 0, 0, 0],
            "col": [0, 0, 0, 0, 0]
        }
        self.createBoard(input_board)
        self.winning_score = 0
        self.bingo_count = 0

    def createBoard(self, input_board):
        for i in range(5):
            for j in range(5):
                choice = input_board[i][j]
                self.playBoard[i][j] = choice
                self.position[choice] = (i, j)

    def updateBoard(self, val):
        if self.position.get(val) == None:
            pass
        else:
            x, y = self.position.get(val)
            self.playBoard[x][y] = 'X'
            self.updateBingo(x, y)

    def updateBingo(self, x, y):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1

    def checkBingo(self, draw):
        board_sum = 0
        if self.bingo_count == 0:
            if 5 in self.bingo["row"] or 5 in self.bingo["col"]:
                for i in range(5):
                    for j in range(5):
                        if self.playBoard[i][j] == 'X':
                            pass
                        else:
                            board_sum += self.playBoard[i][j]
                self.winning_score = board_sum * draw
                self.bingo_count = 1
                return "BINGO"
            else:
                return "no bingo"


class BingoSubsystems:
    def __init__(self):
        with open('input.txt') as input_file:
            self.draw_list = [x.strip('\n') for x in input_file.readline().split(',')]
            self.board_list = []
            for line in input_file:
                temp_board = []
                if line == '\n':
                    for i in range(5):
                        row = input_file.readline().strip('\n').split(' ')
                        row_clean = [int(x) for x in row if x != '']
                        temp_board.append(row_clean)
                        i += 1
                    self.board_list.append(BingoBoard(temp_board))




bingo = BingoSubsystems()
for draw in bingo.draw_list:
    for item in bingo.board_list:
        draw = int(draw)
        item.updateBoard(draw)
        if item.checkBingo(draw) == "BINGO":
            print("winning board: ", item.playBoard)
            print("winning score: ", item.winning_score)
    else:
        continue

