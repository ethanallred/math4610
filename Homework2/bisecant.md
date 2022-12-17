Routine Name: bisecant.py

Author: Ethan Allred

Language: Python

bisecant.py

Description/Purpose: Finds the an approximate root.

Input: It takes a guess and an old guess for what the root might be.

Output: The output is an approximate value for the root and an old approximation.

Usage/Example: iteration of the secant and bisection methods to a set percent error

Implementation/Code: Call with bisecant(x0, x1)

def bisecant(x0, x1):
  hold0 = x0
  hold1 = x1

  holdarray = secantmethod(x0,x1)
  x0 = holdarray[0]
  x1 = holdarray[1]
  error = np.abs((x1 - x0)/x1)
  holdarray = secantmethod(x0, x1)
  x0 = holdarray[0]
  x1 = holdarray[1]
  error2 = np.abs((x1 - x0)/x1)


  if error2 > error:
    i = 0
    x0 = hold0
    x1 =hold1
    while i < 4:
      xr = (x0 + x1) / 2
      fx = function(xr)
      fx1 = function(x1)
      if (fx * fx1) <= 0:
        x0 = xr
      else:
        x1 = xr
      i = i + 1
  while error2 > 2:
    holdarray = secantmethod(x0, x1)
    x0 = holdarray[0]
    x1 = holdarray[1]
    error2 = np.abs((x1 - x0) / x1) * 100
  print(x1)
Last Modified: September/2022
