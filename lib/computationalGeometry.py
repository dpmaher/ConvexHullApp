# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 19:12:13 2018

@author: Daniel Maher

This file contains some methods for 2D computational geometry problems
"""


import queue as Q
import random as rand

class Point2D:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __eq__(self, v):
        if self.x == v.x and self.y == v.y:
            return True
        return False

    def __str__(self):
        s = "(%.3f, %.3f)" % (self.x, self.y)
        return s

    def __repr__(self):
        return str(self)

"""
CLASS: Point2DLeftRightNode; Point2DRightLeftNode

Wrapper classes that define the Point2D comparator used for the PriorityQueue

Many computational geometry problems require sorting the point set in a 
lowest-to-highest or highest-to-lowest order according to X or Y coordinate
"""
class Point2DLeftRightNode:
    def __init__(self, point):
        self.point = point

    def __lt__(self, node):
        if self.point.x < node.point.x:
            return True
        elif self.point.x == node.point.x:
            if self.point.y < node.point.y:
                return True
        return False

class Point2DRightLeftNode:
    def __init__(self, point):
        self.point = point
    
    def __lt__(self, node):
        if self.point.x > node.point.x:
            return True
        elif self.point.x == node.point.x:
            if self.point.y < node.point.y:
                return True
        return False

"""
FUNCTION: is_right_turn

Helper function for determining if traversing points r, s, and t (in that order) forms a "right turn"
"""    
def is_right_turn(r, s, t):
    """
    check if determinant of following is < 0:
        | 1 r.x r.y |
        | 1 s.x s.y |
        | 1 t.x t.y |
    """
    det = ((s.x * t.y) - (t.x * s.y)) - r.x * (t.y - s.y) + r.y * (t.x - s.x)
    return det < 0;


"""
FUNCTION: compute_partial_hull

Computes partial convex hull

Inputs: points <list<Point2D>> - a list of points
        isUpper <boolean> - boolean value indicates whether partial hull is upper or lower hull
        
Output: pHull <list<Point2D>> - list of points on the convex hull of input points, listed in clockwise order
                                (if isUpper=True, points listed from left to right; else, points listed from right to left)
"""
def compute_partial_hull(points, isUpper):
    pq = Q.PriorityQueue()
    pHull = []
    
    # sort points by lowest x-coordinate or highest x-coordinate, depending on isUpper value
    for p in points:
        if isUpper:
            pq.put(Point2DLeftRightNode(p))
        else:
            pq.put(Point2DRightLeftNode(p))
    
    pHull.append(pq.get().point)
    pHull.append(pq.get().point)
    
    # find all widest right turns, starting from from the two rightmost or leftmost (depending on isUpper) points
    while not pq.empty():
        s = pHull.pop()
        r = pHull.pop()
        t = pq.get().point
        
        right = is_right_turn(r,s,t)
        while not right:
            if len(pHull) == 0:
                pHull.append(r)
                pHull.append(t)
                break;
            s = r
            r = pHull.pop()
            right = is_right_turn(r,s,t)
        
        if right:
            pHull.append(r)
            pHull.append(s)
            pHull.append(t)
    
    return pHull
    

"""
Computes convex hull of input list of points
"""
def compute_convexhull(points):
    
    if len(points) <= 2:
        return points
    
    uhull = compute_partial_hull(points, isUpper=True)
    lhull = compute_partial_hull(points, isUpper=False)
    
    return uhull + lhull[1:-1]



"""
Convert 2 lists of number values into list of Point2D

Inputs: 
    xList <list<float>> : a list of floats representing the x values of
        the output points
    yList <list<float>> : a list of floats representing the y values of
        the output points

Output:
    points <list<Point2D>> : a list of points
"""
def form_point_list(xList, yList):
    numpts = len(xList)
    points = []
    for i in range(numpts):
        points.append(Point2D(xList[i], yList[i]))
        
    return points
