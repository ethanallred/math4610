Routine Name: newtonmethod

Author: Ethan Allred

Language: Python

newtonmethod.py
Description/Purpose:
Finds the an approximate root.

Input:
It takes a guess as to what one of the roots might be alog with the results of the function at ther guess and the derivative at the guess.

Output:
The out put is a approximate value for the root.

Usage/Example:
call for 1 iteration of the newton method

Implementation/Code:
Call with newtonmethod(x, func, deriv)

def newtonmethod(x, func, deriv):
x = x - func / deriv))
return x
Last Modified: September/2022
