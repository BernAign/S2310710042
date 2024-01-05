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
import classes.classVehicle as vehicle

__version__ = "0.1.0"
__email__ = "s2310710042@fhooe.at"
__author__ = "Bernhard Aigner S2310710042"



#setup arg parser
argParser_ = argparse.ArgumentParser(description="Plotter for break distance")
argParser_.add_argument("pdfFileName", type=str, help="filename for plot")
argParser_.add_argument("pdfFilePath", type=str, nargs='?', default = os.getcwd(), help="path to save plot (default: current directory)")

argParser_.add_argument("mass", type=float, help="enter mass of vehicle [kg] (example: 1250.50)")
# argParser_.add_argument("friction", type=float, help="enter friction of vehicle wheels (example: 0.5)")
argParser_.add_argument("velocity", type=float, help="enter velocity of vehicle [km/h] (example: 50.5)")


# Road type arguments with default values
argParser_.add_argument("-concrete", type=bool, nargs='?', default = True, help="roadtype (default)")
argParser_.add_argument("-ice", type=bool, nargs='?', default = True, help="roadtype")
argParser_.add_argument("-water", type=bool, nargs='?', default = True, help="roadtype")
argParser_.add_argument("-gravel", type=bool, nargs='?', default = True, help="roadtype (always dry)")
argParser_.add_argument("-sand", type=bool, nargs='?', default = True, help="roadtype (always dry)")

argParser_.add_argument("--wet", type=bool, nargs='?', default = False, help="roadcondition (default: dry)")


# argParser_.add_argument("pdf_file_path", type=str, help="path to save file" )
args = argParser_.parse_args()
# print (args.pdf_file_name)
# print (args.pdf_file_path)

targetDir = Path(args.pdfFilePath)

if not targetDir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)
    


def main():

    vehicle(args)


if __name__ == "__main__":
    main()