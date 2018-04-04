import math

# define the indexes to search for a  win
ROWS = [[x,x+1,x+2] for x in (0,3,6)]
COLS = [[x,x+3,x+6] for x in (0,1,2)]
DIAGS = [[0,4,8],[2,4,6]]
UNITS = ROWS+COLS+DIAGS

# define named constants. The values don't matter, but the names are used in the code
XWINS, OWINS, TIE, CONTINUE = 1,-1,2,3
X = "X"
O = "O"

# define some helpful dictionaries
SCORE = {XWINS:1, OWINS:-1, TIE:0}
result_string = {XWINS: "X wins", OWINS: "O Wins", TIE: "Tie", CONTINUE: "Error"}
NEXT = {X:O, O:X}

# more useful constants
START_BOARD = "."*9
DEBUG = False

class Node:
    def __init__(self, board, last_move):
        self.board = board
        self.last_move = last_move
        self.score = -1
        self.player = "X"
    # a class that holds board, player, move, score info for minmax tree
    # FILL THIS IN

def print_board(board):
    print("%s\n%s\n%s" % ( board[:3],board[3:6],board[6:]))

def goal_test(board):
    for S in UNITS:
        if all([board[j]==X for j in S]): return XWINS
        if all([board[j]==O for j in S]): return OWINS
    if board.find(".") == -1:
        return TIE
    return CONTINUE

def get_moves(board, player):
    return [x for x in range(len(board)) if board[x]=="."]

def make_move(board, move, player):
    assert(board[move]==".")
    return board[:move]+player+board[move+1:]

def minimax(node, player):
    # n is the root node of the subtree to search
    # player is current player (X or O)
    # depth is just for debugging
    # returns the NODE which is a child of N with the best score for player
    # Fill this in!
    result = goal_test(node.board)
    if result != CONTINUE:
        node.score = SCORE[result]
        return node

    children = []
    poss = get_moves(node.board, player)
    for i in poss:
        board = make_move(node.board, i, player)
        c = Node(board, i)
        children.append(c)
    for c in children:
         c.score = minimax(c, NEXT[player])

    if player == "X": return max(children, key = lambda c: minimax(c, "O").score)
    if player == "O": return min(children, key=lambda c: minimax(c, "X").score)


def minimax_strategy(board, player):
    # calls minimax
    # makes board into a node
    # returns the MOVE (index from 0..8) contained in the node returned by minimax
    # note it always returns center square for the first move, as a speed-up
    if board==START_BOARD: return 4
    return minimax(Node(board, -1), player).last_move

def human_strategy(board, player):
    # asks human for a move (int from 0..8)
    # returns that move (integer)
    # does not check if move is valid
    move = int(input("Which move, %s? " % player))
    return move

def play_game(p1, p2):
    # p1 = X strategy (a function pointer / function name)
    # p2 = O strategy
    board = START_BOARD
    over = False
    player = X
    strategy = p1 #this is a function pointer!
    other = {X:O, O:X, p1:p2, p2:p1}

    while(not over):
        move = strategy(board, player) # works because p1 and p2 have the same parameter list (board, player)
        print("Player %s makes move %i" % (player, move))
        board = make_move(board, move, player)
        # does not check for valid moves!
        print_board(board)

        result = goal_test(board)
        player = other[player]
        strategy = other[strategy]
        over = (result != CONTINUE)
    print(result_string[result])


# Main plays AI vs AI
if __name__ == "__main__":
    play_game(minimax_strategy, minimax_strategy)