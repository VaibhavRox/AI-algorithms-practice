import math

board=[" " for _ in range(9)]

#function to print board
def print_board():
    #display as 3x3 grid
    for i in range(0,9,3):
        row=board[i:i+3]
        print(f"|{row[0]}|{row[1]}|{row[2]}|")

#function to check winner
def check_winner(brd):
    win_patter=[
        [0,1,2],[3,4,5],[6,7,8],    #rows
        [0,3,6],[1,4,7],[2,5,8],    #columns
        [0,4,8],[2,4,6]
    ]
    #loop through each pattern and see if that place is occupied by the same symbol in board
    for ptrn in win_patter:
        if brd[ptrn[0]]==brd[ptrn[1]]==brd[ptrn[2]]!=" ":
            return brd[ptrn[0]]
    if " " not in brd:
        return "Tie"
    return None     #no winner yet

#function to check the available spots to make moves
def available_moves(brd):
    moves=[]
    for i in range(len(brd)):
        if brd[i]==" ":
            moves.append(i)
    return moves

#function of minimax
def minimax(brd,is_maximizing):
    #check whether any winner currently
    result=check_winner(brd)
    if result=="X":
        return -1
    elif result=="O":
        return 1    #favour AI winning
    elif result=="Tie":
        return 0
    #otherwise make moves
    if is_maximizing:       #true for AI turn, false for human turn
        best_score=-math.inf
        for move in available_moves(brd):
            brd[move]="O"   #try a move
            score=minimax(brd,False)
            brd[move]=" "   #undo move 
            best_score=max(score,best_score)
        return best_score
    else:                   #humans move
        best_score=math.inf
        for move in available_moves(brd):
            
            brd[move]="X"   #try a move
            score=minimax(brd,True)
            brd[move]=" "   #undo move 
            best_score=min(score,best_score)
        return best_score

#define a function to find best move for AI
def best_move():
    best_score=-math.inf
    move_chosen=None
    for move in available_moves(board):
        board[move]="O"     #try move
        score=minimax(board,False)
        board[move]=" "
        if score>best_score:
            best_score=score
            move_chosen=move
    return move_chosen

#main part
print("-------------TicTacToe with AI-------------")
print_board()
while True:
    move=int(input("Enter your move as index (0-8):"))
    if board[move]!=" ":        #check if valid space
        print("Invalid space, already occupied")
        continue
    board[move]="X"
    if check_winner(board):
        print(f"Game Over ! Result:{check_winner(board)}")
        break
    comp=best_move()
    board[comp]="O"
    print("\n AI made its move")
    print_board()

    if check_winner(board):
        print(f"Game Over ! Result:{check_winner(board)}")
        break

    