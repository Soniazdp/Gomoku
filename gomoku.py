import random

def is_empty(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == " ":
                continue
            else:
                return False
    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    if d_y == 0 and d_x == 1:  # direction is left-to-right
        if x_end == len(board) - 1 and x_end - length + 1 == 0:  # bounded by the board
            return "CLOSED"
        elif x_end == len(board - 1): # the end is bounded by the board
            if board[y_end][x_end - length ] == " ":
                return "SEMIOPEN"
            elif board[y_end][x_end - length ] != " ":
                return "CLOSED"
        elif x_end - length + 1 == 0: # the start is bounded by the board
            if board[y_end][x_end + 1] == " ":
                return "SEMIOPEN"
            elif board[y_end][x_end + 1] != " ":
                return "CLOSED"
        else: # not bounded on either side
            if board[y_end][x_end - length ] == " " and board[y_end][x_end + 1] == " ":
                return "OPEN"
            elif board[y_end][x_end - length ] == " " and board[y_end][x_end + 1] != " ":
                return "SEMIOPEN"
            elif board[y_end][x_end - length ] != " " and board[y_end][x_end + 1] == " ":
                return "SEMIOPEN"
            elif board[y_end][x_end - length ] != " " and board[y_end][x_end + 1] != " ":
                return "CLOSED"

    elif d_y == 1 and d_x == 0:  # direction is top-to-bottom
        if y_end == len(board) - 1 and y_end - length + 1 == 0: # bounded by the board on both sides
            return "CLOSED"
        elif y_end == len(board) - 1: # the end is bounded by the board
            if board[y_end - length][x_end] == " ":
                return "SEMIOPEN"
            elif board[y_end - length][x_end] != " ":
                return "CLOSED"
        elif y_end - length + 1 == 0: # the start is bounded by the board
            if board[y_end + 1][x_end] == " ":
                return "SEMIOPEN"
            elif board[y_end + 1][x_end] != " ":
                return "CLOSED"
        else: # not bounded on either side
            if board[y_end - length][x_end] == " " and board[y_end + 1][x_end] == " ":
                return "OPEN"
            elif board[y_end - length][x_end] == " " and board[y_end + 1][x_end] != " ":
                return "SEMIOPEN"
            elif board[y_end - length][x_end] != " " and board[y_end + 1][x_end] == " ":
                return "SEMIOPEN"
            elif board[y_end - length][x_end] != " " and board[y_end + 1][x_end] != " ":
                return "CLOSED"

    elif d_y == 1 and d_x == 1:  # direction is upper left to lower right
        if (y_end == len(board) - 1 or x_end == len(board) - 1) and (y_end - length + 1 == 0 or x_end - length + 1 == 0):   # bounded by the board on both sides
            return "CLOSED"
        elif y_end == len(board) - 1 or x_end == len(board) - 1: # the end is bounded by the board
            if board[y_end - length][x_end - length] == " ":
                return "SEMIOPEN"
            elif board[y_end - length][x_end - length] != " ":
                return "CLOSED"
        elif y_end - length + 1 == 0 or x_end - length + 1 == 0: # the start is bounded by the board
            if board[y_end + 1][x_end + 1] == " ":
                return "SEMIOPEN"
            elif board[y_end + 1][x_end + 1] != " ":
                return "CLOSED"
        else:
            if board[y_end - length][x_end - length] == " " and board[y_end + 1][x_end + 1]  == " ":
                return "OPEN"
            elif board[y_end - length][x_end - length] != " " and board[y_end + 1][x_end + 1]  == " ":
                return "SEMIOPEN"
            elif board[y_end - length][x_end - length] == " " and board[y_end + 1][x_end + 1]  != " ":
                return "SEMIOPEN"
            elif board[y_end - length][x_end - length] != " " and board[y_end + 1][x_end + 1]  != " ":
                return "CLOSED"


    elif d_y == 1 and d_x == -1:  # direction is upper right to lower left
        if (y_end == len(board) - 1 or x_end == 0) and (y_end - length + 1 == 0 or x_end - length + 1 == len(board) - 1):   # bounded by the board on both sides
            return "CLOSED"
        elif y_end == len(board) - 1 or x_end == 0: # the end is bounded by the board
            if board[y_end - length][x_end + length] == " ":
                return "SEMIOPEN"
            elif board[y_end - length][x_end + length] != " ":
                return "CLOSED"
        elif y_end - length + 1 == 0 or x_end - length + 1 == len(board) - 1: # the start is bounded by the board
            if board[y_end + 1][x_end - 1] == " ":
                return "SEMIOPEN"
            elif board[y_end + 1][x_end - 1] != " ":
                return "CLOSED"
        else:
            if board[y_end - length][x_end + length] == " " and board[y_end + 1][x_end - 1]  == " ":
                return "OPEN"
            elif board[y_end - length][x_end + length] != " " and board[y_end + 1][x_end - 1]  == " ":
                return "SEMIOPEN"
            elif board[y_end - length][x_end + length] == " " and board[y_end + 1][x_end - 1]  != " ":
                return "SEMIOPEN"
            elif board[y_end - length][x_end + length] != " " and board[y_end + 1][x_end - 1]  != " ":
                return "CLOSED"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count, semi_open_seq_count = 0, 0

    # extract sequences of squares of colour col

    y, x = y_start, x_start
    sequences = []
    while y < len(board) and x < len(board):
        # detect start of a sequence
        if (x == 0 or y == 0) and d_x != -1:
            if board[y][x] == col:
                sequences.append([x, y])
        elif (x == len(board) - 1 or y == 0) and d_x == -1:
            if board[y][x] == col:
                sequences.append([x, y])
        else:
            if board[y][x] == col and board[y - d_y][x - d_x] != col:
                sequences.append([x, y])

        # detect end of a sequence
        if (x == len(board) -1 or y == len(board)-1) and d_x != -1:
            if board[y][x] == col:
                sequences.append([x, y])
        elif (x == 0 or y == len(board) - 1) and d_x == -1:
            if board[y][x] == col:
                sequences.append([x, y])
        else:
            if (board[y][x] == col and board[y + d_y][x + d_x] != col):
                sequences.append([x, y])

        y += d_y
        x += d_x


    # recognize sequences with length length
    sequences1 = []
    for i in range(0, len(sequences), 2):
        start, end = sequences[i], sequences[i + 1]
        if end[0] - start[0] == (length - 1) * d_x and end[1] - start[1] == (length - 1) * d_y:
            sequences1.append(start)
            sequences1.append(end)


    # recognize semi-open and open sequences
    for i in range(0, len(sequences1), 2):
        start, end = sequences1[i], sequences1[i + 1]

        # start of the sequence
        # the sequence is bounded by the edge
        if (start[0] == 0 or start[1] == 0) and d_x != -1:
            start_stu = "CLOSED"
        elif (start[0] == len(board) - 1 or start[1] == 0) and d_x == -1:
            start_stu = "CLOSED"

        else:  # the sequence isn't bounded by the edge
            if board[start[1] - d_y][start[0] - d_x] == " ":
                start_stu = "OPEN"
            elif board[start[1] - d_y][start[0] - d_x] != " ":
                start_stu = "CLOSED"

        # end of the sequence
        # the sequence is bounded by the edge
        if (end[0] == len(board) - 1 or end[1] == len(board) - 1) and d_x != -1:
            end_stu = "CLOSED"
        elif (end[0] == 0 or end[1] == len(board) - 1) and d_x == -1:
            end_stu = "CLOSED"

        else:  # the sequence isn't bounded by the edge
            if board[end[1] + d_y][end[0] + d_x] == " ":
                end_stu = "OPEN"
            elif board[end[1] + d_y][end[0] + d_x] != " ":
                end_stu = "CLOSED"

        if end_stu == "CLOSED" and start_stu == "CLOSED":
            pass
        elif end_stu == "OPEN" and start_stu == "OPEN":
            open_seq_count += 1
        else:
            semi_open_seq_count += 1

    return (open_seq_count, semi_open_seq_count)


def create_collections(board):
    # extract the "rows" through the entire board
    # extract row "rows"
    lor = board

    # extract top-to-bottom "rows"
    loc = []
    for column in range(len(board)):
        loc1 = []
        for row in range(len(board)):
            loc1.append(board[row][column])
        loc.append(loc1)

    # extract "rows" from upper-left to lower-right
    loul = []
    for column in range(len(board) - 1, -1, -1):
        loul1 = []
        row = 0
        while column < len(board) and row < len(board):
            loul1.append(board[row][column])
            column += 1
            row += 1
        loul.append(loul1)
    for row in range(1, len(board), 1):
        column = 0
        loul2 = []
        while column < len(board) and row < len(board):
            loul2.append(board[row][column])
            column += 1
            row += 1
        loul.append(loul2)

    # extract "rows" from upper-right to lower-left
    lour = []
    for column in range(0, len(board), 1):
        lour1 = []
        row = 0
        while column >= 0 and row < len(board):
            lour1.append(board[row][column])
            column -= 1
            row += 1
        lour.append(lour1)
    for row in range(1, len(board), 1):
        lour2 = []
        column = len(board) - 1
        while column >= 0 and row < len(board):
            lour2.append(board[row][column])
            column -= 1
            row += 1
        lour.append(lour2)
    return (lor, loc, loul, lour)


def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    column_col = create_collections(board)[1]
    col1 = create_collections(board)[2]
    col2 = create_collections(board)[3]

    for i in (board, column_col, col1, col2):
        for row in i:
            copy = ''
            copy = copy.join(row)
            col_length = col*length
            while col_length in copy:
                                        # if the sequence is blocked by both edges:
                if copy.index(col_length) == 0 and copy.index(col_length) + length - 1 >= len(copy)-1:
                    pass
                                        # if start of the sequence is blocked by the board:
                elif copy.index(col_length) == 0:
                    if copy[copy.index(col_length) + length] == " ": # edge/space
                        semi_open_seq_count += 1
                    elif copy[copy.index(col_length) + length] != " ": # edge/non-space
                        pass
                                        # if end of the sequence is blocked by the board:
                elif copy.index(col_length) + length - 1 >= len(copy)-1:
                    if copy[copy.index(col_length) - 1] == " " : # space/edge
                        semi_open_seq_count += 1
                    elif copy[copy.index(col_length) - 1] != " ": # non-space/edge
                        pass
                                        # if the sequence is not blocked by edges:
                elif copy.index(col_length) > 0 and copy.index(col_length) + length - 1 < len(copy)-1:
                    if copy[copy.index(col_length) + length ] == "p" or copy[copy.index(col_length)-1] == "p":
                                                                # if the sequence is not complete
                        pass
                    elif copy[copy.index(col_length) + length ] != " " and copy[copy.index(col_length)-1] != " ":
                                                                # the sequence is bounded by two non-space
                        pass
                    elif copy[copy.index(col_length) - 1] == " " and copy[copy.index(col_length) + length] != " " and copy[copy.index(col_length) + length] != col:
                                                                # space/non-space
                        semi_open_seq_count += 1

                    elif copy[copy.index(col_length) + length] == " " and copy[copy.index(col_length) - 1] != " " and copy[copy.index(col_length) - 1] != col:
                                                                # non-space/space
                        semi_open_seq_count += 1

                    elif copy[copy.index(col_length) + length] == " " and copy[copy.index(col_length) - 1] == " " :
                                                                # space/space
                        open_seq_count += 1

                # change recorded sequences to spaces
                copy = copy[ :copy.index(col_length)] + "p"*length + copy[(copy.index(col_length) + length):]

    return (open_seq_count, semi_open_seq_count)


### search_max
def get_empty(board):
    sparse_board = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                sparse_board.append([j, i])
    return sparse_board


def replicate_board(board):
    board1 = []
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            row.append(board[i][j])
        board1.append(row)

    return board1


def search_max(board):
    sparse_board = get_empty(board)

    optimal_coord = []
    max_score = 0
    score1 = 0
    for coord in sparse_board:
        new_board = replicate_board(board)
        new_board[coord[1]][coord[0]] = "b"

        score1 = score(new_board)

        if optimal_coord == []:
            optimal_coord = [coord]
            max_score = score1

        else:
            if score1 < max_score:
                pass
            elif score1 == max_score:
                optimal_coord.append(coord)
            elif score1 > max_score:
                optimal_coord = [coord]
                max_score = score1

    if len(optimal_coord) == 1:
        move_y, move_x = optimal_coord[0][1], optimal_coord[0][0]
    elif len(optimal_coord) > 1:
        choice = int(random.random() * len(optimal_coord))
        move_y, move_x = optimal_coord[choice][1], optimal_coord[choice][0]

    return (move_y, move_x)



## Do not modify
def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


### is_win
def col_is_win1(lor, loc, loul, lour, col):
    win = []
    sequences = []

    # check lor
    for row in range(len(lor)):
        x = 0
        if lor[row] == [" "] * (len(lor[row])):
            continue
        else:
            while x < len(lor[row]):
                # detect start of a sequence
                if x == 0:
                    if lor[row][x] == col:
                        sequences.append([row, x])
                elif x > 0:
                    if lor[row][x] == col and lor[row][x - 1] != col:
                        sequences.append([row, x])

                # detect end of a sequence
                if x == len(lor[row]) - 1:
                    if lor[row][x] == col:
                        sequences.append([row, x])
                elif x < len(lor[row]) - 1:
                    if lor[row][x] == col and lor[row][x + 1] != col:
                        sequences.append([row, x])
                x += 1

    # check loc
    for row in range(len(loc)):
        x = 0
        if loc[row] == [" "] * (len(loc[row])):
            continue
        else:
            while x < len(loc[row]):
                # detect start of a sequence
                if x == 0:
                    if loc[row][x] == col:
                        sequences.append([row, x])
                elif x > 0:
                    if loc[row][x] == col and loc[row][x - 1] != col:
                        sequences.append([row, x])

                # detect end of a sequence
                if x == len(loc[row]) - 1:
                    if loc[row][x] == col:
                        sequences.append([row, x])
                elif x < len(loc[row]) - 1:
                    if loc[row][x] == col and loc[row][x + 1] != col:
                        sequences.append([row, x])
                x += 1

    # check loul
    for row in range(len(loul)):
        x = 0
        if loul[row] == [" "] * (len(loul[row])):
            continue
        else:
            while x < len(loul[row]):
                # detect start of a sequence
                if x == 0:
                    if loul[row][x] == col:
                        sequences.append([row, x])
                elif x > 0:
                    if loul[row][x] == col and loul[row][x - 1] != col:
                        sequences.append([row, x])

                # detect end of a sequence
                if x == len(loul[row]) - 1:
                    if loul[row][x] == col:
                        sequences.append([row, x])
                elif x < len(loul[row]) - 1:
                    if loul[row][x] == col and loul[row][x + 1] != col:
                        sequences.append([row, x])
                x += 1

    # check lour
    for row in range(len(lour)):
        x = 0
        if lour[row] == [" "] * (len(lour[row])):
            continue
        else:
            while x < len(lour[row]):
                # detect start of a sequence
                if x == 0:
                    if lour[row][x] == col:
                        sequences.append([row, x])
                elif x > 0:
                    if lour[row][x] == col and lour[row][x - 1] != col:
                        sequences.append([row, x])

                # detect end of a sequence
                if x == len(lour[row]) - 1:
                    if lour[row][x] == col:
                        sequences.append([row, x])
                elif x < len(lour[row]) - 1:
                    if lour[row][x] == col and lour[row][x + 1] != col:
                        sequences.append([row, x])
                x += 1

    for pair_start in range(0, len(sequences), 2):
        start, end = sequences[pair_start][1], sequences[pair_start + 1][1]
        if (end - start) >= 4:
            win.append(True)
        elif (end - start) < 4:
            win.append(False)

    if win == []:
        return False
    elif True in win:
        return True
    else:
        return False


def is_full(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] != " ":
                continue
            else:
                return False
    return True




def is_win(board):
    # determine if "b" or "w" wins
    lor = create_collections(board)[0]
    loc = create_collections(board)[1]
    loul = create_collections(board)[2]
    lour = create_collections(board)[3]

    w_win = col_is_win1(lor, loc, loul, lour, "w")
    b_win = col_is_win1(lor, loc, loul, lour, "b")

    if w_win == True and b_win == False:
        return "White won"
    elif w_win == False and b_win == True:
        return "Black won"
    elif w_win == False and b_win == False:
        return "Continue playing"

    elif is_full(board) == True:
        return "Draw"


## Do not modify
def print_board(board):
    s = "*"
    for i in range(len(board[0]) - 1):
        s += str(i % 10) + "|"
    s += str((len(board[0]) - 1) % 10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0]) - 1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0]) - 1])

        s += "*\n"
    s += (len(board[0]) * 2 + 1) * "*"

    print(s)


