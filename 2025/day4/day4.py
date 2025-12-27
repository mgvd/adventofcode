filename = "test.txt"
filename = "input.txt"
direct = "2025/day4/"

input = []

def readFile():
    r = []
    with open(direct + filename) as f:
        for x in f:
            r.append(x.strip())
    return r

def printField(field):
    for l in field:
        print(l)

def countNeighbours(x,y, field):
    h = len(field)
    w = len(field[0])
    n = 0
    # left neightbours
    if (x > 0):
        if (y > 0):
            if (field[x-1][y-1] == '@'):
                n += 1
        if (field[x-1][y] == '@'):
            n += 1
        if ( y < h-1):
            if (field[x-1][y+1] == '@'):
                n +=1
    
    # top & bottom neighbours
    if (y > 0):
        if (field[x][y-1] == '@'):
            n += 1
    if ( y < h-1):
        if (field[x][y+1] == '@'):
            n +=1
    # right neighbours
    if (x < w-1):
        if (y > 0):
            if (field[x+1][y-1] == '@'):
                n += 1
        if (field[x+1][y] == '@'):
            n += 1
        if ( y < h-1):
            if (field[x+1][y+1] == '@'):
                n +=1
    return n
        
def copyArray(arr):
    newarr = []
    for i, v in enumerate(arr):
        if (type(arr[i]) is list):
            newarr.append(copyArray(arr[i]))
        else:
            newarr.append(v)
    return newarr
    

def main():
    input = readFile()

    field = [] 
    count = 0
    for line in input:
        field.append(list(line))
   
    totalRemoved = 0
    count, newfield = removeRolls(field)
    totalRemoved += count
    while count > 0:
        count, newfield = removeRolls(newfield)
        totalRemoved += count
    

    print(totalRemoved)

def removeRolls(field):
    count = 0
    newfield = copyArray(field.copy())
    width = len(field[0])
    height = len(field)
    for x in range(0,width):
        for y in range(0,height):
            if (field[x][y] == '@'):
                n = countNeighbours(x,y,field)
                if (n < 4):
                    newfield[x][y] = 'x'
                    count += 1
    return (count, newfield)

main()


