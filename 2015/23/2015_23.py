def run_instruction(pos):
    global instructions
    try:
        words = instructions[pos].replace('\n','').split()
    except LookupError:
        return None
    if words[0] == 'hlf':
        registers[words[1]] = registers[words[1]] // 2
        return pos + 1
    elif words[0] == 'tpl':
        registers[words[1]] = registers[words[1]] * 3
        return pos + 1
    elif words[0] == 'inc':
        registers[words[1]] += 1
        return pos + 1
    elif words[0] == 'jmp':
        return pos + int(words[1])
    elif words[0] == 'jie':
        if registers[words[1].replace(',','')] % 2 == 0:
            if words[2][0] == '+':
                return pos + int(words[2][1:])
            elif words[2][0] == '-':
                return pos - int(words[2][1])
        else:
            return pos + 1
    elif words[0] == 'jio':
        if registers[words[1].replace(',','')] == 1:
            if words[2][0] == '+':
                return pos + int(words[2][1:])
            elif words[2][0] == '-':
                return pos - int(words[2][1:])
        else:
            return pos + 1   

try:
    inputfile = open('.\\2015\\23\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

instructions = inputdata

pos = 0
registers = {'a': 0,'b': 0}
while pos is not None:
    pos = run_instruction(pos)
b1 = registers['b']

pos = 0
registers = {'a': 1,'b': 0}
while pos is not None:
    pos = run_instruction(pos)
b2 = registers['b']

try:
    output = open('.\\2015\\23\\Output.txt','w')
    output.write(f"{b1}\n{b2}")
    output.close()
except:
    print("Could not write output file!")