class Wire:
    def __init__(self,instructionstring):
        fullinstruction = instructionstring.replace('\n','')
        inout = fullinstruction.split(' -> ')
        self.name = inout[1]
        inputargs = inout[0].split()
        if len(inputargs) == 1:
            try:
                self.signal = int(inputargs[0])
            except:
                self.input1name = inputargs[0]
                self.operator = 'PASS'
        elif len(inputargs) == 2:
            self.operator = inputargs[0]
            self.input1name = inputargs[1]
            if self.input1name.isnumeric():
                self.input1signal = int(self.input1name)
        elif len(inputargs) == 3:
            self.input1name = inputargs[0]
            if self.input1name.isnumeric():
                self.input1signal = int(self.input1name)
            self.operator = inputargs[1]
            if self.operator in ['AND','OR']:
                self.input2name = inputargs[2]
                if self.input2name.isnumeric():
                    self.input2signal = int(self.input2name)
            else:
                self.modifier = int(inputargs[2])

    def can_propogate(self):
        if self.operator in ['NOT','LSHIFT','RSHIFT','PASS']:
            if hasattr(self,'input1signal'):
                return True
        elif self.operator in ['AND','OR']:
            if hasattr(self,'input1signal') and hasattr(self,'input2signal'):
                return True
        return False

    def propogate_signal(self):
        if self.operator == 'AND':
            self.signal = self.input1signal & self.input2signal
        elif self.operator == 'OR':
            self.signal = self.input1signal | self.input2signal
        elif self.operator == 'LSHIFT':
            self.signal = self.input1signal << self.modifier
        elif self.operator == 'RSHIFT':
            self.signal = self.input1signal >> self.modifier
        elif self.operator == 'NOT':
            self.signal = ~self.input1signal & 65535
        elif self.operator == 'PASS':
            self.signal = self.input1signal
              
class Circuit():
    def __init__(self):
        self.wires_with_signal = {}
        self.wires_without_signal = {}

    def lookup_input_signal(self,inputwirename):
        if inputwirename in self.wires_with_signal:
            return self.wires_with_signal[inputwirename].signal

    def calculate_input_signals(self):
        wirestoremove = []
        for wirename in self.wires_without_signal:
            wire = self.wires_without_signal[wirename]
            if hasattr(wire,'input1name') and not hasattr(wire,'input1signal'):
                signal = self.lookup_input_signal(wire.input1name)
                if type(signal) is int:
                    wire.input1signal = signal
            if hasattr(wire,'input2name') and not hasattr(wire,'input2signal'):
                signal = self.lookup_input_signal(wire.input2name)
                if type(signal) is int:
                    wire.input2signal = signal
            if wire.can_propogate():
                wire.propogate_signal()
                self.wires_with_signal[wire.name] = wire
                wirestoremove.append(wirename)
        for wirename in wirestoremove:
            self.wires_without_signal.pop(wirename)

try:
    inputfile = open('.\\2015\\07\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

circuit1 = Circuit()
for line in inputdata:
    wire = Wire(line)
    if hasattr(wire,'signal'):
        circuit1.wires_with_signal[wire.name] = wire
    else:
        circuit1.wires_without_signal[wire.name] = wire
while len(circuit1.wires_without_signal) > 0:
    circuit1.calculate_input_signals()
a1 = circuit1.wires_with_signal['a'].signal

circuit2 = Circuit()
for line in inputdata:
    wire = Wire(line)
    if wire.name == 'b':
        wire.signal = a1
    if hasattr(wire,'signal'):
        circuit2.wires_with_signal[wire.name] = wire
    else:
        circuit2.wires_without_signal[wire.name] = wire
while len(circuit2.wires_without_signal) > 0:
    circuit2.calculate_input_signals()
a2 = circuit2.wires_with_signal['a'].signal

try:
    output = open('.\\2015\\07\\Output.txt','w')
    output.write(f"{a1}\n{a2}")
    output.close()
except:
    print("Could not write output file!")