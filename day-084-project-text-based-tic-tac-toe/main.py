from board import Board
from player import Player

TITLE = r"""
  _____ _         _____            _____          
 |_   _(_) ___   |_   _|_ _  ___  |_   _|__   ___ 
   | | | |/ __|____| |/ _` |/ __|   | |/ _ \ / _ \
   | | | | (_|_____| | (_| | (__    | | (_) |  __/
   |_| |_|\___|    |_|\__,_|\___|   |_|\___/ \___|
   """

print(TITLE)
view_rules = input("Welcome to the Tic-Tac Toe game. Would you like an overview of the rules (y/n)? ")
if view_rules == 'y':
    print("\n1. The game is played on a grid that's 3 squared by 3 squares;\n"
          "2. You are X, your friend (or the computer) is O. Players take turns putting their marks in empty "
          "squares;\n"
          "3. The first player to get 3 of their marks in a row (up, down, across or diagonally) is the winner;\n"
          "4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a "
          "tie.\n")


board = Board()
p1 = Player("Player 1", "X")
p2 = Player("Player 2", "O")

n_players = int(input("How many players will play the game (1/2)? "))
if n_players == 1:
    p2.toggle_ai()

turn = 1
current_player = p1


def is_valid_move(position):
    """Return if position is valid or not (within matrix range and unmarked space)."""
    r = int(position[0]) - 1
    c = int(position[2]) - 1

    if (0 <= r <= 2) and (0 <= c <= 2) and board.grid[r][c] == '_':
        return True
    else:
        return False


def check_game():
    """Return 1 if there is a winner. Return 2 if it is a draw. Otherwise, return 0."""

    # Check if there is a combination in each row
    for r in board.grid:
        if r[0] != '_' and r[0] == r[1] and r[1] == r[2]:
            return 1

    # Check if there is a combination in each column
    for i in range(3):
        if board.grid[0][i] != '_' and board.grid[0][i] == board.grid[1][i] and board.grid[1][i] == board.grid[2][i]:
            return 1

    # Check if there is a combination in each diagonal
    if board.grid[0][0] != '_' and board.grid[0][0] == board.grid[1][1] and board.grid[1][1] == board.grid[2][2]:
        return 1
    if board.grid[0][2] != '_' and board.grid[0][2] == board.grid[1][1] and board.grid[1][1] == board.grid[2][0]:
        return 1

    # Check if all spaces are marked and there is no winner
    if all('_' not in line for line in board.grid):
        return 2

    return 0


is_game_over = False
while not is_game_over:
    if turn == 9:
        is_game_over = True

    print(f"\n========== TURN {turn} ==========\nPLAYER 1: {p1.score}     PLAYER 2: {p2.score}")
    for row in board.grid:
        print(row)
    print(f"CURRENT PLAYER: {current_player.name} ({current_player.mark})")

    if current_player == p2 and p2.is_ai is True:
        pos = p2.place_mark_as_ai()
        while not is_valid_move(pos):
            pos = p2.place_mark_as_ai()
    else:
        pos = input("Place mark on row,column (example: 2,1 marks the position on row 2, column 1): ")

    while not is_valid_move(pos):
        pos = input("Position invalid. Place mark on row,column (example: 2,1 marks the position on row 2, column 1): ")

    board.grid[int(pos[0]) - 1][int(pos[2]) - 1] = current_player.mark

    if check_game() == 1:
        for row in board.grid:
            print(row)
        is_game_over = True
        print(f"""
        ===============================================
        GAME OVER !!! WINNER: {current_player.name} !!!
        ===============================================
""")
    elif check_game() == 2:
        for row in board.grid:
            print(row)
        is_game_over = True
        print(f"""
        ======================
        GAME OVER !!! DRAW !!!
        ======================
""")
    else:
        turn += 1
        current_player = p2 if current_player == p1 else p1
