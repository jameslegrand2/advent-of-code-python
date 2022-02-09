def get_generatable_molecules(starting_molecule):
    global possible_replacements
    generatable_molecules = []
    skip = False
    for i in range(len(starting_molecule)):
        if skip == False:
            for replacement in possible_replacements:
                if starting_molecule[i] == replacement[0]:
                    generatable_molecules.append(starting_molecule[:i] + replacement[1] + starting_molecule[i+1:])
                if i < len(starting_molecule):
                    if starting_molecule[i:i+2] == replacement[0]:
                        generatable_molecules.append(starting_molecule[:i] + replacement[1] + starting_molecule[i+2:])
                        skip = True
        else:
            skip = False
    return generatable_molecules

def sort_replacements(possible_replacements):
    for i in range(len(possible_replacements)):
        sorted = True
        for j in range(len(possible_replacements) - i - 1):
            j_uppers = 0
            j_p1_uppers = 0
            for char in possible_replacements[j][1]:
                if char.isupper:
                    j_uppers += 1
            for char in possible_replacements[j + 1][1]:
                if char.isupper:
                    j_p1_uppers += 1
            if j_uppers > j_p1_uppers:
                possible_replacements[j],possible_replacements[j + 1] = possible_replacements[j + 1],possible_replacements[j]
                sorted = False
        if sorted:
            break
    return possible_replacements[::-1]

def get_reduced_molecules(molecule):
    global possible_replacements
    starting_molecules = []
    for replacement in possible_replacements:
        key = 0
        while key < len(molecule):
            key = molecule.find(replacement[1],key)
            if key == -1:
                break
            starting_molecules.append(molecule[:key] + molecule[key:].replace(replacement[1],replacement[0],1))
            key += len(replacement[1])
    return starting_molecules

try:
    inputfile = open('.\\2015\\19\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

starting_molecule = inputdata.pop().replace('\n','')
del inputdata[-1]
possible_replacements = [tuple(line.replace('\n','').split(' => ')) for line in inputdata]
possible_replacements = sort_replacements(possible_replacements)

count1 = len(set(get_generatable_molecules(starting_molecule)))

target_molecules = [starting_molecule]
count2 = 0
while 'e' not in target_molecules:
    starting_molecules = []
    for target_molecule in target_molecules:
        starting_molecules += get_reduced_molecules(target_molecule)
    count2 += 1
    target_molecules = list(set(starting_molecules))
    print(count2,len(target_molecules))
print(count2)


'''
target_molecule = starting_molecule
starting_molecules = ['e']
count2 = 0
while True:
    generateable_molecules = []
    for starting_molecule in starting_molecules:
        generateable_molecules += get_generatable_molecules(starting_molecule)
    count2 += 1
    if target_molecule in generateable_molecules:
        break
    else:
        starting_molecules = list(set(generateable_molecules))
print(count2)
'''