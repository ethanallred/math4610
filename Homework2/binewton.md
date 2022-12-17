Routine Name: binewtonmethod

Author: Ethan Allred

Language: Python

binewton.py

Description/Purpose: Finds an approximate root. It takes a guess and tests the newton method on it. If it does not converge it swtiches to bisection for a little bit and then goes back to the newton method.

Input: a guess above and below the root.

Output: The output is an approximate value for the root.

Usage/Example: iteration of the newton method to a set percent error

Implementation/Code: Call with binewton(x0, x1)

def binewton(x0, x1):
    hold0 = x0
    hold1 = x1

    xr = newtonmethod(x0)
    error = np.abs((xr - x0)/xr)
    xr2 = newtonmethod(xr)
    error2 = np.abs((xr2 - xr) / xr)

    if error2 > error:
        i = 0
        x0 = hold0
        x1 = hold1
        while i < 4:
            xr = (x0+x1)/2
            fx = function (xr)
            fx1 = function (x1)
            if (fx * fx1) < 0:
                x0 = xr
            else:
                x1 = xr
            i = i + 1
    while error2 > 2:
        xhold = xr2
        xr2 = newtonmethod(xr2)
        error2 = np.abs((xr2 - xhold) / xr2) * 100
    print (xr2)
Last Modified: September/2022
