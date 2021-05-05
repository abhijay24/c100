class car (object):
    def __init__(self, colour, company, speedlimit, model):
        self.colour = colour
        self.company = company
        self.speedlimit = speedlimit
        self.model = model
    def start(self):
        print("started")
    def stop (self) :
        print("stopped")
    def accelerate(self):
        print("acclerating")
    def changeGear(self):
        print("changed gear")
AUDI = car("black","audi","100","a6")
print(AUDI.colour)
    
    
        
