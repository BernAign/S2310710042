class Vehicle:
    amount = 0
       # constructor
    def __init__(self, args):
        self.mass = args.mass
        self.friction = args.friction
        self.velocity = args.velocity
        Vehicle.amount += 1
        print(args.mass)

    # destructor
    def __del__(self):
        print("vehicle deleted!")
        Vehicle.amount -= 1

    # string method
    def __str__(self):
        return "Mass: {}, Friction: {}, Velocity: {}".format(self.mass, self.friction, self.velocity)

    # deceleration method
    def get_brake_distance(self, args):
        if args.pdfFileName == "blub":
            print(1)
        if args.pdfFilePath == r"C:\Users\aigne\OneDrive\Dokumente\Git_Repo_FH\S2310710042":
            print("passed  " + args.pdfFilePath)