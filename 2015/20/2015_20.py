try:
    inputfile = open('.\\2015\\20\\Input.txt','r')
    inputdata = inputfile.read()
    inputfile.close
except:
    print("Could not obtain input from file!")

'''
house = 0
min_presents = int(inputdata)
while True:
    house += 1
    elf = 0
    house_presents = 0
    while elf <= house:
        elf += 1
        if house % elf == 0:
            house_presents += 10 * elf
    print(house,house_presents)
    if house_presents >= min_presents:
        break
print(house)
'''