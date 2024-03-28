# Day 84 Project: Text-Based Tic-Tac Toe

## Concept

This program simulates the Tic-Tac Toe game as a text-based implementation. Currently, it works for
two players. Upon execution, the program is able to provide rules for the game, if desired by the user,
and keeps track of the board inputs.

The game asks for input in the format `row,column` as numbers (e.g., 1,2 or 3,3). It checks if the
position is valid (within the matrix's range and an unoccupied space) and then updates the board,
prompting the other player for their input. After each input, the game checks if there is any
winner or if there is a draw, then finishes its execution after a message status.

In future versions, this program might include the option to play against the PC.