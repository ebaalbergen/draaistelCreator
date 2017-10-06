#!/usr/bin/env python

import STLcreator
import sys

def main(template, parameters):
    model = STLcreator.Model("face")
    triangle1 = STLcreator.Triangle()
    triangle1.addVertex(0, 0, 0)
    triangle1.addVertex(1, 0, 0)
    triangle1.addVertex(0, 1, 0)
    model.addTriangle(triangle1)
    return model.getSTLCode()

def saveFile(filename, string):
    try:
        outputfile = open(filename, "w")
        outputfile.write(string)
        outputfile.close
    except:
        print("Error 0x01: writing outputfile!")

if __name__ == "__main__":
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Program called with too little or too much arguments.\n\
The program should be called with 2 or 3 parameters\n\
\n\
$ python " + __name__ + ".py template parameters [outputfile]\n\
First parameter: Template file\n\
Second parameter: Parameter file\n\
Thirth parameter (optional): Output file (STL)\n\
\n\
The thirth parameter is optional and is used to determen\n\
how the result will be stored (STL-file or std-out)\n\
Recommended is to use the STL-file as an output. std-out\n\
will not be stored except when you copy the code by yourself\n\
using the std-out output mode is recommended for \n\
debugging purposes only.")
    else:
        result = main(sys.argv[1], sys.argv[2])
        if len(sys.argv) == 4:
            saveFile(sys.argv[3], result)
        else:
            print(result)
