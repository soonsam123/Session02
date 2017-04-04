# Name: Soon Sam R Santos
# Date: February 20, 2017
# Session: 2
# Lambda.py

# Lambda is used if you don't want to wast the space writing the function.
def square(x):
    return x*x
def selfComposition(some_function):
    def returnFunction(arg):
        # The function is called twice
        return (some_function(some_function(arg)))
    # return the value calculated above
    return returnFunction
f = selfComposition(square)
print f(2)
print selfComposition(square)(2)  # = returnFunction(2)
print selfComposition(lambda x : x*x)(2)  # lambda (argument it receives) : operation it does.
print selfComposition(lambda x : x + 1)(2)  # 4

demolist = [1,2,3,4,5]
# map returns a list of the function applied to the sequence of numbers.
# map(function, [list of values]) --> returns a list of function applyied to each [list of values]
print map(square,demolist)   # [1,4,9,16,25]
# By this time I writing the function where I should call it. I can do a bunch of things with just one line.
print map(lambda x : x*2, demolist)  # [1,2,6,8,10]
# pure function
print demolist              # [1,2,3,4,5]
# listcomprehension
print [(x,y) for x in demolist for y in demolist]  # 1 combined to the others, 2 combined to the others.... (very big)
# To copy
c = [1,2,3,4]
a = c[:]
# This is a copy, you can alter one without altering the other
