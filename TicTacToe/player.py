import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, try again")

        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # Start with a random move
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # Firstly we want to check if the previous move is a winner
        # This is our base case
        if state.current_winner == other_player:
            # We should return position and score because we need to keep track of the score
            # for minimax to work
            return {'position' : None,
                'score' : 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                    state.num_empty_squares() + 1)
            }
        elif not state.empty_squares(): # No empty squares
            return {'position' : None, 'score' : 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # Each score should maximize
        else:
            best = {'position': None, 'score': math.inf} # Each score should minimize
        
        for possible_move in state.available_moves():
            # Step 1: Make a move, try that spot
            state.make_move(possible_move, player)
            # Step 2: Recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player) # Alternate players
            # Step 3: Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # Step 4: Update dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # Replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score # Replace best
        
        return best
                