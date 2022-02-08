from itertools import combinations

try:
    inputfile = open('.\\2015\\17\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

containers = [int(line.replace('\n','')) for line in inputdata]
combo_count = 0
min_combo = len(containers)
for i in range(len(containers)):
    for combination in combinations(containers,i + 1):
        if sum(combination) == 150:
            combo_count += 1
            if len(combination) < min_combo:
                min_combo = len(combination)

try:
    output = open('.\\2015\\17\\Output.txt','w')
    output.write(f"{combo_count}\n{min_combo}")
    output.close()
except:
    print("Could not write output file!")