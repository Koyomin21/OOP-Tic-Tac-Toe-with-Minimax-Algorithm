import random
from Board import Board

class Bot:

    def __init__(self, player_notation):
        self.name = 'Bot'
        self.player_notation = player_notation
        self.notation = ''
        if self.player_notation == 'X':
            self.notation = 'O'
        else:
            self.notation = 'X'

    def play_easy_move(self, used):
        """Easy bot makes random moves regardless what happens on the board"""
        move = str(random.randint(1, 9))
        while move in used:
            print('Doing move')
            move = str(random.randint(1, 9))
            print(move)
        return move

    def play_medium_move(self, board):
        """Medium bot makes random moves, however if there is a risk to lose or an opportunity to win, it will do a proper move"""
        move = self._optimal_move(board)
        if move is None:
            print("The random move will be choosen")
            while move in board.used or move is None:
                move = str(random.randint(1, 9))
        
        print("Bot's move: ", move)
        return move


    def play_hard_move(self, board):
        """Hard bot cannot be beaten. The best case for player is the draw. Uses minimax algorithm"""
        bestScore = -1000
        bestMove = 0

        possible_moves = [i for i in board.board if not(i == self.notation) and not(i == self.player_notation)]
        for i in possible_moves:
            board.set_field(i, self.notation)
            score = self._minimax(board, 0, False)
            board.remove_field(i)

            if score > bestScore:
                bestScore = score
                bestMove = i
        
        return bestMove
    
    def _optimal_move(self, board):
        """Optimal move either wins the game or does not allow to lose it"""
        for i in range(3):
            horizontal = board.board[i*3:(i+1)*3]
            print('Horizontal: ', horizontal)
            move = self._check_row(horizontal)
            if move:
                return move
            
            vertical = board.board[i::3]
            print('Vertical: ', vertical)
            move = self._check_row(vertical)
            if move:
                return move

        diagonal_prime = board.board[::4]
        move = self._check_row(diagonal_prime)
        if move:
            return move

        diagonal_secon = board.board[2:7:2]
        move = self._check_row(diagonal_secon)
        if move:
            return move
        
        return None
    
    def _check_row(self, row):
        if row.count(self.notation) == 2:
            for i in row:
                if not (i == self.notation) and not (i == self.player_notation) :
                    print('To win move:', row)
                    return str(i)
        if row.count(self.player_notation) == 2:
            for i in row:
                if not (i == self.notation) and not (i == self.player_notation) :
                    print('Not to lose move ', row)
                    return str(i)

        return None
    
                
    def _minimax(self, board, depth, isMaximizing):
        """Minimax algorithm. Calculates every possible move and analyzes the state on the board"""
        if board.check_win(self.notation):
            return 100

        elif board.check_win(self.player_notation):
            return -100

        elif board.check_draw():
            return 0
        
        if isMaximizing:
            bestScore = -1000

            possible_moves = [i for i in board.board if not(i == self.notation) and not(i == self.player_notation)]
            for i in possible_moves:
                board.set_field(i, self.notation)
                score = self._minimax(board, depth+1, False)
                board.remove_field(i)

                if score > bestScore:
                    bestScore = score

            return bestScore

        else:
            bestScore = 800

            possible_moves = [i for i in board.board if not(i == self.notation) and not(i == self.player_notation)]
            for i in possible_moves:
                board.set_field(i, self.player_notation)
                score = self._minimax(board, depth+1, True)
                board.remove_field(i)


                if score < bestScore:
                    bestScore = score

            return bestScore
            



