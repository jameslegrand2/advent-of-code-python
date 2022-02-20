def get_atoms(molecule):
    atoms = []
    start = 0
    for i in range(len(molecule)):
        if molecule[i].isupper() == True and i > start:
            atoms.append(molecule[start:i])
            start = i
        if i == len(molecule) - 1:
            atoms.append(molecule[start:])
    return atoms
    
def get_generatable_molecules(starting_molecule):
    global possible_replacements
    generatable_molecules = []
    for i in range(len(starting_molecule)):
        for replacement in possible_replacements:
            if starting_molecule[i] == replacement[0]:
                generatable_molecules.append(starting_molecule[:i] + replacement[1] + starting_molecule[i+1:])
    return generatable_molecules

try:
    inputfile = open('.\\2015\\19\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

starting_molecule = get_atoms(inputdata.pop().replace('\n',''))
del inputdata[-1]
possible_replacements = []
for line in inputdata:
    molecules = line.replace('\n','').split(' => ')
    possible_replacements.append((molecules[0],get_atoms(molecules[1])))

generatable_molecules = get_generatable_molecules(starting_molecule)
for i in range(len(generatable_molecules)):
    generatable_molecules[i] = ''.join(generatable_molecules[i])
count1 = len(set(generatable_molecules))

count2 = 0
current_molecule = starting_molecule
while current_molecule != ['e']:
    for possible_replacement in possible_replacements:
        if ''.join(possible_replacement[1]) in ''.join(current_molecule):
            current_molecule = get_atoms(''.join(current_molecule).replace(''.join(possible_replacement[1]),''.join(possible_replacement[0]),1))
            count2 += 1

try:
    output = open('.\\2015\\19\\Output.txt','w')
    output.write(f"{count1}\n{count2}")
    output.close()
except:
    print("Could not write output file!")