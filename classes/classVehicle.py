from classes import constants

class Vehicle:
    
    amount = 0
       
    # constructor
    def __init__(self, args):
        self.mass = args.mass
        self.friction = self.set_roadtype(args)
        self.velocity = args.velocity
        Vehicle.amount += 1

    # destructor
    def __del__(self):
        print("vehicle deleted!")
        Vehicle.amount -= 1

    # string method
    def __str__(self):
        return "Mass: {}, Friction: {}, Velocity: {}".format(self.mass, self.friction, self.velocity)

    # deceleration method
    def get_brake_distance(self):
        if self.mass == 1500.0:
            print(self.friction)
        # if args.pdfFilePath == r"C:\Users\aigne\OneDrive\Dokumente\Git_Repo_FH\S2310710042":
        #     print("passed  " + args.pdfFilePath)
        
    def set_roadtype(self, args):
        if(args.concrete and not args.wet):
            return constants.CONCRETE_DRY
        elif(args.concrete and args.wet):
            return constants.CONCRETE_WET
        elif(args.ice and not args.wet):
            return constants.ICE_DRY
        elif(args.ice and args.wet):
            return constants.ICE_WET
        elif(args.water):
            return constants.WATER
        elif(args.gravel):
            return constants.GRAVEL
        elif(args.sand):
            return constants.SAND


  