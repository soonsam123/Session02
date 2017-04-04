import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    startState = 'Free'
    def getNextValues(self, state, inp):
        print self.state
        if state == 'Free':
            # Center sonars are free to move.
            if inp.sonars[3]>=0.45 and inp.sonars[4]>=0.45:
                return ('Free', io.Action(fvel = 0.8, rvel = 0))
            else:
                # If they aren't, stop and goes to Boundarie Found.
                return ('Boundarie Found', io.Action(fvel = 0, rvel = 0))
            
        elif state == 'Boundarie Found':
            # Rotate until the right be less than 0.5.
            if inp.sonars[7]>=0.50:   
                return ('Boundarie Found', io.Action(fvel = 0, rvel = 0.3))
            elif inp.sonars[7]<=0.50 and inp.sonars[6]<=0.5:   
                return ('Boundarie Found', io.Action(fvel = 0, rvel = 0.3))
            else:
                return ('Following Boundarie', io.Action(fvel = 0, rvel = 0))
        elif state == 'Adjusting':
            # Keep adjusting while the most right is less than 0.5.
            if (inp.sonars[3]<=0.50 or inp.sonars[4]<=0.50):   
                return ('Adjusting', io.Action(fvel = 0, rvel = 0.3))
            # Keep adjusting while the center is less than 0.5.
            elif (inp.sonars[5]<=0.50 or inp.sonars[6]<=0.50):
                return ('Adjusting', io.Action(fvel = 0, rvel = 0.3))
            # If the most right is bigger than 0.5
            elif inp.sonars[5]>=0.50 and inp.sonars[6]>=0.50 and inp.sonars[7]<=0.5:
                return ('Following Boundarie', io.Action(fvel = 0, rvel = 0))

        elif state == 'Following Boundarie':
            # While sonar right is in the range and most right is bigger than 0.5.
            if 0.30<=inp.sonars[7]<=0.50 and (inp.sonars[5]>=0.50 or inp.sonars[6]>=0.50):        
                return ('Following Boundarie', io.Action(fvel = 0.3, rvel = 0))
            # Either the center is less than 0.5 or the most right. Works for the inside corner.
            elif (inp.sonars[3]<=0.50 or inp.sonars[4]<=0.50):
                # Stop and start to Adjust.
                return ('Adjusting', io.Action(fvel = 0, rvel = 0))
            elif (inp.sonars[5]<=0.50 or inp.sonars[6]<=0.50):
                return ('Adjusting', io.Action(fvel = 0, rvel = 0))
            # Outside Corner: If the right sonar goes to bigger than 0.5.
            elif inp.sonars[7]>=0.50: # It will come here only if, both most right are bigger and both centers are bigger.
                return ('Outside', io.Action(fvel = 0, rvel = 0))
            else:
                return ('Boundarie Found', io.Action(fvel = 0, rvel = 0))

        elif state == 'Outside':
            # Rotate clockwise while the right is greater than 0.5
            if inp.sonars[7]>=0.50:
                return ('Outside', io.Action(fvel = 0, rvel = -0.3))
            # Keep going straight.
            elif inp.sonars[7]<=0.5 and (inp.sonars[3]>=0.5 or inp.sonars[4]>=0.5):
                return ('Following Boundarie', io.Action(fvel = 0, rvel = 0))
            # An inside corner just after the outside corner.
            elif (inp.sonars[3]<=0.5 or inp.sonars[4]<=0.5):
                return ('Boundarie Found', io.Action(fvel = 0, rvel = 0))
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
