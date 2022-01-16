class tic_tae_toe:  

    def __init__(self,count_turn,board):
        self.count_turn=count_turn
        self.board=board

    def print_Board(self):
        print('  a     b     c  ')
        print('     |     |     ')
        print('1 {}  |  {}  |  {}  '.format(self.board['a1'],self.board['b1'],self.board['c1']))
        print('_____|_____|_____')
        print('     |     |     ')
        print('2 {}  |  {}  |  {}  '.format(self.board['a2'],self.board['b2'],self.board['c2']))
        print('_____|_____|_____')
        print('     |     |     ')
        print('3 {}  |  {}  |  {}  '.format(self.board['a3'],self.board['b3'],self.board['c3']))
        print('     |     |     ')

    def player(self):
        if self.count_turn%2!=0:
            return 'X'
        else:
            return 'O'


    def set_board(self,number):
        self.board[number]=tic_tae_toe.player(self)

    def check_victory(self):
        if self.board['a1'] == tic_tae_toe.player(self) and self.board['b1']  == tic_tae_toe.player(self) and self.board['c1'] == tic_tae_toe.player(self):
             return True
        elif self.board['a1'] == tic_tae_toe.player(self) and self.board['a2']  == tic_tae_toe.player(self) and self.board['a3'] == tic_tae_toe.player(self):
             return True
        elif self.board['a1'] == tic_tae_toe.player(self) and self.board['b2']  == tic_tae_toe.player(self) and self.board['c3'] == tic_tae_toe.player(self):
             return True
        elif self.board['a2'] == tic_tae_toe.player(self) and self.board['b2']  == tic_tae_toe.player(self) and self.board['c2'] == tic_tae_toe.player(self):
             return True
        elif self.board['a3'] == tic_tae_toe.player(self) and self.board['b3']  == tic_tae_toe.player(self) and self.board['c3'] == tic_tae_toe.player(self):
             return True
        elif self.board['b1'] == tic_tae_toe.player(self) and self.board['b2']  == tic_tae_toe.player(self) and self.board['b3'] == tic_tae_toe.player(self):
             return True
        elif self.board['a3'] == tic_tae_toe.player(self) and self.board['b2']  == tic_tae_toe.player(self) and self.board['c1'] == tic_tae_toe.player(self):
             return True
        elif self.board['c1'] == tic_tae_toe.player(self) and self.board['c2']  == tic_tae_toe.player(self) and self.board['c3'] == tic_tae_toe.player(self):
             return True
        else:
             return False


board={'a1' : "-", 'b1' : "-", 'c1' : "-",'a2' : "-", 'b2' : "-", 'c2' : "-",'a3' : "-", 'b3' : "-", 'c3' : "-"}

count_turn=1   

game1 = tic_tae_toe(count_turn,board)

game1.print_Board()

while game1.count_turn<=9:
    
    print('Next Player:',game1.player())
    
    print('>',end='')
    
    number=input()

    game1.set_board(number)

    game1.print_Board()

    if game1.check_victory():
        print(game1.player(),'의 승리')
        break
    
    game1.count_turn+=1

if game1.check_victory()==False:
    print('무승부')
    