## Do not modify
def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "] * sz)
    return board


## Do not modify
def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i) 
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


### Do not modify
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


## Do not modify
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


##### Tests

def test_is_empty():
    board = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def test_is_bounded():
    board = make_empty_board(8)
    x = 5
    y = 1
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5
    y = 1
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0, x, length, d_y, d_x) == (1, 0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")


def test_detect_rows():
    board = make_empty_board(8)
    x = 5
    y = 1
    d_x = 0
    d_y = 1
    length = 3
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col, length) == (1, 0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")


def test_search_max():
    board = make_empty_board(8)
    x = 5
    y = 0
    d_x = 0
    d_y = 1
    length = 4
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6
    y = 0
    d_x = 0
    d_y = 1
    length = 4
    col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4, 6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")


def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()


def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5 
    x = 2 
    d_x = 0 
    d_y = 1 
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)


if __name__ == '__main__':
    test_detect_row()
    test_detect_rows()
    test_is_bounded()
    test_is_empty()
    test_search_max()
    some_tests()

    board = make_empty_board(8)
    x = 5 
    y = 0 
    d_x = 0 
    d_y = 1 
    length = 4 
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6 
    y = 0 
    d_x = 0 
    d_y = 1 
    length = 4 
    col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    new_board = replicate_board(board)
    new_board[1][7] = "b"
    print_board(new_board)
    score(new_board)

    board = make_empty_board(8)
    board[2][2] = "w"
    y = 3 
    x = 2 
    d_x = 0 
    d_y = 1 
    length = 5
    put_seq_on_board(board, y, x, d_y, d_x, length, 'b')
    print_board(board)
    score(board)
    search_max(board)
    if is_win(board) == "Black won":
        print("PASSSSSSSSS")
    else:
        print("EPIC FAIL :(")
    
        # Expected output:
        # *0|1|2|3|4|5|6|7*
        # 0 | | | | | | | *
        # 1 | | | | | | | *
        # 2 | |w| | | | | *
        # 3 | |b| | | | | *
        # 4 | |b| | | | | *
        # 5 | |b| | | | | *
        # 6 | |b| | | | | *
        # 7 | |b| | | | | *
        # *****************
        # PASSSSSSSSS