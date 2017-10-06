#!/usr/bin/env python

import model

def main():
    model1 = model.Model("Cube")
    
    triangle1 = model.Triangle()
    triangle1.addVertex(0, 0, 0)
    triangle1.addVertex(1, 0, 0)
    triangle1.addVertex(1, 1, 0)
    model1.addTriangle(triangle1)

    triangle2 = model.Triangle()
    triangle2.addVertex(0, 0, 0)
    triangle2.addVertex(1, 1, 0)
    triangle2.addVertex(0, 1, 0)
    model1.addTriangle(triangle2)

    triangle3 = model.Triangle()
    triangle3.addVertex(0, 0, 0)
    triangle3.addVertex(1, 0, 1)
    triangle3.addVertex(1, 0, 0)
    model1.addTriangle(triangle3)

    triangle4 = model.Triangle()
    triangle4.addVertex(0, 0, 0)
    triangle4.addVertex(0, 0, 1)
    triangle4.addVertex(1, 0, 1)
    model1.addTriangle(triangle4)

    triangle5 = model.Triangle()
    triangle5.addVertex(0, 0, 1)
    triangle5.addVertex(1, 1, 1)
    triangle5.addVertex(1, 0, 1)
    model1.addTriangle(triangle5)

    triangle6 = model.Triangle()
    triangle6.addVertex(0, 0, 1)
    triangle6.addVertex(0, 1, 1)
    triangle6.addVertex(1, 1, 1)
    model1.addTriangle(triangle6)

    triangle7 = model.Triangle()
    triangle7.addVertex(0, 1, 1)
    triangle7.addVertex(0, 1, 0)
    triangle7.addVertex(1, 1, 1)
    model1.addTriangle(triangle7)

    triangle8 = model.Triangle()
    triangle8.addVertex(1, 1, 1)
    triangle8.addVertex(1, 1, 0)
    triangle8.addVertex(0, 1, 0)
    model1.addTriangle(triangle8)

    triangle9 = model.Triangle()
    triangle9.addVertex(1, 0, 0)
    triangle9.addVertex(1, 0, 1)
    triangle9.addVertex(1, 1, 1)
    model1.addTriangle(triangle9)

    triangle10 = model.Triangle()
    triangle10.addVertex(1, 0, 0)
    triangle10.addVertex(1, 1, 1)
    triangle10.addVertex(1, 1, 0)
    model1.addTriangle(triangle10)

    triangle11 = model.Triangle()
    triangle11.addVertex(0, 0, 1)
    triangle11.addVertex(0, 0, 0)
    triangle11.addVertex(0, 1, 1)
    model1.addTriangle(triangle11)

    triangle12 = model.Triangle()
    triangle12.addVertex(0, 0, 0)
    triangle12.addVertex(0, 1, 0)
    triangle12.addVertex(0, 1, 1)
    model1.addTriangle(triangle12)

    print(model1.getSTLCode())

if __name__ == "__main__":
    main()

