# AI Engine for Gomoku

This project designs an AI engine for the game Gomoku, where users are aimed to place a horizontal, vertical or diagonal sequence of 5 stones on a 8 x 8 board, when alternatively placing a stone on an empty space. The game follows all the rules presented in the page https://en.wikipedia.org/wiki/Gomoku. 

The file `gomoku.py` contains the following primary functions:

- `print_board`: prints out the game board.

- `is_empty`: checks if the current board is empty (i.e., no stone on the board).

- `is_bounded`: checks the status of the given sequence and report if it is OPEN, SEMIOPEN, or CLOSED.

- `search_max`: advises on what the optimal move for Black (which is the computer) is.

- `detect_row`: returns the number of OPEN and SEMI-OPEN sequences of the chosen color that are contained, given the *direction*, *start* and *end* of a sequence

- `detect_rows`: different from the function `detect_row`, it searches the number of OPEN and SEMI-OPEN sequences of the chosen color that present in the **entire** board. 

- `analysis`: computes the number of OPEN and SEMI-OPEN sequences of both colors in the **entire** board.

- `is_win`: returns the current status of the game if either of the player wins, a draw is reached, or they should continue playing.




## Credits 
The starter code of this project is provided by Michael Guerzhoy, based on which the full functionality of the AI engine is built by Bonnie Luo and Sonia Zeng in 2020 Fall.
