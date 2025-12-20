
dail = 50
i = 0
inst = []
with open("2025/day1/input.txt") as f:
    for x in f:
        inst.append(x.split()[0])

for x in inst:
    # print(x)
   # if (len(x)>1):
    r = x[:1]
    c = int(x[1:])
    if (r == "L"):
        if (dail == 0):
            i -= 1
        dail -= c
        while (dail < 0):
            dail += 100
            i += 1
        if (dail == 0): 
            i += 1
    if (r == "R"):
        dail += c
        while (dail > 99):
            dail -= 100
            i += 1
print(i)