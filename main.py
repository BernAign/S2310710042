#!/usr/bin/env python3

"""
{This script calculates the braking distance of a vehicle 
mass, speed, road type, weather conditions and gradient must be specified.}
"""

#import generic/built-in
import os
import sys
import argparse
from pathlib import Path

#import owned
import skripts.vehicleCalculation as vehicleCalculation
from classes.classVehicle import Vehicle

__version__ = "0.1.0"
__email__ = "s2310710042@fhooe.at"
__author__ = "Bernhard Aigner S2310710042"



#setup arg parser
arg_parser = argparse.ArgumentParser(description="Plotter for break distance")
arg_parser.add_argument("pdfFileName", type=str, help="filename for plot")
arg_parser.add_argument("pdfFilePath", type=str, nargs='?', default = os.getcwd(), help="path to save plot (default: current directory)")

arg_parser.add_argument("mass", type=float, help="enter mass of vehicle [kg] (example: 1250.50)")
arg_parser.add_argument("friction", type=float, help="enter friction of vehicle wheels (example: 0.5)")
arg_parser.add_argument("velocity", type=float, help="enter velocity of vehicle [km/h] (example: 50.5)")


# Road type arguments with default values
arg_parser.add_argument("-concrete", type=bool, nargs='?', default = True, help="roadtype (default)")
arg_parser.add_argument("-ice", type=bool, nargs='?', default = True, help="roadtype")
arg_parser.add_argument("-water", type=bool, nargs='?', default = True, help="roadtype")
arg_parser.add_argument("-gravel", type=bool, nargs='?', default = True, help="roadtype (always dry)")
arg_parser.add_argument("-sand", type=bool, nargs='?', default = True, help="roadtype (always dry)")

arg_parser.add_argument("--wet", type=bool, nargs='?', default = False, help="roadcondition (default: dry)")

args = arg_parser.parse_args()
# print (args.pdf_file_name)
# print (args.pdf_file_path)

targetDir = Path(args.pdfFilePath)
if not targetDir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)


def main():
    blub = "test"
    test_car = Vehicle(args)
    test_car.get_brake_distance(args)

if __name__ == "__main__":
    main()