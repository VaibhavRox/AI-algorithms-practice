def is_safe(assignment,row,col):
    for r,c in assignment.items():
        if c==col:
            return False
        elif abs(r-row)==abs(c-col):          #diagonal
            return False
    return True

def backtrack(assignment):
    if len(assignment)==4:      #all queens placed
        return assignment
    row=len(assignment)
    for col in range(0,4):
        if is_safe(assignment,row,col):
            assignment[row]=col
            result=backtrack(assignment)
            if result:
                return result
            del assignment[row]         #delete the assignment
    return None

def print_board(solution):
    for r in range(0,4):
        row=""
        for c in range(0,4):
            if solution[r]==c:
                row+="Q"
            else:
                row+="_"
        print(row)
    print()

assignment={}
n=int(input("Enter number of preplaced queens(0-4):"))
for i in range(0,n):
    r=int(input("Enter row value to place the queen(0-3):"))
    c=int(input("Enter col value to place the queen(0-3):"))
    if r in assignment:
        print("A queen already placed in this place!")
        continue
    elif not is_safe(assignment,r,c):
        print("Invalid place!")
        continue
    else:
        assignment[r]=c
        if i==n-1:
            break
solution=backtrack(assignment)
if solution:
    print("solution exists!\n")
    print_board(solution)
else:
    print("No solution!")