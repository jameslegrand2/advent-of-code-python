def has_three_vowels(string):
    return string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') >= 3

def has_double_letter(string):
    for i in range(1,len(string)):
        if string[i] == string[i - 1]:
            return True
    return False

def has_no_bad_substrings(string):
    return string.find('ab') == -1 and string.find('cd') == -1 and string.find('pq') == -1 and string.find('xy') == -1

def is_nice1(string):
    return has_three_vowels(string) and has_double_letter(string) and has_no_bad_substrings(string)

def has_letter_pair_twice(string):
    for i in range(1,len(string)):
        pair = string[i - 1:i + 1]
        if string.find(pair,i+1) != -1:
            return True
    return False

def has_letter_sandwich(string):
    for i in range(2,len(string)):
        if string[i] == string[i - 2]:
            return True
    return False

def is_nice2(string):
    return has_letter_pair_twice(string) and has_letter_sandwich(string)

try:
    inputfile = open('.\\2015\\05\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

total1 = 0
for line in inputdata:
    if is_nice1(line):
        total1 += 1

total2 = 0
for line in inputdata:
    if is_nice2(line):
        total2 += 1

try:
    output = open('.\\2015\\05\\Output.txt','w')
    output.write(f"{total1}\n{total2}")
    output.close()
except:
    print("Could not write output file!")