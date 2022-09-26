def secantmethod(x0, x1)
    xhold = x1
    x1 = (function(x1) *  (x0 -x1)) / (function(0) - function(1))
    x0 = xhold
    return x1 and x0
