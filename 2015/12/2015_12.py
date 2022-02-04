import json

try:
    inputfile = open('.\\2015\\12\\Input.json','r')
    inputdata = json.load(inputfile)
    inputfile.close
except:
    print("Could not obtain input from file!")


def calculate_sum(object):
    sum = 0
    if type(object) is list:
        for item in object:
            sum += calculate_sum(item)
    elif type(object) is dict:
        for key in object:
            sum += calculate_sum(object[key])
    elif type(object) is int:
        sum += object
    return sum

def calculate_sum_no_red(object):
    sum = 0
    if type(object) is list:
        for item in object:
            sum += calculate_sum_no_red(item)
    elif type(object) is dict:
        for key in object:
            if object[key] != 'red':
                sum += calculate_sum_no_red(object[key])
            else:
                return 0
    elif type(object) is int:
        sum += object
    return sum

sum1 = calculate_sum(inputdata)
sum2 = calculate_sum_no_red(inputdata)

try:
    output = open('.\\2015\\12\\Output.txt','w')
    output.write(f"{sum1}\n{sum2}")
    output.close()
except:
    print("Could not write output file!")