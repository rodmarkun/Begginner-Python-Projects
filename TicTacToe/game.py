import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range (9)] # 3x3 Board
        self.current_winner = None # Keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Check row
        row_index = square // 3
        row = self.board[row_index*3 : (row_index + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column 
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4 ,8]] # Left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4 ,6]] # Right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game = True):
    # Returns letter of winner or None for a tie
    if print_game:
        game.print_board_nums()


    letter = 'X' # Starting letter
    # Iterate while the game still has empty squares
    # When there's a winner we'll return and break the loop
    while game.empty_squares():
        # Get the move from the appropiate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # Just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter


            # Alternate letters after move
            letter = 'O' if letter == 'X' else 'X'

        # Tiny break
        time.sleep(0.8)

    if print_game:
        print("It's a tie!")
        
if __name__ == '__main__':
      x_player = HumanPlayer('X')
      o_player = GeniusComputerPlayer('O')
      t = TicTacToe()
      play(t, x_player, o_player, print_game = True)