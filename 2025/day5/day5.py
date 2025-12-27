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

    for l,h in ranges:
        # count += (h-l)
        i = i + [*range(l,h+1)]
    print(len(set(i)))

def main():
    input = readFile()

    ranges = readRanges(input)
    ins = readIngredients(input)
    countFreshIngredients(ranges, ins)
    countPossibleFreshIngredients(ranges)

main()


