# Name: Soon Sam R Santos
# Date: February 20, 2017
# Session: 2
# Lecture_1.py

def increment(n):
    return n + 1
def square(n):
    return n**2

# This first method use three loops. Although it is working, you can easily lose yourself.
def findSequence(initial, goal):  # findSequence(1, 100)
    # candidates = [str(1), 1]
    candidates = [(str(initial), initial)]
    # for i in range (1, 100) Quantity of terms between both values.
    for i in range(1, goal-initial+1):
        newCandidates = []
        for (action, result) in candidates:
            # action = 1 result = 1
            for (a,r) in [(' increment', increment),(' square', square)]:
                # '1 increment increment', 'square' square(1)
                newCandidates.append((action+a,r(result)))
                # 1: '1 increment' = 2
                print i, ': ',newCandidates[-1]
                if newCandidates[-1][1] == goal:
                    return newCandidates[-1]

        candidates = newCandidates
answer = findSequence(1,100)
print 'answer: ', answer

print "------------------------------------------------" # Organazing

# Another way by Functional Programming
# Greater modularity, easier for debugging. Debug each function easier than debug all
# Clarity of thought 
def apply(opList, arg):
    if len(opList)==0:
        return arg
    else:
        # First list position is the argument applyied to the argument is just the argument.
        # The rest of the list will be the operations to do with the argument.
        # Recursion: much easier
        return apply(opList[1:],opList[0](arg))
def addLevel(opList, fctList):
    return [x+[y] for y in fctlist for x in opList]
def findSequence(initial, goal):
    opList = [[]]
    for i in range(1, goal-initial+1):
        opList = addLevel(opList,[increment, square])
        for seq in opList:
            if apply(seq, initial) == goal:
                return seq

# State Machine. Higher level
