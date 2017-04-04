import lib601.sm as sm

##################################
# Double Delay SM
##################################

class Delay2Machine(sm.SM):
    def __init__(self, val0, val1):
        self.startState = (val0, val1)
    def getNextValues(self, state, inp):
        (previousPreviousInput, previousInput) = state
        return ((previousInput, inp), previousPreviousInput) 
  

def runTestsDelay():
    # Testcases for Delay2Machine using transduce.
    print 'Test1:', Delay2Machine(100, 10).transduce([1,0,2,0,0,3,0,0,0,4])
    print 'Test2:', Delay2Machine(10, 100).transduce([0,0,0,0,0,0,1])
    print 'Test3:', Delay2Machine(-1, 0).transduce([1,2,-3,1,2,-3])
    # Test that self.state is not being changed.
    m = Delay2Machine(100, 10)
    m.start()
    [m.getNextValues(m.state, i) for i in [-1,-2,-3,-4,-5,-6]]
    print 'Test4:', [m.step(i) for i in [1,0,2,0,0,3,0,0,0,4]]
print runTestsDelay()
# execute runTestsDelay() to carry out the testing, you should get:
#Test1: [100, 10, 1, 0, 2, 0, 0, 3, 0, 0]
#Test2: [10, 100, 0, 0, 0, 0, 0]
#Test3: [-1, 0, 1, 2, -3, 1]
#Test4: [100, 10, 1, 0, 2, 0, 0, 3, 0, 0]

# DONE!

##################################
# Comments SM
##################################

x1 = '''def f(x):  # func
   if x:   # test
     # comment
     return 'foo' '''

x2 = '''#initial comment
def f(x):  # func
   if x:   # test
     # comment
     return 'foo' '''


class CommentsSM(sm.SM):
    # Don't need to initializate because you have no value to begin.
    startState = 'close'
    # I choose the state close: when it is not a comment. and opne: when it is a comment.
    def getNextValues(self, state, inp):
        if inp == '#':
            if state == 'close':
                return ('open', inp)
        elif inp == '\n':
            if state == 'open':
                return ('close', None)
        else:
            if state == 'open':
                return ('open', inp)
            if state == 'close':
                return ('close', None)
            
            
                        
        
 

def runTestsComm():
    m = CommentsSM()
    # Return only the outputs that are not None
    print 'Test1:',  [c for c in CommentsSM().transduce(x1) if not c==None]
    print 'Test2:',  [c for c in CommentsSM().transduce(x2) if not c==None]
    # Test that self.state is not being changed.
    m = CommentsSM()
    m.start()
    [m.getNextValues(m.state, i) for i in ' #foo #bar']
    print 'Test3:', [c for c in [m.step(i) for i in x2] if not c==None]
print runTestsComm()
# execute runTestsComm() to carry out the testing, you should get:

#Test1: ['#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
#Test2: ['#', 'i', 'n', 'i', 't', 'i', 'a', 'l', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
#Test3: ['#', 'i', 'n', 'i', 't', 'i', 'a', 'l', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']

# DONE!

##################################
# First Word SM
##################################

# Test 1
test1 = '''hi
ho'''
# This can also be writtent as:
# test1 = 'hi\nho'

#Test 2
test2 = '''  hi
ho'''
# This can also be writtent as:
# test2 = '  hi\nho'

#Test 3
test3  = '''

 hi
 ho ho ho

 ha ha ha'''
# This can also be writtent as:
# test3 ='\n\n hi \nho ho ho\n\n ha ha ha'

class FirstWordSM(sm.SM):
    # States I am looking for the first word.
    startState = 'looking'
    def getNextValues(self, state, inp):
        if inp == ' ':
            
            # Looking for still.
            if state == 'looking':
                # Keep saying I am still looking for.
                return ('looking', None)
            
            # Regardless of the state now, I am not looking for anymore.
            # Therefore I'll just say 'not' and None.
            else:
                return ('not', None)
        elif inp == '\n':

            # Regardless of the state, it should start to look for again.
                return ('looking', None)
        
        else:

            # I am looking for the first word.
            if state == 'looking':
                # Found the first word.
                return ('found', inp)

            # Keep showing what the first word is.
            if state == 'found':
                return ('found', inp)

            # I already did my job with the first word.
            if state == 'not':
                return ('not', None)

def runTestsFW():
    m = FirstWordSM()
    print 'Test1:', m.transduce(test1)
    print 'Test2:', m.transduce(test2)
    print 'Test3:', m.transduce(test3)
    m = FirstWordSM()
    m.start()
    [m.getNextValues(m.state, i) for i in '\nFoo ']
    print 'Test 4', [m.step(i) for i in test1]

print runTestsFW()
# execute runTestsFW() to carry out the testing, you should get:

# HINT: I just needed to recognize that I would need to use three states instead of 2. I can use as many states I want...
# states --> looking for the first word, already found the first word, I am not in the first word anymore.
# DONE!


#Test1: ['h', 'i', None, 'h', 'o']
#Test2: [None, None, 'h', 'i', None, 'h', 'o']
#Test3: [None, None, None, 'h', 'i', None, None, 'h', 'o', None, None, None, None, None, None, None, None, None, 'h', 'a', None, None, None, None, None, None]
#Test4: ['h', 'i', None, 'h', 'o']
