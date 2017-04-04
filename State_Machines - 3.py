# Name: Soon Sam R Santos
# Date: February 20, 2017
# Session: 2
# State_Machines - 3.py

class SM:
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
    def getNextValues(self, state, inp):
        newState = self.getNextState(state)
        return newState, newState

class Delay(SM):
    def __init__(self, v0):
        self.startState = v0
    def getNextValues(self, state, inp):  
        return (inp, state)

# TestCases
d = Delay(100)
print d.transduce([3,4,2,10,17,80])
# Working
class Increment(SM):
    startState = 0
    def __init__(self, k):
        self.k = k
    def getNextValues(self, state, inp):
        return (inp + self.k, inp + self.k)

# TestCases
i = Increment(1)
print i.transduce([1,2,3,4,5])

class Cascade(SM):
    startState = None
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)
    def getNextValues(self, state, inp):
        (s1, s2) = state
        # First Machine
        (nextS1, o1) = self.m1.getNextValues(s1, inp)
        # Second Machine
        (nextS2, o2) = self.m2.getNextValues(s2, o1)
        return ((nextS1,nextS2), o2)
# d is a Delay machine, i is an Increment machine.
c = Cascade(d,i)
print c.step(3)
