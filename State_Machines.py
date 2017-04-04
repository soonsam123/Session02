# Name: Soon Sam R Santos
# Date: February 16, 2017
# Session: 2
# State_Machines.py

# State Machines: A modeling system whose output depends on the entire history of their inputs. For Robots we will try to capture just the most important points of the previous
# inputs to get the current and the next state.
# SM will be the superclass for all the specified machines class we create. This superclass doesn't say the behavior of the machine, that's why we do not instantiate it.
# there are just some useful methods.
# To specify the new type of State Machine, use the SM as a parent class.
# We must define an attribute startState which specifies the initial state of the machine and a method getNextValues which takes the state and input at time t
# and returns the state at time t + 1 and the output at time t.
class Accumulator(SM):
    startState = 0
    # Must be a pure function. Can't change the values of state, because we don't know how many times it will be called.
    def getNextValues(self, state, inp):
        return (state + inp, state + inp)
        # state + inp are accumalating the values.
        # the state at time t + 1 is the output at time t. State is like a support to make the calculation and then through to output.
        # the next state is the result of the sum of the actual value plus the input of the user. The output is the same thing.

# We could do a initialization to Accumulator
    def __init__(self, initilValue):
        self.startState = initialValue   # assigned as an instance of the method because it will be called many times in different values.
    def getNextValues(self, state, inp):
        return state + inp, state + inp
# >>> c = Accumulator(100)
# >>> c.start()
# >>> c.step(20)
# 120   # Because of the initial Value.
start, step, transduce, run
class SM:
    def start(self):
        # Setting the current state.
        self.state = self.startState
    def step(self, inp):
        # Making the machine do a cycle
        # Seting the values of the actual output and of the next state
        (s, o) = self.getNextValues(self, self.state, inp)
        # Changing the current state.
        self.state = s
        return o
    def transduce(self, inputs):
        # Same thing as above but doing for a list of inputs.
        self.start() # To set the first value o state
        return [self.step(inp) for inp in inputs]
    def run(self, n=10):
        # If the machine has no inputs
        return self.transduce([None]*n)
    # Default Values
    startState = None
    def getNextValues(self, state, inp):
        # We assume the next state is the same as the output.
        # In case of accumulator we would add state + inp as being the nextstate and we would return it again as being the output.
        nextState = self.getNextState(state, inp)
        return (nextState, nextState)

class Gain(SM):
    def __init__(self, k):
        self.k = k
    def getNextState(self, state, inp):
        # This is the next state, which turns out to be the same as the output because it is going to use the default value of SM superclass.
        return inp * self.k
#>>> g = Gain(3)
#>>> g.transduce([1.1, -2, 100,5])
#[3.3, -6, 300, 15]
class Accumulator(SM):
    startState = 0
    def getNextState(self, state, inp):
        return state + inp
    # This will be more succintly since I already know the output and the next state of the Accumulator are the same, therefore I can just use the getNextValues of the SM class.
    # I don't need anymore to calculate the output, I just calculate the nextstate.
