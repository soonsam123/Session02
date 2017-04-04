class AccountPounds:
    def __init__(self, ib):
        self.initial = ib
    def depositPounds(self, deposit):
        initial_D = self.initial*2
        deposit_D = deposit*2
        return (((initial_D + deposit_D)*1.1) - 0.3)/2
        

x = AccountPounds(1)
print x.depositPounds(1.5)
# 2.6
