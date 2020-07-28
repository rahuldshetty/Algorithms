'''
Simple program for backtracking basics

Bot can start at top left (0,0) and have to move until (r-1,c-1) where r->#rows and c->#columns.
Only 2 actions are allowed. One to move on right and other down.
'''

board = [
    [1,1,1],
    [1,1,1],
    [1,1,0],
    [0,1,1]
]

start = (0,0)
r = len(board)
c = len(board[0])
end = (r-1, c-1)

def get_route(board, matrix, pos, end):
    # x -> row; y -> column
    x,y = pos
    if pos == end and board[x][y] == 1:
        matrix[x][y] = 1
        return True
    elif board[x][y] == 1:
        if y + 1 <= c-1:
            # try to move right
            matrix[x][y + 1] = 1
            if get_route(board, matrix, (x,y+1), end) == True:
                return True
            matrix[x][y + 1] = 0
        if x + 1 <= r-1:
            # try to move down
            matrix[x + 1][y] = 1
            if get_route(board, matrix, (x+1,y), end) == True:
                return True
            matrix[x + 1][y] = 0
    return False

initial_matrix = [ [0]*(c) for _ in range(r) ]

initial_matrix[start[0]][start[1]] = 1

if get_route(board, initial_matrix, start, end) == True:
    print("Success")
    for row in initial_matrix:
        print(row)
else:
    print("Not Possible")