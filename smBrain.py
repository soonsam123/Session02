import math
import lib601.util as util
import lib601.sm as sm    # Importing the state machine class.
import lib601.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    def getNextValues(self, state, inp):
        # fvel : velocity forward(m/s). rvel : rotate velocity(rad/s)
        # If any of the sensors point 0.5 I should maintaing in this distance.
        #count = 0
        # Counting the quantity of sensors which are pointing less than 0.5 meters.
        #for i in range(8):
        #    if inp.sonars[i] <= 0.5:
        #        count = count + 1
        # I none are, keep going.
        #if count == 0:
        #    return (state, io.Action(fvel = 0.2, rvel = 0.5))
        # If one or more are, just stop to not shock.
        #else:
        return (state, io.Action(fvel = 0, rvel = -1))

mySM = MySMClass()
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False, # slime trails. If I put True, it will appear that window when I close the program
                                  sonarMonitor=True) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())

# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    # Sonars: 8 sensor list[0] --> the left most, list[7] --> the right most.
    for i in range(8):
        print inp.sonars[i]
    print "------------------------------------------------"
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass
