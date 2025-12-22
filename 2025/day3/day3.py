filename = "test.txt"
filename = "input.txt"
direct = "2025/day3/"

input = []

def readFile():
    r = []
    with open(direct + filename) as f:
        for x in f:
            r.append(x.strip())
    return r

def findLargest(numbers):
    i = [0,0]
    for f,n in enumerate(numbers):
        if int(n) > i[0]:
            i=[int(n), f]
    return i

input = readFile()


sum = 0
targetlen = 12
for i in input:
    n = list(i)
    res = ""
    index = 0
    l = 0
    while len(res)<targetlen:
        endindex = -targetlen+l+1
        if endindex == 0:
            f = n
        else:
            f= n[:endindex]
        h, index = findLargest(f)
        n = n[index+1:]
        res += str(h)
        l = len(res)
    sum += int(res)
    print(res)

    
print(sum)


