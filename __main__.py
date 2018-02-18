#!/usr/bin/env python

from STLcreator import model as mdl
import sys
import json

def main(template, parameters):
    try:
        template   = open(template, "r")
        parameters = open(parameters, "r")
    except:
        print("Error reading file.")

    try:
        template   = json.load(template)
        parameters = json.load(parameters)
    except:
        print("Error reading JSON")

    triangles = template[1]["triangles"]
    model = mdl.Model("face")
    
    for triangle in triangles:
        tempTriangle = mdl.Triangle()
        
        for vertex in triangle:
            triangleName = vertex
        
        verteces = []
        verteces.append(template[0]["vertex"][triangle[triangleName][0]])
        verteces.append(template[0]["vertex"][triangle[triangleName][1]])
        verteces.append(template[0]["vertex"][triangle[triangleName][2]])
        
        for vertex in verteces:
            xCoordinate = vertex[0]["x"]
            yCoordinate = vertex[1]["y"]
            zCoordinate = vertex[2]["z"]
            
            if type(xCoordinate) is str:
                xCoordinate = parameters[xCoordinate]
            
            if type(yCoordinate) is str:
                yCoordinate = parameters[yCoordinate]
            
            if type(zCoordinate) is str:
                zCoordinate = parameters[zCoordinate]
            
            tempTriangle.addVertex(xCoordinate, yCoordinate, zCoordinate)
        
        model.addTriangle(tempTriangle)
    
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
