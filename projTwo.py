from queue import Queue as qu



    
def flipCakes( cakes, ithCake ):
    tmpStack = []
    for i in range( ithCake ):
        tmpStack.append( cakes[i] )
    for i in reversed( range( ithCake, len(cakes) ) ):
        tmpStack.append( cakes[i] )
    return tmpStack            

def isSolution( arr ):
    for i in range( 1, len(arr) - 1 ):
        if arr[i] > arr[i + 1]:
            return False
    return  True

def lalDoesBFS( arr ):
    q = qu()
    q.put( arr )
    solved = isSolution( arr )
    while( not solved ):
        curArr = q.get()
        print(curArr)
        lastFlip = curArr[0]
        for i in range( 1, len(curArr) - 1 ):
            if i is not lastFlip:
                tmpArr = flipCakes( curArr, i)
                tmpArr[0] = i
                q.put(tmpArr)
        solved = isSolution( curArr )
        if solved:
            print('solution: ', curArr)


def main():
    arr = [0,3,1,5,7,2]
    #lalDoesBFS( arr )
    solved = isSolution( arr )
    d = 1
    sos = []
    sos.append( arr )
    while( not solved ):
        tmpArr = []
        for i in range( d + 1 ):
            for j in range(1, )






if __name__ == "__main__":
    main()
