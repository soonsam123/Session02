class Hammock:
    def __init__(self):
        self.sit = 'empty'
        self.list = []
    def sitDown(self, name):
        if self.sit == 'empty':
            self.sit = 'ocupied'
            return 'welcome!'
        else:
            if name in self.list:
                return 'welcome!'
            else:
                self.list.append(name)
                return 'sorry, no room'
    def leave(self):
        if self.sit == 'ocupied':
            self.sit = 'empty'
            return 1
        else:
            return 0
myHammock = Hammock()
print myHammock.sitDown('George')
# welcome!
print myHammock.sitDown('Bobby')
# sorry, no room
print myHammock.sitDown('Bobby')
# welcome!
print myHammock.leave()
# 1
print myHammock.leave()
# 0
print myHammock.leave()
# 0
print myHammock.sitDown('Martha')
# welcome!
print myHammock.sitDown('Wilhelm')
# sorry, no room
print myHammock.sitDown('Klaus')
# sorry, no room
print myHammock.sitDown('Wilhelm')
# sorry, no room

