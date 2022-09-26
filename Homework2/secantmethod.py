def secantmethod(x0, x1, func0, func1)
    xhold = x1
    x1 = (func1 *  (x0 -x1)) / (func0 - func1)
    x0 = xhold
    return x1 and x0
