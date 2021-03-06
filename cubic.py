#!/usr/bin/env python

# from https://www.physics.rutgers.edu/~masud/computing/WPark_recipes_in_python.html

"""
cbrt(x) = x^{1/3},  if x >= 0
        = -|x|^{1/3},  if x < 0
"""
def cbrt(x):
    from math import pow
    q = x.magnitude
    if type(q) == complex:
      q = q.real
    if q >= 0: 
        return x ** (1.0/3.0)
    else:
        return -abs(x)** (1.0/3.0)


"""
Convert from rectangular (x,y) to polar (r,w)
    r = sqrt(x^2 + y^2)
    w = arctan(y/x) = [-\pi,\pi] = [-180,180]
"""
def polar(x, y, deg=0):         # radian if deg=0; degree if deg=1
    from math import hypot, atan2, pi
    if deg:
        return hypot(x, y), 180.0 * atan2(y, x) / pi
    else:
        return hypot(x, y), atan2(y, x)


"""
x^2 + ax + b = 0  (or ax^2 + bx + c = 0)
By substituting x = y-t and t = a/2, the equation reduces to 
    y^2 + (b-t^2) = 0 
which has easy solution
    y = +/- sqrt(t^2-b)
"""
def quadratic(a, b, c=None):
    import math, cmath
    if c:               # (ax^2 + bx + c = 0)
        a, b = b / (a), c / (a)
    t = a / 2.0
    r = t**2 - b

    q = r.magnitude
    if type(q) == complex:
      q = q.real
    if q >= 0:          # real roots
        y1 = r ** 0.5
    else:               # complex roots
        y1 = cmath.sqrt(r.magnitude) * (abs(r)** 0.5)/(abs(r).magnitude**0.5)
    y2 = -y1
    return y1 - t, y2 - t

"""
x^3 + ax^2 + bx + c = 0  (or ax^3 + bx^2 + cx + d = 0)
With substitution x = y-t and t = a/3, the cubic equation reduces to    
    y^3 + py + q = 0,
where p = b-3t^2 and q = c-bt+2t^3.  Then, one real root y1 = u+v can
be determined by solving 
    w^2 + qw - (p/3)^3 = 0
where w = u^3, v^3.  From Vieta's theorem,
    y1 + y2 + y3 = 0
    y1 y2 + y1 y3 + y2 y3 = p
    y1 y2 y3 = -q,
the other two (real or complex) roots can be obtained by solving
    y^2 + (y1)y + (p+y1^2) = 0
"""
def cubic(a, b, c, d=None):
    from math import cos
    if d:                                     # (ax^3 + bx^2 + cx + d = 0)
        a, b, c = b / (a), c / (a), d / (a)
    t = a / 3.0
    p, q = b - 3 * t**2, c - b * t + 2 * t**3
    u, v = quadratic(q, -(p/3.0)**3)
    if type(u) == type(0j):                   # complex cubic root
        r, w = polar(u.real, u.imag)
        y1 = 2 * cbrt(r) * cos(w / 3.0)
    else:                                     # real root
        y1 = cbrt(u) + cbrt(v)
    y2, y3 = quadratic(y1, p + y1**2)
    return y1 - t, y2 - t, y3 - t

