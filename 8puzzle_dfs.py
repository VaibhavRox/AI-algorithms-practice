def find_zeros(state):
    for i in range(0,3):
        for j in range(0,3):
            if state[i][j]==0:
                return i,j

#generate neighbours
def get_neighbours(state):
    neighbours=[]
    r,c=find_zeros(state)
    directions={
        'Up':(-1,0),
        'Down':(1,0),
        'Left':(0,-1),
        'Right':(0,1)
    }
    for move,(dr,dc) in directions.items():
        nr,nc=r+dr,c+dc
        if 0<=nr<3 and 0<=nc<3:     #checking if valid move
            new_state=[row[:] for row in state] 
            new_state[r][c],new_state[nr][nc]=new_state[nr][nc],new_state[r][c]
            #append to neighbours
            neighbours.append((new_state,move))
    return neighbours

#define dfs
def dfs(start,goal,max_depth=10):
    #initialize stack with start, path, and depth
    stack=[(start,[],0)]
    visited=set()
    while stack:
        state,path,depth=stack.pop()
        hash_state=tuple(tuple(row) for row in state)
        #check if goal
        if hash_state in visited:
            continue
        visited.add(hash_state)
        if state==goal:
            return path
        if depth>max_depth:
            continue
        #otherwise append neighbours
        for neighbours,move in get_neighbours(state):
            stack.append((neighbours,path+[move],depth+1))
    return None #if no solution

def get_input():
    state=[]
    print("Enter elements in form of A B C and put 0 where blank:\n")
    for i in range(3):
        row=list(map(int,input().strip().split()))
        state.append(row)
    return state
print("-------------8puzzle using DFS--------------\n")
print("Enter the start state:\n")
start=get_input()
print("Enter the goal state:\n")
goal=get_input()
solution=dfs(start,goal)
if solution:
    print("Solution exists!!")
    print(f"Number of moves:{len(solution)}")
    print("Moves:"," -> ".join(map(str,solution)))
    print("Showing the states:\n")
    curr=[row[:] for row in start]
    for move in solution:
        for neighbours,m in get_neighbours(curr):
            if m==move:
                curr=neighbours
                print(m)
                for i in curr:
                    print(i)
                print()
                break
else:
    print("No solution")
