#import system libs
import os
#import math and plot modules
import numpy as np
import matplotlib.pyplot as plt
#own modules
from classes import constants

class Vehicle:
    """Class representing a Vehicle"""
    amount = 0 
    # constructor
    def __init__(self, args):
        self.name = args.pdfFileName
        self.path = args.pdfFilePath
        self.mass = args.mass
        self.gradient = np.deg2rad(args.gradient)
        self.friction = self.set_roadtype(args)
        self.velocity = args.velocity
        # self.deceleration = constants.GRAVITATIONAL_ACCELERATION * self.friction
        self.deceleration = constants.GRAVITATIONAL_ACCELERATION*(np.sin(self.gradient)-np.cos(self.gradient)*self.friction)+self.velocity*self.deceleration_time
        self.deceleration_time = np.linspace(0, self.velocity/self.deceleration, 100, endpoint=True)
        Vehicle.amount += 1
        print(self.deceleration)

    # destructor
    def __del__(self):
        Vehicle.amount -= 1

    # string method
    def __repr__(self):
        return f"Mass: {self.mass}, Friction: {self.friction}, Velocity: {self.velocity}"
        
    def  get_brake_velocity(self):
        """
        Returns:
            float: returns an array with 100 timestamps based on v(t)=v-a*t
                   from v0 to 0
        """
        brake_velocity = self.velocity - self.deceleration * self.deceleration_time
        print(brake_velocity)
        return brake_velocity
    
    # deceleration method
    def get_brake_distance(self):
        """
        Returns:
            float:  returns an array with 100 timestamps based on s(t)=1/2*(t(2*v-a*t)
                    from s0 to absolute standstill
        """
        brake_distance = 0.5 * (self.deceleration_time*(2 * self.velocity - self.deceleration * self.deceleration_time))
        return brake_distance
    
    def plot(self):
        """        
        Returns:
            float: fig based on matplotlib
                   takes two arguments for ordinate 
                   will return a list with two plots over time

        """
        
        #default figure size A4
        fig, axs = plt.subplots(1, 2, figsize=(11.69, 8.27))
        x_time = self.deceleration_time
        y_deceleration = self.get_brake_velocity()
        y_distance = self.get_brake_distance()
        axs[0].plot(x_time, y_deceleration)
        axs[1].plot(x_time, y_distance)
        axs[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
        axs[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

        axs[0].plot(x_time[-1], y_deceleration[-1], 'ro', label=f'{x_time[-1]:.3f} [s]') 
        axs[1].plot(x_time[-1], y_distance[-1], 'ro', label=f'{y_distance[-1]:.3f} [m]')
        
        axs[0].set_xlabel('Time [s]')
        axs[0].set_ylabel('Deceleration [m/s^2]')
        axs[1].set_xlabel('Time [s]')
        axs[1].set_ylabel('Distance [m]')

        axs[0].legend()
        axs[1].legend()
        plt.show()
        self.saver(fig)
                    
    def set_roadtype(self, args):
        """
        Args:
            args (bool): gets from the cli which roadtype
                            and if wet
        Returns:
            float: a constant with the chosen roadtype
        """
        if(args.concrete and not args.wet):
            return constants.CONCRETE_DRY
        elif(args.concrete and args.wet):
            return constants.CONCRETE_WET
        elif(args.ice and not args.wet):
            return constants.ICE_DRY
        elif(args.ice and args.wet):
            return constants.ICE_WET
        elif args.water:
            return constants.WATER
        elif args.gravel:
            return constants.GRAVEL
        elif args.sand:
            return constants.SAND
        
    def saver(self, fig):
        """saves the shown plot as pdf;
            if permission error with your given path it will 
            create an output directory in your user documents
            named plot           
        Args:
            fig (matplotlib fig): contains a list with two plots over time
        """
        try:
            file_path_and_name = os.path.join(self.path, self.name+".pdf")
            fig.savefig(file_path_and_name, dpi=300, format='pdf')
        except PermissionError:
            output_directory = os.path.join(os.path.expanduser('~'), 'Documents', 'plots')
            os.makedirs(output_directory, exist_ok=True)
            file_path_and_name = os.path.join(output_directory, self.name+".pdf")
            fig.savefig(file_path_and_name, dpi=300, format='pdf')
# End-of-file (EOF)
