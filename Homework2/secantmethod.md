Routine Name: secantmethod

Author: Ethan Allred

Language: Python

Input: A guess and old guess the function at guess and old guess.

Output: It returns a a root approximation and an old guess

Usage/Example:

Call the function with secantmethod(x0, x1, func0, func1) to run one iteration.

Implementation/Code:

def secantmethod(x0, x1, func0, func1)
xhold = x1
x1 = (func1 * (x0 -x1)) / (func0 - func1)
x0 = xhold

Last Modified: September/2022
