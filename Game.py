from Board import Board
from Player import Player
from Bot import Bot

class Game:
    

    def __init__(self):
        self.gameover = False

    def run_menu(self):
        while not self.gameover:
            print('1. Singleplayer')
            print('2. Multiplayer')
            print('3. Exit')

            option = input()

            if option == '1':
                self.run_singleplayer()
            elif option == '2':
                self.run_multiplayer()
            elif option == '3':
                self.gameover = True
            else:
                print("Invalid input!")
        
    def run_multiplayer(self):
        player1 = Player.create_player()
        player2 = Player.create_player()
        print(player1.name, '-', player1.notation)
        print(player2.name, '-',player2.notation)
        board = Board()
        step = 1
        current_player = ''
        while not self.gameover:
            if step % 2 != 0:
                current_player = player1
            else:
                current_player = player2
            
            board.display()
            move = current_player.make_move(board.used)
            board.set_field(move, current_player.notation)

            if board.check_win(current_player.notation):
                board.display()
                print(f'Player {current_player.name} has won!')
                del player1
                del player2
                break
            if step == 9:
                print("Draw on the board!")
                del player1
                del player2
                break
            step+=1
        """Clean the game settings"""
        
    def run_singleplayer(self):
        while True:
            print('Choose the difficulty: ')
            print('1. Easy')
            print('2. Medium')
            print('3. Hard')
            print('4. Exit')

            diff = input()

            if diff == '1':
                self.play_with_bot('Easy')
                break
            elif diff == '2':
                self.play_with_bot('Medium')
                break
            elif diff == '3':
                self.play_with_bot('Hard')
                break
            elif diff == '4':
                break
            else:
                print("Invalid input!")

    def play_with_bot(self, diff):
        player = Player.create_player()
        bot = Bot(player.notation)
        board = Board()
        step = 1
        current_notation = ''
        while True:
            board.display()
            if step % 2 == 1:
                move = player.make_move(board.used)
                current_notation = player.notation
            if step % 2 == 0:
                current_notation = bot.notation
                if diff == 'Easy':
                    move = bot.play_easy_move(board.used)
                elif diff == 'Medium':
                    move = bot.play_medium_move(board)
                elif diff == 'Hard':
                    move = bot.play_hard_move(board)
                
            
            board.set_field(move, current_notation)
            
            if board.check_win(current_notation):
                board.display()
                if step % 2 == 1:
                    print(f"Player {player.name} has won!")
                elif step % 2 == 0:
                    print('Bot won!')

                del player
                break
            if step == 9:
                print("Draw on the board!")
                del player
                break
            step+=1