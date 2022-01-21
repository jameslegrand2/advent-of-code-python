from hashlib import md5

def get_md5hex(string):
    return md5(string.encode()).hexdigest()

def check_solution(string,leadingzeros):
    return get_md5hex(string)[:leadingzeros] == '0' * leadingzeros

try:
    inputfile = open('.\\2015\\04\\Input.txt','r')
    inputdata = inputfile.read()
    inputfile.close
except:
    print("Could not obtain input from file!")

solution1 = 0
while True:
    solution1 += 1
    stringtocheck = inputdata + str(solution1)
    if check_solution(stringtocheck,5):
        break

solution2 = 0
while True:
    solution2 += 1
    stringtocheck = inputdata + str(solution2)
    if check_solution(stringtocheck,6):
        break

try:
    output = open('.\\2015\\04\\Output.txt','w')
    output.write(f"{solution1}\n{solution2}")
    output.close()
except:
    print("Could not write output file!")

