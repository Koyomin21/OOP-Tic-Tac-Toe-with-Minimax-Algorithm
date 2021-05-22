class Board:

    def __init__(self):
        self.board = [1,2,3,4,5,6,7,8,9]
        self.used = []

    def display(self):
        """Displays board in the console"""
        print('-------------')
        for i in range(3):
            print('| ', end='')
            print(*self.board[i*3:(i+1)*3], sep=' | ', end='')
            print(' | ')
            print('-------------')

    def set_field(self, field, notation):
        field = int(field)
        self.board[field-1] = notation
        self.used.append(str(field))
        
    
    def remove_field(self, field):
        field = int(field)
        self.board[field-1] = str(field)
        self.used.remove(str(field))
        

    
    def check_win(self, notation):
        """Check if a player has won the game"""
        for i in range(3):
            # Checking the horizontals
            if self.board[i*3:(i+1)*3].count(notation) == 3:
                return True
            
            # Checking the verticals
            if self.board[i::3].count(notation) == 3:
                return True
            
        if self.board[::4].count(notation) == 3:
            return True
        if self.board[2:7:2].count(notation) == 3:
            return True
    
    def check_draw(self):
        o_count = self.board.count('O')
        x_count = self.board.count('X')
        if o_count+x_count == 9:
            return True
        else:
            return False
        
        
            

            

    
