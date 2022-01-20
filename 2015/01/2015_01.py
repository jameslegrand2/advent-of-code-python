try:
    input = open('Input.txt','r')
    str = input.read()
    input.close
except:
    print("Could not obtain input from file!")

print(str)

