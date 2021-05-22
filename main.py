from Game import Game
from os import system, name
import os

def clear():
      
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    clear()
    game = Game()
    game.run_menu()
    clear()







if __name__ == '__main__':
    main()
    