# Name: Soon Sam R Santos
# Date: February 19, 2017
# Session: 2
# State_machines2.py

    # SuperClass
class SM:
    # Default Values
    startState = None
    def start(self):
        self.state = self.startState
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o
    def transduce(self, inputs):
        self.start() 
        return [self.step(inp) for inp in inputs]
    def run(self, n=10):
        return [self.transduce([None]*n)]
    # Defaul Values
    def getNextValues(self, state, inp):
        nextState = self.getNextState(state, inp)
        return (nextState, nextState)


# SubClass
class Accumulator(SM):
    startState = 0
    def getNextState(self, state, inp):
        return state + inp
# TestCases
a = Accumulator()
a.start()
print a.state         # 0
print a.step(5)       # 5
print a.step(15)      # 20
        
# SubClass
class ABC(SM):
    startState = 0
    def getNextValues(self, state, inp):
        if state == 0 and inp == 'a':
            return (1, True)
        elif state == 1 and inp == 'b':
            return (2, True)
        elif state == 2 and inp == 'c':
            return (0, True)
        else:
            return (3, False)
# TestCases
b = ABC()
b.start()
print b.step('a')    # True
print b.step('b')    # True
print b.step('c')    # True
print b.step('b')    # False, always...
c = ABC()
c.start
print c.transduce(['a','b','c','b'])    # [True, True, True, False]

# SubClass
class UpDown(SM):
    startState = 0
    # getNextState because the nextstate = output. So we use the default method getNextValues.
    def getNextState(self, state, inp):
        if inp == 'u':
            return state + 1
        else:
            return state - 1
# TestCases
ud = UpDown()
ud.start()
print ud.step('u')  # 1   State: 0
print ud.step('u')  # 2   State: 1
print ud.step('u')  # 3   State: 2
print ud.step('d')  # 2   State: 3
print ud.step('d')  # 1   State: 2
print ud.transduce(['u','d','u','u','d'])   # [1,0,1,2,1]

# SubClass
# We will use so frequently this machine that we put it with the class SM file.
class Delay(SM):
    def __init__(self, v0):
        self.startState = v0
    def getNextValues(self, state, inp):
        # Nextstate = actual inp / Output = previousstate
        return (inp, state)
d = Delay(7)
print d.transduce([3,5,7,10])   # [7,3,5,7]

# SubClass        
class Average2(SM):
    startState = 0
    def getNextValues(self, state, inp):
        return (inp, (state + inp) / 2.0)
# TestCases
a2 = Average2()
print a2.transduce([100, 50, 150, 200])    # [50.0, 75.0, 100.0, 175.0]

# SubClass
class sumLast3(SM):
    startState = (0, 0)
    def getNextValues(self, state, inp):
        (previousPreviousinp, previousInp) = state
        return ((previousInp, inp),
                (previousPreviousinp + previousInp + inp))
sl3 = sumLast3()
print sl3.transduce([2,1,3,4,10,1,2,1,5])

# Select Machines are very useful, this is a simple one who takes the kth element of a list
# SubClass
class Select(SM):
    def __init__(self, k):
        self.k = k
    def getNextState(self, state, inp): # inp is a list of inputs.
        return inp[self.k]

# SubClass
class SimpleParkingGate(SM):
    startState = 'waiting'

    def generateOutput(self, state):
        if state == 'raising':
            return 'raise'
        elif state == 'lowering':
            return 'lower'
        else:
            return 'nop'
    def getNextValues(self, state, inp):
        (gatePosition, carAtGate, carJustExited) = inp
        if state == 'waiting' and carAtGate:
            nextState = 'raising'
        elif state == 'raising' and gatePosition == 'top':
            nextState = 'raised'
        elif state == 'raised' and carJustExited:
            nextState = 'lowering'
        elif state == 'lowering' and gatePosition == 'bottom':
            nextState = 'waiting'
        else:
            nextState = state
        return (nextState, self.generateOutput(nextState))

# TestCases
spg = SimpleParkingGate()
testInput = [('bottom',False,False), ('bottom',True,False), ('bottom',True,False),
             ('middle',True,False), ('bottom',True,False), ('bottom',True,False),
             ('top',True,False), ('top',True,False), ('top',True,False), ('top',True,True), ('top',True,True), ('top',True,False),
             ('middle',True,False), ('middle',True,False), ('middle',True,False),]
print spg.transduce(testInput)

# SubClass for parallel machines
class Parallel(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)
    def getNextValues(self, state, inp):
        # Input two states, one for each machines
        (s1, s2) = state
        # Use the method for each machine, note that the input is the same.
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        # return the state and the outputs
        return ((newS1, newS2), (o1, o2))

# For parallel2 the only difference is that the input are different for the machines
# the init method is the same, so we will inherits it from Parallel
class Parallel2(Parallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (i1, i2) = splitValue(inp)
        (newS1, o1) = self.m1.getNextValues(s1, i1)
        (newS2, o2) = self.m2.getNextValues(s2, i2)
        return ((newS1,newS2),(o1, o2))
# The value of the input latter may be undefined, that's why we use splitValue, to accept both undefined or numbers.
    def splitValue(v):
        if v == 'undefined':
            return ('undefined','undefined')
        else:
            return v

# ParallelAdd is equal to Parallel, except it has only one output(the sum of both).
class ParallelAdd(Parallel):
    # Inherits from Parallel to don't need to initializate it again.
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), o1+o2)

# Feedback machine: Takes the output at t as the input at t+1
# We must use cascade machines in order for this to work.
class TF(SM):
    startState = False
    def getNextValues(self, state, inp):
         if inp == True:
             return (True, False)
         if inp == False:
             return (False, True)
    # Not defined the true and false machine. No sufficient knowledge
# Will take the output as input. Input will be not necessary.
class Feedback(SM):
    def __init__(self, sm):
        # Taking the machine I will use.
        self.m = sm
        # Setting the starting state of this machine.
        self.startState = self.m.startState
    # As we don't know what first input will be we must set it as undefined.
    # If it get undefined as input it should return undefined as an output.
    # So: If we pass undefined to the constuent machine we must not get undefined as an output. If we do,
    # it means there is an immediate dependence between them.
    # NextState: Nextstate of the constituent by fb value
    def getNextValues(self, state, inp):   # This method is from the feedback!!!
        (ignore, o) = self.m.getNextValues(state, 'undefined')
        # Output of from self.m will be inputed to self.m again.
        (newS, ignore) = self.m.getNextValues(state, o)
        return (newS, o)

def makeCounter(init, step):
    return sm.Feedback(sm.Cascade(Increment(step), sm.Delay(init)))

