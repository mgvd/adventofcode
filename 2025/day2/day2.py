input = []

def isValid(id):
    idstr = str(id)
    for x in range(0,round(len(idstr)/2+0.5)):
        sub = idstr[0:x+1]
        ocur = idstr.count(sub)
        if (ocur>1):
            test = ""
            for i in range(0,ocur):
                test += sub 
            if (test == idstr):
                # print (f"{test} == {idstr}")
                return False
    # while len(subs[subs.count])
    return True

with open("2025/day2/input.txt") as f:
    for x in f:
        input = x.split(",")

sum = 0
for i in input:

    a,b = i.split("-")
    for id in range(int(a),int(b)+1):
        # print(id)
        if not isValid(id):
            # print(id)
            sum += id
print(sum)


