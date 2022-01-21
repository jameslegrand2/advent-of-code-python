try:
    inputfile = open('.\\2015\\02\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

def dimensions(string):
    return string.rstrip().split('x')

def surfaceareawithslack(length,width,height):
    side1area = length * width
    side2area = length * height
    side3area = width * height
    sideareas = [side1area,side2area,side3area]
    sideareas.sort()
    slack = sideareas[0]
    return 2 * (side1area + side2area + side3area) + slack

def smallestperimeterwithslack(length,width,height):
    side1perimeter = 2 * (length + width)
    side2perimeter = 2 * (length + height)
    side3perimeter = 2 * (width + height)
    sideperimeters = [side1perimeter,side2perimeter,side3perimeter]
    sideperimeters.sort()
    smallestperimeter = sideperimeters[0]
    slack = length * width * height
    return smallestperimeter + slack

total1 = 0
total2 = 0
for line in inputdata:
    dimensionslist = dimensions(line)
    total1 += surfaceareawithslack(int(dimensionslist[0]),int(dimensionslist[1]),int(dimensionslist[2]))
    total2 += smallestperimeterwithslack(int(dimensionslist[0]),int(dimensionslist[1]),int(dimensionslist[2]))

try:
    output = open('.\\2015\\02\\Output.txt','w')
    output.write(f"{total1}\n{total2}")
    output.close()
except:
    print("Could not write output file!")