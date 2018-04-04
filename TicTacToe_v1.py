#should have a separate method that alternates between calling min_max and asking the human for his input

class Node:
    def __init__(self, score, parent):
        self.score = score
        self.parent = parent        #will i ever use the parent?
        self.children = []
        if self.parent is None:         #don't really need depth?
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

board = ""      #should be a nine character string

def min_max(board, player):     #replaces the DFS
    if goal_test(board) is True:            #change this when you change goal_test to represent the options
        board.score = goal_test(board)
        return board
    if player == "MAX":
        board.children = make_moves(board, player)
        return max(board.children, key = lambda c: min_max(c, "MIN").score)
    if player == "MIN":
        return min(board.children, key = lambda c: min_max(c, "MAX").score)
    return None

def make_moves(board, player):      #should return a list of all the possible boards that could come with the next move
    return None

def goal_test(board):               #should return one of the four options (as a String?): X won, O won, Tie, Still going
    return None

def find_valid_moves(board, player):    #should return a list of indices to all open squares to use in make_moves
    return None                         #maybe i don't need to do this? could just calculate this in make_moves