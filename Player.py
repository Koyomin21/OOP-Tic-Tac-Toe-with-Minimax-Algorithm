class Player:
    amount = 0
    used_notations = []

    def __init__(self, name, notation):
        self.name = name
        self.notation = notation


    @classmethod
    def create_player(cls):
        cls.amount+=1

        while True:
            print(f"Enter the name of the player {cls.amount}: ")
            name = input()
            if len(name.strip()) < 2:
                print("Your nickname should be at least two characters")
                continue
            else:
                break


        while True:
            if cls.amount == 1:
                print("Choose the notation: ")
                print("1. X")
                print("2. O")
                notation = input()
            else:
                if 'X' in cls.used_notations:
                    notation = '2'
                else:
                    notation = '1'
            
            if notation == '1':
                notation = 'X'
            elif notation == '2':
                notation = 'O'
            else:
                print('Invalid input!')
                continue
            cls.used_notations.append(notation)
            break

        return cls(name, notation)
    
    def make_move(self, used):
        while True:
            print(self.name + ', your turn!')
            move = input()

            if move not in ['1','2','3','4','5','6','7','8','9']:
                print("Wrong Input!")
                continue
            elif move in used:
                print("This field is already taken!")
                continue
            else:
                break
            
        return move

    def __del__(self):
        # print('Destructor called!')
        Player.amount = 0
        Player.used_notations.clear()
