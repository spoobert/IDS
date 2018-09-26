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

def lalDoesBFS( arr ):
    q = qu()
    q.put( arr )
    pointers = {}
    values = []
    index = 0
    pointers[str(arr)] = -1
    values.append(arr)
    while( True ):
        current = q.get()
        print( current )
        if isSolution( current ):
            return (current, values, pointers)
        children = NewPermute( current )
        for child in children:
            q.put( child )
            #pointers[str(child)] = index
            child[0][2] = len(values)
            #print(str(child))
            values.append(child)
            pointers[len(values)-1] = index
        index += 1
        


def NewPermute(a):
    b = []
    for N in range(1,len(a) - 1):
        for I in range(1,len(a) - (N)):
            if(a[0][0] != N  or a[0][1] != N+I):
                tmp = revItoJ(a, N, N+I)
                tmp[0] = (N,N+I, -1)
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
    arr = [(0,0,0),3,1,4,7,6, 3, 9]
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
