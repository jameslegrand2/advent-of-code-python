from itertools import combinations
from copy import copy

def has_a_possible_2_compartment_balance(remainder):
    for i in range(1,len(remainder) + 1):
        for group1 in combinations(remainder,i):
            group2 = copy(remainder)
            for present in group1:
                group2.remove(present)
            if sum(group1) == sum(group2):
                return True
    return False

def has_a_possible_3_compartment_balance(remainder):
    for i in range(1,len(remainder) + 1):
        for group1 in combinations(remainder,i):
            remainder2 = copy(remainder)
            for present in group1:
                remainder2.remove(present)
            if sum(group1) == sum(remainder2) // 2:
                if has_a_possible_2_compartment_balance(remainder2):
                    return True
    return False

try:
    inputfile = open('.\\2015\\24\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

presents = []
for line in inputdata:
    presents.append(int(line.replace('\n','')))
presents.sort(reverse=True)

for i in range(1,len(presents) + 1):
    ideal_quantum_entanglement = 1e100
    for group1 in combinations(presents,i):
        remainder = copy(presents)
        for present in group1:
            remainder.remove(present)
        if sum(group1) == sum(remainder) // 2:
            if has_a_possible_2_compartment_balance(remainder):
                quantum_entanglement = 1
                for present in group1:
                    quantum_entanglement *= present
                if quantum_entanglement < ideal_quantum_entanglement:
                    ideal_quantum_entanglement = quantum_entanglement
    if ideal_quantum_entanglement < 1e100:        
        break
quantum_entanglement_1 = ideal_quantum_entanglement

for i in range(1,len(presents) + 1):
    ideal_quantum_entanglement = 1e100
    for group1 in combinations(presents,i):
        remainder = copy(presents)
        for present in group1:
            remainder.remove(present)
        if sum(group1) == sum(remainder) // 3:
            if has_a_possible_3_compartment_balance(remainder):
                quantum_entanglement = 1
                for present in group1:
                    quantum_entanglement *= present
                if quantum_entanglement < ideal_quantum_entanglement:
                    ideal_quantum_entanglement = quantum_entanglement
    if ideal_quantum_entanglement < 1e100:        
        break
quantum_entanglement_2 = ideal_quantum_entanglement

try:
    output = open('.\\2015\\24\\Output.txt','w')
    output.write(f"{quantum_entanglement_1}\n{quantum_entanglement_2}")
    output.close()
except:
    print("Could not write output file!")