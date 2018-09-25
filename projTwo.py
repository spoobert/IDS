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
    solved = isSolution( arr )
    pointers = []
    while( not solved ):
        current = q.get()
        print( current )
        #current[0] allways >= 1 
        rBound = len(arr) - 2
        for i in range( current[0], len(current) - 2 ):
            child = revItoJ( current, i, len(current) - 1 )
            child[0] = i
            pointers[i] = child
            q.put( child )
            if i < rBound:
                child = revItoJ( current, i, rBound )
                rBound -= 1 
                child[0] = i 
                pointers[i] = child
                q.put( child )
        if isSolution( current ):
            
        

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
    arr = [1,3,1,4,7,9]
    print('arr: ', arr)
    lalDoesBFS(arr)
    #print( lalDoesIDS( arr ) )    
    #print( lalDoesDFS( arr, 10 ) )



if __name__ == "__main__":
    main()
