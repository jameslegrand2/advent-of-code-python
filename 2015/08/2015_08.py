try:
    inputfile = open('.\\2015\\08\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

def code_length(line):
    code = -2
    escaped = False
    for char in line:
        if char == '\\' and escaped == False:
            escaped = True
        elif char in ['"','\\'] and escaped == True:
            escaped = False
            code += 1
        elif char == 'x' and escaped == True:
            escaped = False
            code -= 1
        else:
            code += 1
    return code

def encode(line):
    newline = '"'
    for char in line:
        if char == '"':
            newline += '\\"'
        elif char == '\\':
            newline += '\\\\'
        else:
            newline += char
    newline += '"'
    return newline

total1 = 0
for line in inputdata:
    line = line.replace('\n','')
    total1 += len(line) - code_length(line)

total2 = 0
for line in inputdata:
    line = line.replace('\n','')
    newline = encode(line)
    total2 += len(newline) - len(line)

try:
    output = open('.\\2015\\08\\Output.txt','w')
    output.write(f"{total1}\n{total2}")
    output.close()
except:
    print("Could not write output file!")