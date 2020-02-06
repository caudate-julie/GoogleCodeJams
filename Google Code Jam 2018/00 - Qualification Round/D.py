# Julie
# April, 7, 2018
# Qualification Round
# "Cubic UFO"

from math import sin, cos, sqrt, pi, atan
from copy import copy


PRECISION = 1e-7
aleph = atan(1/sqrt(2))
vertices = ((pi/4, aleph), (pi/4, -aleph), (3*pi/4, aleph), (3*pi/4, -aleph),
            (5*pi/4, aleph), (5*pi/4, -aleph), (7*pi/4, aleph), (7*pi/4, -aleph))
r = sqrt(3) / 2

def PointsByAngles(phi, psi):
    return ((0.5 * cos(phi) * cos(psi), 0.5 * sin(phi) * cos(psi), 0.5 * sin(phi) * sin(psi)),
            (-0.5 * sin(phi), 0.5 * cos(phi) * cos(psi), 0.5 * cos(phi) * sin(psi)),
            (0, -0.5 * sin(psi), 0.5 * cos(psi)))


def GetConvex(points):
    points = list(copy(points))
    convex = [points.pop()]
    while points:
        x0, y0 = convex[-1]
        ux, uy = convex[0][0] - x0, convex[0][1] - y0
        i_next = -1
        for i in range(len(points)):
            vx, vy = points[i][0] - x0, points[i][1] - y0
            if ux * vy - vx * uy >= 0:
                ux, uy, i_next = vx, vy, i
        if i_next == -1:
            break
        convex.append(points.pop(i_next))
    convex.append(convex[0])
    return convex


def TriangleArea(A, B, C):
    return abs(A[0] * (B[1]-C[1]) + B[0] * (C[1]-A[1]) + C[0] * (A[1]-B[1])) / 2

def Area(phi, psi):
    projecs = [(r * cos(phi_0 + phi) * cos(psi_0), 
                r * sin(phi_0 + phi) * cos(psi_0) * sin (psi) + r * sin(psi_0) * cos(psi)) 
        for phi_0, psi_0 in vertices]
    convex = GetConvex(projecs)
    return sum(TriangleArea(convex[i], convex[i+1], convex[-1]) for i in range(0, len(convex)-2))
    


def RotateZ(A):
    lower = 0
    upper = pi/4
    mid = lower + (upper - lower) / 2
    area = Area(mid, 0)
    while abs(area - A) > PRECISION:
        if area < A:
            lower = mid
        else:
            upper = mid
        mid = lower + (upper - lower) / 2
        area = Area(mid, 0)
    return mid

def RotateX(A):
    lower = 0
    upper = aleph
    mid = lower + (upper - lower) / 2
    area = Area(pi/4, mid)
    while abs(area - A) > PRECISION:
        if area < A:
            lower = mid
        else:
            upper = mid
        mid = lower + (upper - lower) / 2
        area = Area(pi/4, mid)
    return mid


def CubicUfo(A):
    if A < sqrt(2):
        return PointsByAngles(RotateZ(A), 0)
    else:
        return PointsByAngles(pi/4, RotateX(A))



T = int(input())
for case in range(1, T + 1):
    A = float(input())
    result = CubicUfo(A)
    answer = ('Case #%d:\n' % case) + '\n'.join(' '.join('%.9f' % y for y in x) for x in result)
    print(answer)
