from core.init import init
import sys
sys.path.append("..")  # Adds higher directory to python modules path.


class initClass:
    def __init__(self, parameter0, parameter1, parameter2):
        self.parameter0 = parameter0
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    def doInit(self):
        if (self.parameter0 in ['full']):
            if (self.parameter1 and self.parameter2):
                print(init.full(self.parameter1, self.parameter2))
            else:
                print('init full must have <Project> and <Origin> arguments')
        else:
            print(init.simple(self.parameter0, self.parameter1))
