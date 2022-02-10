from math import sqrt

def sum_factors(num):
    if num == 1:
        return num
    result = 1 + num
    for i in range(2,int(sqrt(num)) + 1):
        if num % i == 0:
            result += i
            if i != (num/i):
                result += num//i
    return result

def sum_factors_minfactor(num,minfactor):
    result = 0
    if minfactor == 1:
        result += 1
    if num > 1:
        result += num
    for i in range(2,int(sqrt(num)) + 1):
        if num % i == 0:
            if i >= minfactor:
                result += i
            if i != (num/i) and (num/i) >= minfactor:
                result += num//i
    return result

try:
    inputfile = open('.\\2015\\20\\Input.txt','r')
    inputdata = inputfile.read()
    inputfile.close
except:
    print("Could not obtain input from file!")

min_presents = int(inputdata)

house = 0
while True:
    house += 1
    house_presents = (sum_factors(house) * 10)
    if house_presents >= min_presents:
        last_house_1 = house
        break

house = 0
min_elf = 1
while True:
    house += 1
    house_presents = (sum_factors_minfactor(house,min_elf) * 11)
    if house_presents >= min_presents:
        last_house_2 = house
        break
    if house % 50 == 0:
        min_elf += 1

try:
    output = open('.\\2015\\20\\Output.txt','w')
    output.write(f"{last_house_1}\n{last_house_2}")
    output.close()
except:
    print("Could not write output file!")