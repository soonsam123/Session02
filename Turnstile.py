class SM:
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
        return self.transduce([None]*n)
    

class Turnstile1(SM):
    startState = 'locked'
    def getNextValues(self, state, inp):
        if state == 'locked':
            if inp == 'coin':
                return ('unlocked', 'enter')
            else:         # Input == None
                return ('locked', 'pay')
        if state == 'unlocked':
            if inp == 'turn':
                return ('locked','pay')
            else:
                return ('unlocked','enter')
turn = Turnstile1()
print turn.transduce([None, None, 'coin', 'coin', 'turn', 'coin', 'turn', 'turn'])
# It properly work, now if you connect it into a turnstile it will work.
# AWESOME!!!
