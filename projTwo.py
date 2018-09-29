from queue import Queue as qu
from itertools import permutations as pu
import time 

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



def NewPermute(a):
    b = []
    for N in range(0,len(a[1]) - 1):
        #add child iff a's left and right boundry are not current left right boundry
        for I in range(1,len(a[1]) - (N)):
            if(a[0][0] != N  or a[0][1] != N+I):
                tmp = [[N , N + I , 0 , 0]]
                tmp.append( revItoJ(a[1], N, N+I) )
                b.append(tmp)
    return b


def isSolution( arr ):
    for i in range( 0, len(arr[1]) - 1 ):
        if arr[1][i] > arr[1][i + 1]:
            return False
    return  True


#arr[0][0,1,2,3] 0=lbound ; 1=rbound ; 2=parent ; 3=self
#function assumes arr[0]=(0,0,anyVal,anyVal)
def lalDoesBFS( arr ):
    t = time.clock()
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

    maxLen = 1
    #pointers[ arr[0][3] ] = arr[0][2]
    if isSolution( arr ):
        return (arr, values, pointers, time.clock() - t)

    while( True ):
        #if(maxLen < len(q)):
        #    maxLen = len(q)
        current = q.get()
        if isSolution( current ):
            return (current, values, pointers, time.clock() - t)

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
            if isSolution( child ):
                return (child, values, pointers, time.clock() - t) 
        index += ( chilCount) # +1
        #index += 1



def loreDoesIDS( a ):
    d = 0
    t = time.clock()
    while( True ):
        a = a[0:2]
        a, v, p = lalDoesDFS( a, d )
        if isSolution(a):
            return(a,v,p, time.clock() - t)
        d += 1

        #check how you do indexing, the values may not be getting unique indices
def lalDoesDFS( arr , d):
    stack = []
    pointers = {}
    values = []
    index = 0
    arr[0][2] = -1
    arr[0][3] = 0
    arr.append([d])
    stack.append( arr )
    values.append( arr )
    #parent of -1 means root node
    pointers[ arr[0][3] ] = -1
    #pointers[ arr[0][3] ] = arr[0][2]
    maxLen = 1
    if isSolution( arr ):
        return (arr[0:2], values, pointers)
    while( True ):
        if(maxLen < len(stack)):
            maxLen = len(stack)
        #print(len(stack))
        empty = len(stack) == 0
        if not empty:
            current = stack.pop()    
        else:
            return(arr[0:2],values,pointers)

        if current[2][0] == -1:
            return (arr[0:2], values, pointers)
        children = NewPermute(current)
        chilCount = 0
        for child in children:
            chilCount += 1 
            #parent is set
            child[0][2] = index
            #self index is set
            child[0][3] = index + chilCount
            child.append([current[2][0]-1])
            if(child[2][0] > 0):
                stack.append( child )
            #key=self index ; value=parent index
            pointers[child[0][3]] = child[0][2]
            if isSolution( child ):
                print('sol ', child)
                return (child[0:2], values, pointers)
            #if d == 0:
                #return (current, values, pointers)
        
                



#TODO values for P are always transformed to single digit
# 123 -> 1 2 3
#
#that's because your're reading them in as characters, try
# for...:
#   tmp2 = 0
#   while( i is not ' '):
#       tmp2 *= 10
#       tmp2 += int(i)
#       i = next i
#   tmp.append(tmp2)
#
def main():
    
    program = True
    while( program ):
        
        arr = [ [0,0,0,0] ]
        tmp = []
        tmparr = input(' enter P value for BFS: ')
        for i in tmparr:
            if i is not ' ':
                tmp.append( int(i) )
        arr.append( tmp )
        node, vals, dic, t = lalDoesBFS(arr)    
        idx = dic[node[0][3]]
        count = 0
        while( True ):        
            count += 1
            nextnode = vals[idx]
            print(nextnode)
            if nextnode[0][2] == -1:
                break
            idx = dic[nextnode[0][3]]
        print('solution printed out of order for readability: ')
        print( node[1], ' t: ', t , '; flip count: ' , count) 

        arr = [ [0,0,0,0] ]
        tmp = []
        tmparr = input(' enter P value of IDS: ')
        for i in tmparr:
            if i is not ' ':
                tmp.append( int(i) )
        arr.append( tmp )
        node, vals, dic ,t = loreDoesIDS(arr)    
        idx = dic[node[0][3]]
        for this in dic:
            print(dic[this])
        count = 0
        while( True ):        
            count += 1
            nextnode = vals[idx]
            print(nextnode[1])
            if nextnode[0][2] == -1:
                break
            idx = dic[node[0][3]]
        print('solution printed out of order for readability: ')
        print( node[1], ' t: ', t, '; flip count: ' , count) 

        cont = input(' to run again enter y or n to stop: ')
        for this in cont:
            if this == 'y':
                program = True
            else: program = False 

if __name__ == "__main__":
    main()


'''

def lalDoesIDS( a ):
    d = 0 
    b = False
    m = {}
    v = []
    while( True ):
        #a = a[0:2]
        solv, dnot, mapp, vals, a = loreDoesDFS( b,d,m,v,a )
        if solv:
            return (solv, mapp, vals,a)
        d += 1

        
#root parent must be set to -1 on initial call        
def loreDoesDFS( b, d, m, v,a):
    if(d < 0):
        return (False,d,m,v,a)
    
    v.append(a)
    #map a's self index to a's parent index 
    m[a[0][3]] = a[0][2]
    if(isSolution(a)):
        print(d)
        print(a)
        return (True, d,m,v,a)
    children = NewPermute(a)
    real = False
    chilcount = 0
    for child in children:
        chilcount += 1
        #child self index gets parent index + childcount
        child[0][3] = ( a[0][3] + chilcount)
        v.append(child)
        #map child's self index to parents self index 
        m[ child[0][3] ] = a[0][3]
        if(isSolution(child)):
            return (True,d,m,v,a)
        print(child)
        real, d,m,v,a = loreDoesDFS( real, d - 1, m, v, a)
        if(real):
            return (True,d,m,v,a)
    return (False,d,m,v,a)

            

def DataLore(n):
    if(n==1):
        return 1
    return n * DataLore(n-1)

'''
