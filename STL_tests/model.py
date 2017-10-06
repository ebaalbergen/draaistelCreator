#!/usr/bin/env python

class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getSTLCode(self):
        return "vertex " + str(float(self.x)) + " " + str(float(self.y)) + " " + str(float(self.z))


class Triangle:
    def __init__(self):
        self.verteces = []

    def addVertex(self, x , y, z):
        self.verteces.append(Vertex(x, y, z))

    def getNormalVector(self):
        #return 0, 0, 0
        if len(self.verteces) != 3:
            raise Exception("Number of verteces in triangle is not three.\n\
                    Therefor the normal vector cannot be determend.")
        AA = self.verteces[1].x - self.verteces[0].x
        BB = self.verteces[1].y - self.verteces[0].y
        CC = self.verteces[1].z - self.verteces[0].z
        DD = self.verteces[2].x - self.verteces[0].x
        EE = self.verteces[2].y - self.verteces[0].y
        FF = self.verteces[2].z - self.verteces[0].z

        normalX = BB*FF-CC*EE 
        normalY = CC*DD-AA*FF
        normalZ = AA*EE-BB*DD
        return normalX, normalY, normalZ
    
    def getSTLCode(self):
        stlCode = ""

        normalX, normalY, normalZ = self.getNormalVector()
        stlCode += "facet normal "+str(normalX)+" "+str(normalY)+" "+str(normalZ)+"\n"
        stlCode += "outer loop\n"
        for vertex in self.verteces:
            stlCode += vertex.getSTLCode() + "\n"

        stlCode += "endloop\n"
        stlCode += "endfacet"

        return stlCode

class Model:
    def __init__(self, name):
        self.name = name
        self.triangles = []

    def addTriangle(self, triangle):
        self.triangles.append(triangle)

    def getSTLCode(self):
        stlCode = "solid " + self.name + "\n"
        for triangle in self.triangles:
            stlCode += triangle.getSTLCode() + "\n"
        stlCode += "endsolid"

        return stlCode

