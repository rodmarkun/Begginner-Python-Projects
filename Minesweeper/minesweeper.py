import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        # Keep track of parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Create the board
        self.board = self.make_new_board()
        self.assign_values_to_board()

        # Initialize a set to keep track of uncovered locations
        self.dug = set() # If we dig at 0,0 then self.dug = {(0,0)}

    def make_new_board(self):
        # Construct a new board based on the dim size and num bombs
        # Generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # Plant bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                # There's already a bomb
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # Assign numbers (0-8) depending on adjacent bombs
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # If already a bomb, we don't want to calculate it
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
    
    def get_num_neighboring_bombs(self, row, col):
        # Let's iterate through each of the neighboring position and sum number of bombs
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size - 1, (row+1) + 1)):
            for c in range(max(0,col-1), min(self.dim_size - 1, (col+1) + 1)):
                if r == row and c == col:
                    # Original location, do not check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        
        return num_neighboring_bombs

    def dig(self, row, col):
        # Dig at that location
        # return True if succesful dig, False if bomb dug

        # Hit a bomb: Game Over
        # Dig at location with neighboring bombs: Finish dig
        # Dig at location with no neighboring bombs: Recursively dig neighbors

        self.dug.add((row, col)) # Keep track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row-1), min(self.dim_size - 1, (row+1) + 1)):
            for c in range(max(0,col-1), min(self.dim_size - 1, (col+1) + 1)):
                if (r, c) in self.dug:
                    continue # Don't dig where you've already dug
                self.dig(r, c)

        return True

    def __str__(self): # Check out what this does!
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if(row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # Put this together in a string
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


# Play the Game
def play(dim_size = 10, num_bombs = 10):
    # Step 1: Create board and plant the bombs
    board = Board(dim_size, num_bombs)
    # Step 2: Show the user the board and ask for where they want to dig

    # Step 3a: If location is a bomb, show game over message
    # Step 3b: If location is not a bomb, dig recursively until each square is next to a bomb
    # Step 4: Repeat 2 and 3 until there are no more places to dig (Victory)
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location")
            continue

        # If it is valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # Dug a bomb
            break

    if safe:
        print("You are victorious! Congratulations!")
    else:
        print("Sorry, game over :(")
        # Reveal whole board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()