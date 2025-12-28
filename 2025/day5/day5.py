filename = "test.txt"
filename = "input.txt"
direct = "2025/day5/"

input = []

def readFile():
    r = []
    with open(direct + filename) as f:
        for x in f:
            r.append(x.strip())
    return r

def readRanges(input):
    ranges = []
    for r in input:
        if r.strip() == "":
            break
        low,high = r.split("-")
        ranges.append((int(low),int(high)))
        # print(f'{low}-{high}')
    return ranges

def readIngredients(input):
    ins = []
    isranges = True
    for r in input:
        if r.isspace() or r == '':
            isranges = False
        elif (isranges == False):
            ins.append(int(r))
    return ins

def countFreshIngredients(ranges, ins):
    count = 0
    for i in ins:
        for l, h in ranges:
            if (i>l and i <= h):
                count += 1
                break

    print(count)

def countPossibleFreshIngredients(ranges):
    count = 0
    i = []
    
    newranges =removeOverlapping(ranges)

    for l,h in set(newranges):
        count += (h-l+1)
    print(count)
    print(set(newranges))

def removeOverlapping(ranges):
   
    newranges = []
    for i,j in ranges:
        hasOverlap, l ,h = getOverlappingRange(i,j, ranges)
        if (hasOverlap):
            newranges.append((min(i,l),max(j,h)))
        else:
            newranges.append((i,j))              
    if hasOverlappingRanges(newranges):
        return removeOverlapping(newranges)
    return newranges

def getOverlappingRange(l,h,ranges):
    for i,j in ranges:
        if not(i == l and j == h):
            if (i<=l and j>=l) or (i<=h and j>=h) or (i>=l and j<=h):
                # print(f'Overlapping: {i}-{j} overlaps with {l}-{h}')
                return True, i ,j
    return False, 0, 0

def hasOverlappingRanges(ranges):
    for l,h in ranges:
        hasOverlap, l ,h = getOverlappingRange(l,h,ranges)
        if hasOverlap:
            return True
    return False  

def main():
    input = readFile()

    ranges = readRanges(input)
    # ins = readIngredients(input)
    # countFreshIngredients(ranges, ins)
    countPossibleFreshIngredients(ranges)

main()


