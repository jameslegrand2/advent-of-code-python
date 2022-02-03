try:
    inputfile = open('.\\2015\\10\\Input.txt','r')
    inputdata = inputfile.read()
    inputfile.close
except:
    print("Could not obtain input from file!")

def next_sequence(current):
    next = ''
    for i in range(len(current)):
        if i == 0:
            count = 1
            number = current[i]
        elif current[i] == current[i-1]:
            count += 1
        elif current[i] != current[i-1]:
            next += str(count) + number
            count = 1
            number = current[i]
    next += str(count) + number
    return next

current = inputdata.replace('\n','')
for i in range(40):
    next = next_sequence(current)
    current = next
result1 = len(current)

current = inputdata.replace('\n','')
for i in range(50):
    next = next_sequence(current)
    current = next
result2 = len(current)

try:
    output = open('.\\2015\\10\\Output.txt','w')
    output.write(f"{result1}\n{result2}")
    output.close()
except:
    print("Could not write output file!")