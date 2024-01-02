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

__version__ = "0.1.0"
__email__ = "s2310710042@fhooe.at"
__author__ = "Bernhard Aigner S2310710042"



#setup arg parser
argParser_ = argparse.ArgumentParser(description="Plotter for break distance")
argParser_.add_argument("pdfFileName", type=str, help="filename to plot")
argParser_.add_argument("pdfFilePath", type=str, nargs='?', default = os.getcwd(), help="filename to plot (default: current directory)")

# argParser_.add_argument("pdf_file_path", type=str, help="path to save file" )
args = argParser_.parse_args()
# print (args.pdf_file_name)
# print (args.pdf_file_path)

targetDir = Path(args.pdfFilePath)

if not targetDir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)


def main():

    vehicleCalculation.getBreakDistance(args)


if __name__ == "__main__":
    main()