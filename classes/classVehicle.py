class vehicle:

#constructor
    def __init__(self, mass, friction, velocity):
        self.mass = mass
        self.friction = friction
        self.velocity = velocity
        vehicle.amount += 1

#destructor
    def __del__(self):
        print("vehicle deleted!")
        vehicle.amount -= 1

#string method
    def __str__(self):
        return("Mass: {}, Friction: {}, Velocity: {}".format(self.mass, self.friction, self.velocity))

#decelaration method
    def getBreakDistance(args):
        if args.pdfFileName == "blub":
            print (1)
        if args.pdfFilePath == r"C:\Users\aigne\OneDrive\Dokumente\Git_Repo_FH\S2310710042" :
            print("passed  " + args.pdfFilePath)

    