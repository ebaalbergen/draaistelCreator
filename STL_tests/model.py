#!/usr/bin/env python

# Class for representing a vertex. 
# Contains three floats to store the x, y and z coordinate.
class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Function to return the STL-code for the vertex.
    def getSTLCode(self):
        return "vertex " + str(float(self.x)) + " " + str(float(self.y)) + " " + str(float(self.z))


class Triangle:
    def __init__(self):
        self.verteces = []

    # Adds a new vertex to the triangle. Takes the x, y and z coordinates 
    # as inputs for the new vertex. Verteces should be added counter clockwise
    # as seen from when the normal vector points toward the camera.
    def addVertex(self, x , y, z):
        self.verteces.append(Vertex(x, y, z))

    # Takes the crossproduct of two vectors which span the surface of the face
    # to calculate a normal vector for that face.
    def getNormalVector(self):
        # Throw an exception when the face is not an complete triangle.
        if len(self.verteces) != 3:
            raise Exception("Number of verteces in triangle is not three.\n\
                    Therefor the normal vector cannot be determend.")

        # Calculate the values for the two vectors: (AA, BB, CC) 
        # and (DD, EE, FF)
        AA = self.verteces[1].x - self.verteces[0].x
        BB = self.verteces[1].y - self.verteces[0].y
        CC = self.verteces[1].z - self.verteces[0].z
        DD = self.verteces[2].x - self.verteces[0].x
        EE = self.verteces[2].y - self.verteces[0].y
        FF = self.verteces[2].z - self.verteces[0].z

        # Take the crossproduct to get the normal vector of the face
        normalX = BB*FF-CC*EE 
        normalY = CC*DD-AA*FF
        normalZ = AA*EE-BB*DD
        return normalX, normalY, normalZ
    
    # Function to get the STL-code for the face
    def getSTLCode(self):
        stlCode = ""
        # Define the face and define the normal of the face.
        normalX, normalY, normalZ = self.getNormalVector()
        stlCode += "facet normal "+str(normalX)+" "+str(normalY)+" "+str(normalZ)+"\n"
        
        # Begin looping over al the verteces and add their STL-codes to the face
        stlCode += "outer loop\n"
        for vertex in self.verteces:
            stlCode += vertex.getSTLCode() + "\n"

        stlCode += "endloop\n"

        # Closeoff the face and return the STL-code
        stlCode += "endfacet"
        return stlCode

class Model:
    def __init__(self, name):
        self.name = name
        self.triangles = []

    # Function to add a new triangle to a 3Dmodel.
    # Takes a triangle as a input.
    def addTriangle(self, triangle):
        self.triangles.append(triangle)

    # Function to get the STL-code for the complete model.
    # Loops over all the faces and adds the STL-code for those faces 
    # to the complete STL-code for the solid.
    def getSTLCode(self):
        stlCode = "solid " + self.name + "\n"
        for triangle in self.triangles:
            stlCode += triangle.getSTLCode() + "\n"
        stlCode += "endsolid"

        return stlCode

