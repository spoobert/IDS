from queue import Queue as qu
from itertools import permutations as pu


#[ -1, 1, 2, 3, 4, 5]
def revItoJ( arr , i , j ):
    tmp = []
    
    for k in range( i ):
        tmp.append( arr[k] )
    for k in reversed( range( i, j + 1 ) ):
        tmp.append( arr[k] )
    for k in range( j + 1, len(arr) ):
        tmp.append( arr[k] )
    return tmp

def isSolution( arr ):
    for i in range( 1, len(arr) - 1 ):
        if arr[i] > arr[i + 1]:
            return False
    return  True
#arr[0][0,1,2,3] 0=lbound ; 1=rbound ; 2=parent ; 3=self
#function assumes arr[0]=(0,0,anyVal,0)
def lalDoesBFS( arr ):
    q = qu()
    pointers = {}
    values = []
    index = 0
    arr[0][2] = -1
    q.put( arr )
    values.append(arr)
    #parent of -1 means root node
    pointers[ arr[0][2] ] = index
    while( True ):
        current = q.get()
        print( current )
        if isSolution( current ):
            return (current, values, pointers)
        children = NewPermute( current )
        chilCount = 0
        for child in children:
            chilCount += 1 
            #parent is set
            child[0][2] = index
            #self index is set
            child[0][3] = index + chilCount
            q.put( child )
            values.append(child)
            #key=self index ; value=parent index
            pointers[child[0][3]] = child[0][2]
            chilCount += 1
        index += 1 + chilCount

def NewPermute(a):
    b = []
    for N in range(1,len(a) - 1):
        for I in range(1,len(a) - (N)):
            if(a[0][0] != N  or a[0][1] != N+I):
                tmp = revItoJ(a, N, N+I)
                tmp[0] = (N , N+I , 0 , 0)
                b.append(tmp)
    return b


        

def lalDoesDFS( arr, d ):
    print( arr )
    if d == 0:
        return isSolution( arr )
    children = pu( arr )
    for c in children:
        return lalDoesDFS( c, d - 1 )

def lalDoesIDS( arr ):
    d = 0 
    solved = lalDoesDFS( arr, d )
    while( not solved ):
        d += 1
        solved = lalDoesDFS( arr, d )
        if solved:
            print( 'Solution: ', arr )



def main():
    arr = [(0,0,0,0),3,1,4,7,6, 3, 9]
    node, vals, dic = lalDoesBFS(arr)
    idx = dic[node[0][2]]
    while( idx >= 0):
        print(node)
        print(idx)
        node = vals[idx]
        idx = dic[node[0][2]]
        if(idx == 753):
            break

    #print( lalDoesIDS( arr ) )    
    #print( lalDoesDFS( arr, 10 ) )



if __name__ == "__main__":
    main()
