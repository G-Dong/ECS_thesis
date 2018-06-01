import numpy as np
def dot(w,X):
    n = rows #rows
    m = columns  #columns
    t = np.zeros(n)
    #t = Array(n,sfix)
    #for i in range(n):
    #   t[i] = sfix(0)
    for i in range(n):#rows
        for j in range(m):#columns
           t[i] = t[i] + X[j+m*i]*w[j]
    return t
    
    ## compute error
def error(wx, y):
    n = rows
    e = 0
    delta = 0
    for i in range(n):
        delta = wx[i] - y[i]
        e = e + delta**2
    return e

def gradient_descend(iteration, alpha, w, X, Y, m, n):
    e = np.zeros(iteration)
    for a in range(iteration):
        interprod = dot(w,X)
        e[a] = error(interprod, Y)
        g = np.zeros(m)
         
        for i in range(n):#rows samples
            delta[i] = (interprod[i]-Y[i])/(2*n)
            row_number = m*i
            for j in range(m):#columns features
                g[j] = g[j] + delta[i]*X[j+row_number]/n   
        for j in range(m):
            w[j] = w[j] - alpha*g[j]
    print w
    return e

if __name__ == '__main__':
    rows = 20
    columns = 2
    n = rows
    m = columns
    alpha = 0.1
    iteration = 200
    delta = np.zeros(n)
    w = np.zeros(m)
    prod = n*m
    X = np.array([10,1,10,2,10,3,10,4,10,5,10,6,10,7,10,8,10,9,10,10,
                  20,1,20,2,20,3,20,4,20,5,
                  30,1,30,2,30,3,
                  60,1,60,2])
                  
    Y = np.array([38.0214787278,44.4237918216,50.8261049153,57.2284180091
                ,63.6307311029,70.0330441966,76.4353572904,82.8376703841
                ,89.2399834779,95.6422965717,76.0429574556,88.8475836431
                ,101.652209831,114.456836018,127.261462206,114.064436183
                ,133.271375465,152.478314746,228.128872367,266.542750929])
                
    e = gradient_descend(iteration, alpha, w, X, Y, m, n)   
    print e