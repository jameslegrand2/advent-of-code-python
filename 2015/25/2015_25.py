def next_code(previous_code):
    return previous_code * 252533 % 33554393

def get_code(target):
    codes = [[20151125]]
    i = 0
    obtained_target = False
    while not obtained_target:
        i += 1
        previous = codes[0][-1]
        next = next_code(previous)
        codes.append([next])
        for j in range(1,i + 1):
            previous = next
            next = next_code(previous)
            codes[-1 - j].append(next)
            if len(codes) >= target[0]:
                if len(codes[target[0] - 1]) == target[1]:
                    obtained_target = True
                    break
    return codes[target[0] - 1][target[1] - 1]

try:
    inputfile = open('.\\2015\\25\\Input.txt','r')
    inputdata = inputfile.read()
    inputfile.close
except:
    print("Could not obtain input from file!")

words = inputdata.replace(',','').replace('.','').split()
target = (int(words[-3]),int(words[-1]))
code = get_code(target)

try:
    output = open('.\\2015\\25\\Output.txt','w')
    output.write(f"{code}")
    output.close()
except:
    print("Could not write output file!")