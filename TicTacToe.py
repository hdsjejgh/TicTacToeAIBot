

class Board:
    def __init__(self):
        self.board = [0,1,2,3,4,5,6,7,8]
    def printBoard(self):
        for i in range(3):
            s=""
            for ii in range(3):
                s+=str(self.board[ii+3*i])
            print(s)
    def playerTurn(self):
        choice = None
        self.printBoard()
        if self.getWinner(self.board.copy()) is not None:
            return
        while True:
            try:
                choice = int(input("Choose a square: "))
                assert choice in self.board
                break
            except ValueError:
                print("Enter a valid square")
        self.updateBoard(choice,"X")
        winner = self.getWinner(self.board.copy())
        if winner == "X":
            print("Player wins")
            quit()
        elif winner == "O":
            print("AI Wins")
            quit()
        elif winner == "Tie":
            print("Tie")
            quit()
        self.AITurn()
    def updateBoard(self,action,symbol):
        assert action in self.board, "Invalid Action"
        self.board[action]=symbol
    def AITurn(self):
        possible = []
        for i in self.board:
            if i not in ("X","O"):
                possible.append(i)
            else:
                possible.append(None)
        for i in range(len(possible)):
            if possible[i] is not None:
                possible[i] = self.min(i,self.board.copy())
            else:
                possible[i] = 99999999
        #print(possible)
        self.board[possible.index(min(possible))] = "O"
        #print(possible.index(min(possible)))
        self.playerTurn()

        winner = self.getWinner(self.board.copy())
        if winner=="X":
            print("Player wins")
            quit()
        elif winner=="O":
            print("AI Wins")
            #print(self.board)
            quit()
        elif winner=="Tie":
            print("Tie")
            #print("gg")
            quit()


    def min(self,sq,board):
        b=board
        b[sq]="O"
        #print(b)
        #print(self.board==b)
        #print()
        winner = self.getWinner(board)
        if winner is not None:
            if winner == "X":
                return 1
            elif winner=="O":
                return -1
            elif winner=="Tie":
                return 0
        possible = []
        for i in board:
            if i not in ("X", "O"):
                possible.append(i)
                #print(i)
            else:

                #print(None)
                possible.append(None)
        for i in range(len(possible)):
            if possible[i] is not None:
                possible[i] = self.max(i, board.copy())
            else:
                possible[i]=-99999999
        return max(possible)

    def max(self,sq,board):
        board[sq]="X"
        winner = self.getWinner(board)
        if winner is not None:
            if winner == "X":
                return 1
            elif winner=="O":
                return -1
            elif winner=="Tie":
                return 0
        possible = []
        for i in board:
            if i not in ("X", "O"):
                possible.append(i)
            else:
                possible.append(None)
        for i in range(len(possible)):
            if possible[i] is not None:
                possible[i] = self.min(i, board.copy())
            else:
                possible[i] = 99999999
        return min(possible)

    def play(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.playerTurn()

    def getWinner(self, board):
        if board[0]==board[1]==board[2]:
            return board[0]
        elif board[4]==board[5]==board[3]:
            return board[3]
        elif board[6]==board[8]==board[7]:
            return board[7]
        elif board[0]==board[3]==board[6]:
            return board[0]
        elif board[1]==board[4]==board[7]:
            return board[1]
        elif board[2]==board[5]==board[8]:
            return board[2]
        elif board[0]==board[4]==board[8]:
            return board[0]
        elif board[2]==board[4]==board[6]:
            return board[2]
        elif board.count("X")+board.count("O")==9:
            return "Tie"
        else:
            return None

if __name__ == "__main__":
    b = Board()
    b.play()