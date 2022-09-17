import numpy as np
import math
import tabulate
from tabulate import tabulate
def function1 (x):
    '''
    Function: Function 1

    Summary: Solves Xe(-x) with the input of x
    :param x:
    :type x: float
    :return f:
    :rtype: float

    '''
    f = x * math.pow(np.e , -x)
    return f
def function2 (x):
    '''
    Function: Function 2

    Summary: Solves 10.14 * e(^(x^(2)))cos(pi/x)

    :param x:
    :type x: float
    :return f:
    :rtype: float

    '''
    f = 10.14*math.pow(np.e, x^2)* np.cos(np.pi/x)
    return f
def fixed1original(x,f,root):
    '''
        Function: fixed 1 original

        Summary:  Runs first fixed point equation, and prints a table
                of the results. Solves 10.14 * e(^(x^(2)))cos(pi/x)
        :param x:
        :type x: float
        :param: f
        :type f: float
        :param: root
        :type root: float

        '''
    maxit = 50
    tol = 0.02
    err = 1
    i = 0
    table =[]
    table.append(['i','x','e'])
    while err > tol and i < maxit:
        g = x - f
        err = abs(g - root)
        x = g
        i = i + 1
        table.append([str(i),str(x),str(err)])
    print("Table for fixed method 1")
    print(tabulate(table))

def fixed2original(x,f,root):
    '''
        Function: fixed 2 original

        Summary: Runs second fixed point equation, and prints a table
                of the results. Solves 10.14 * e(^(x^(2)))cos(pi/x)
        :param x:
        :type x: float
        :param: f
        :type f: float
        :param: root
        :type root: float

    '''
    maxit = 50
    tol = 0.02
    err = 1
    i = 0
    table = []
    table.append(['i', 'x', 'e'])
    while err > tol and i < maxit:
        g = x + f
        err = abs(g - root)
        x = g
        i = i + 1
        table.append([str(i), str(x), str(err)])
    print("Table for fixed method 2")
    print(tabulate(table))

def fixed1fix(x,f,root):
    '''
        Function: fixed 1 fix

        Summary: Runs a modified version of the first fixed point equation,
            and prints a table of the results. Solves 10.14 * e(^(x^(2)))cos(pi/x)

        :param x:
        :type x: float
        :param: f
        :type f: float
        :param: root
        :type root: float

    '''
    maxit = 50
    tol = 0.02
    err = 1
    i = 0
    table = []
    table.append(['i', 'x', 'e'])
    while err > tol and i < maxit:
        g = 0.01 * x - f
        err = abs(g - root)
        x = g
        i = i + 1
        table.append([str(i), str(x), str(err)])
    print("Table for adjusted fixed method 1")
    print(tabulate(table))

def fixed2fix(x,f,root):
    '''
        Function: fixed 2 fix

        Summary: Runs a modified version of the second fixed point equation,
            and prints a table of the results. Solves 10.14 * e(^(x^(2)))cos(pi/x)

        :param x:
        :type x: float
        :param: f
        :type f: float
        :param: root
        :type root: float

        '''
    maxit = 50
    tol = .02
    err = 1
    i = 0
    table = []
    table.append(['i', 'x', 'e'])
    while err > tol and i < maxit:
        g = -0.1 * x + f
        err = abs(g - root)
        x = g
        i = i + 1
        table.append([str(i), str(x), str(err)])
    print("Table for adjusted fixed method 2")
    print(tabulate(table))

def bihowmanyit(tol,a,b):
    '''
        Function: bi how many it

        Summary: Finds how many iterations the bi section method will have to take

        :param: tol
        :type tol: float
        :param: a
        :type a: float
        :param: b
        :type b: float
        :return k:
        :rtype: float

    '''
    k = (np.log(tol)/np.log(b-a))/(-np.log(2))+1
    return k

def bisection(a,b,k):
    '''
        Function: bisection

        Summary: Runs the bi section method

        :param: a
        :type a: float
        :param: b
        :type b: float
        :param: k
        :type k:
    '''
    i = 0
    while i < k:
        x = (a+b)/2
        fx = function2 (x)
        fb = function2 (b)
        if (fx * fb) < 0:
            a = x
        else:
            b = x
        i = i + 1
    print ("The root by bisection is ", x)

if __name__ == '__main__':
    guess = 0.1
    actualroot = 0
    f1 = function1(guess)
    f2 = function2(guess)
    fixed1original(guess,f1,actualroot)
    fixed2original(guess, f1, actualroot)
    fixed1fix(guess, f1, actualroot)
    fixed2fix(guess, f1, actualroot)
    fixed1fix(guess, f2, actualroot)
    a = -1
    b = 1
    tol = 0.2
    k = bihowmanyit(tol,a,b)
    bisection(a,b,k)


