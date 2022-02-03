from string import ascii_lowercase

try:
    inputfile = open('.\\2015\\11\\Input.txt','r')
    inputdata = inputfile.read()
    inputfile.close
except:
    print("Could not obtain input from file!")

def increment(current):
    position = -1
    while True:
        if current[position] == 'z':
            current[position] = 'a'
            position -= 1
        else:
            current[position] = ascii_lowercase[ascii_lowercase.find(current[position]) + 1]
            return current

def no_i_o_l(password):
    if 'i' not in password and 'o' not in password and 'l' not in password:
        return True
    else:
        return False

def has_two_repeating(password):
    first_repetition = ''
    for i in range(1,len(password)):
        if password[i] == password[i-1] and first_repetition == '':
            first_repetition = password[i]
        elif password[i] == password[i-1] and password[i] != first_repetition:
            return True
    return False

def has_three_ascending(password):
    for i in range(2,len(password)):
        straight = ''.join(password[i-2:i+1])
        if straight in ascii_lowercase:
            return True
    return False

def is_valid(password):
    return no_i_o_l(password) and has_two_repeating(password) and has_three_ascending(password)

def next_valid(current):
    valid = False
    while valid == False:
        next = increment(current)
        valid = is_valid(next)
        current = next
    return current

original = list(inputdata.replace('\n',''))
password1 = ''.join(next_valid(original))
password2 = ''.join(next_valid(list(password1)))

try:
    output = open('.\\2015\\11\\Output.txt','w')
    output.write(f"{password1}\n{password2}")
    output.close()
except:
    print("Could not write output file!")