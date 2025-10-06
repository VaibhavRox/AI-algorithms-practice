from collections import deque
def water_jug(A,B,C):
    if C>A+B:
        print("Invalid Case:")
        return 
    visited=set()
    queue=deque()
    queue.append(((0,0),[(0,0)]))
    while queue:
        (a,b),path=queue.popleft()
        if (a==0 and b==C) or (a==C and b==0) or (a+b==C):
            print("Solution Path:")
            # Print states separated by ' -> ' without a trailing arrow
            print(" -> ".join(map(str, path)))
            return True
        if (a,b) in visited:
            continue
        visited.add((a,b))
        next_states=[
            (A,b),(a,B),(a,0),(0,b),    #filling and throwing out 
            (a-min(a,B-b),b+min(a,B-b)),#pouring from A->B
            (a+min(A-a,b),b-min(A-a,b)) #pouring from B->A
        ]
        for state in next_states:
            if state not in visited:
                queue.append((state,path+[state]))
    print("No valid sequeuence")
    return False
A=int(input("Enter capacity of jug A:"))
B=int(input("Enter capacity of jug B:"))
C=int(input("Enter target capacity:"))
water_jug(A,B,C)