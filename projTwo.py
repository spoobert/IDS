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
    for i in range( 0, len(arr[1]) - 1 ):
        if arr[1][i] > arr[1][i + 1]:
            return False
    return  True


#arr[0][0,1,2,3] 0=lbound ; 1=rbound ; 2=parent ; 3=self
#function assumes arr[0]=(0,0,anyVal,anyVal)
def lalDoesBFS( arr ):
    q = qu()
    pointers = {}
    values = []
    index = 0
    arr[0][2] = -1
    arr[0][3] = 0 
    q.put( arr )
    values.append(arr)

    #parent of -1 means root node
    pointers[ arr[0][3] ] = index

    #pointers[ arr[0][3] ] = arr[0][2]

    while( True ):
        current = q.get()
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
            #chilCount += 1
        index += ( chilCount) # +1
        #index += 1

def NewPermute(a):
    b = []
    #print(a)
    for N in range(0,len(a[1]) - 1):
        #print('BBB')
        #add child iff a's left and right boundry are not current left right boundry
        for I in range(0,len(a[1]) - (N)):
            if(a[0][0] != N  or a[0][1] != N+I):
                tmp = [[N , N + I , 0 , 0]]
                tmp.append( revItoJ(a[1], N, N+I) )
                #print(tmp)
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
    arr = []
    arr.append( [0,0,0,0] )
    arr.append( [3,1,4,7,6, 3, 9] )
    node, vals, dic = lalDoesBFS(arr)    
    idx = dic[node[0][2]]
    while( idx >= 0 ):        

        node = vals[idx]
        print(node)
        if node[0][2] == -1:
            print(node)
            break
        idx = dic[node[0][2]]
        

    #print( lalDoesIDS( arr ) )    
    #print( lalDoesDFS( arr, 10 ) )
    



if __name__ == "__main__":
    main()
