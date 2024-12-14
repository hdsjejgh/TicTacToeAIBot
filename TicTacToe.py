from random import randint

class Board:
    """The board, create instance of this class and run the play method to play"""

    def __init__(self):
        self.__board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.__gameEnded = False
        
    def play(self,player="X",canExit=False):
        """It plays the game who would have thought. It also resets the game every time it's called
        \nThe player parameter can be X or O, its X by default, if its X the player starts, if its O the AI starts, you know this
        \nThe canExit parameter decides whether or not the plater has the option to exit the game on their turn. defaults to False
        """

        assert player in ("X", "O"), f"Player must be X or O, not {player}"
        self.__player = player
        self.__canExit = canExit
        self.__gameEnded=False
        self.__board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        print("---Tic Tac Toe---")
        for i in range(1):
            print()
        if self.__player=="X":
            self.__playerTurn()
        else:
            self.__AITurn()

    def print(self):
        """Prints the board"""
        try:
            print()
            self.__printBoard()
        except:
            print("0 1 2\n3 4 5\n6 7 8")

    def __printBoard(self):

        for i in range(3):
            s=""
            for ii in range(3):
                s+=str(self.__board[ii+3*i])+" "
            print(s)

    def __playerTurn(self):
        self.__printBoard()
        if self.__getWinner(self.__board.copy()) is not None:
            return
        while True:
            try:
                if not self.__canExit:
                    choice = int(input(f"Choose a square. You are {self.__player}: "))
                    assert choice in self.__board, "Invalid square"
                    break
                else:
                    choice = input(f"Choose a square. You are {self.__player} (Enter X to exit): ")
                    if choice.upper()=="X":
                        self.__gameEnded=True
                        return
                    choice = int(choice)
                    assert choice in self.__board
                    break
            except:
                print("\033[31mEnter a valid square\033[0m")
        self.__updateBoard(choice,self.__player)
        winner = self.__getWinner(self.__board.copy())
        if winner == self.__player and not self.__gameEnded:
            print("\033[32mPlayer wins\033[0m")
            self.__gameEnded=True
        elif winner == {"X":"O","O":"X"}[self.__player] and not self.__gameEnded:
            print("\033[32mAI Wins\033[0m")
            self.__gameEnded=True
        elif winner == "Tie" and not self.__gameEnded:
            print("\033[32mTie\033[0m")
            self.__gameEnded=True
        self.__AITurn()

    def __updateBoard(self,action,symbol):
        assert action in self.__board, "Invalid Action"
        self.__board[action]=symbol
        
    def __AITurn(self):
        possible = []
        for i in self.__board:
            if i not in ("X","O"):
                possible.append(i)
            else:
                possible.append(None)
        for i in range(len(possible)):
            if possible[i] is not None:
                if self.__player =="X":
                    possible[i] = self.__min(i,self.__board.copy())
                else:
                    possible[i] = self.__max(i, self.__board.copy())
            else:
                possible[i] = 99999999 if self.__player == "X" else -999999
        #print(possible)
        if self.__player=="X":
            self.__board[self.__randomChoice(min(possible),possible)] = "O"
        else:
            self.__board[self.__randomChoice(max(possible),possible)] = "X"
        self.__playerTurn()

        winner = self.__getWinner(self.__board.copy())
        if winner==self.__player and not self.__gameEnded:
            print("\033[32mPlayer wins\033[0m")
            self.__gameEnded=True
        elif winner=={"X":"O","O":"X"}[self.__player] and not self.__gameEnded:
            print("\033[32mAI Wins\033[0m")
            #print(self.__board)
            self.__gameEnded=True
        elif winner=="Tie" and not self.__gameEnded:
            print("\033[32mTie\033[0m")
            #print("gg")
            self.__gameEnded=True
            
    def __min(self,sq,board):
        b=board
        b[sq]="O"
        #print(b)
        #print(self.__board==b)
        #print()
        winner = self.__getWinner(board)
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
                possible[i] = self.__max(i, board.copy())
            else:
                possible[i]=-99999999
        return max(possible)

    def __max(self,sq,board):
        board[sq]="X"
        winner = self.__getWinner(board)
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
                possible[i] = self.__min(i, board.copy())
            else:
                possible[i] = 99999999
        return min(possible)
    
    def __getWinner(self, board):
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

    def __randomChoice(self,val,lis):
        i = randint(0,len(lis)-1)
        while lis[i]!=val:
            i = randint(0, len(lis) - 1)
        return i

if __name__ == "__main__":
    b = Board()
    b.play()