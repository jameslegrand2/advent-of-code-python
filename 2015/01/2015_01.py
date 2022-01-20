from collections import Counter

try:
    inputfile = open('.\\2015\\01\\Input.txt','r')
    inputdata = inputfile.read()
    inputfile.close
except:
    print("Could not obtain input from file!")

#Part 1
counts = Counter(inputdata)
total1 = counts['('] - counts[')']

#Part 2
position = 0
total2 = 0
for character in inputdata:
    position += 1
    if character == '(':
        total2 += 1
    elif character == ')':
        total2 -=1
    if total2 < 0:
        break
        
try:
    output = open('.\\2015\\01\\Output.txt','w')
    output.write(f"{total1}\n{position}")
    output.close()
except:
    print("Could not write output file!")