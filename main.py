#!/usr/bin/env python3

"""
{This script calculates the braking distance of a vehicle 
mass, speed, road type, weather conditions and gradient must be specified.}
"""

#import generic/built-in
import os
import sys
import argparse

#import owned
from classes.class_vehicle import Vehicle

__version__ = "0.1.0"
__email__ = "s2310710042@fhooe.at"
__author__ = "Bernhard Aigner S2310710042"

def create_arg_parser():
    """
    Raises:
        sys.exit: quits programm if path is not a valid path    

    Returns:
        _type_: commutated arguments from cli for default values and options press -h
    """
    #setup arg parser
    arg_parser = argparse.ArgumentParser(description="Plotter for brake distance and brake time")

    #file arguments
    arg_parser.add_argument("-pdfFileName", type=str, nargs='?', default = "Vehicle_Plot", help="filename (default: Vehicle_Plot)")
    arg_parser.add_argument("-pdfFilePath", type=str, nargs='?', default = os.getcwd(), help="location (default: current directory)")

    #vehicle arguments
    arg_parser.add_argument("mass", type=float, help="enter mass of vehicle [kg] (example: 1250.50)")
    arg_parser.add_argument("velocity", type=float, help="enter velocity of vehicle [km/h] (example: 50.5)")

    #Road type arguments with default values
    arg_parser.add_argument("-concrete", action="store_true", help="roadtype (default)")
    arg_parser.add_argument("-ice", action="store_true", help="roadtype")
    arg_parser.add_argument("-water", action="store_true", help="roadtype (aquaplaning)")
    arg_parser.add_argument("-gravel", action="store_true", help="roadtype (always dry)")
    arg_parser.add_argument("-sand", action="store_true", help="roadtype (always dry)")

    #additional arguments
    arg_parser.add_argument("--gradient", type=float, nargs='?', default = 0, help="enter gradient (example: 12.5 (default = 0))")
    arg_parser.add_argument("--wet", action="store_true", help="roadcondition (default: dry)")
    args = arg_parser.parse_args()
    
    try:
        os.path.realpath(args.pdfFilePath, strict=True)
    except ValueError as exc:
        raise sys.exit(1) from exc
    
    return args

def main():
    args = create_arg_parser()
    
    test_car = Vehicle(args)
    test_car.plot()
    
if __name__ == "__main__":
    main()
        