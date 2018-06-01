
# -*- coding: utf-8 -*-
# (C) 2016 University of Bristol. See License.txt

# sfix and cfix is just two function which can be called during the programming.
# the semantic is indent-sensitive

#program.bit_length = 80
#print "program.bit_length: ", program.bit_length
#program.security = 40# The value in GF = 2^40
import numpy as np
import sklearn
from sklearn.datasets.samples_generator import make_regression
import csv 
import matplotlib.pyplot as plt
import pylab
import random
 #Set regression (x,y) data set    
if __name__ == '__main__':

    X, Y = make_regression(n_samples=20, n_features=10, n_informative=10, 
                        random_state=0, noise=5) 
    print 'x.shape = %s y.shape = %s' %(X.shape, Y.shape)


print X
print Y



"""
get_raw_input_from_1 = np.array([-17.86704704, -170.85994889, -164.17498266,  -90.2400275,   -24.72629196,
 -112.7218008,     9.40306418,   65.76707309,  110.93867978,  127.51813227,
  135.11141224, -104.12307323,   58.60702735,  -94.74379431,  139.57007129,
  235.80726864,   26.41376731, -124.03195764,  -10.56624293,  -29.21077983,
   91.22338762,  205.94546504,  -76.71548454,  -19.50715098,   45.66643318,
  202.42175302,  188.91429903,  -55.96667448,  -18.60643508,   30.02223498  ])
 
get_raw_input_from_0 = np.array([-0.40178094,0.46278226,0.17742614,-1.63019835
,-1.98079647,0.15634897,-0.88778575,-0.34791215
,-1.42001794,1.9507754,-1.04855297,-1.70627019
,-1.23482582,-0.68481009,1.13940068,0.40234164
,-0.20515826,-0.85409574,1.49407907,0.3130677,
-1.18063218,0.42833187,-0.51080514,-0.02818223
,0.3024719,-0.36274117,0.06651722,-0.63432209
,0.40015721,2.2408932,1.76405235,0.97873798,
0.97663904,0.70657317,0.20827498,0.3563664,
1.91006495,0.8024564,-0.86122569,-0.26800337
,1.20237985,-0.30230275,1.23029068,-0.38732682
,-0.97727788,-0.15135721,1.86755799,0.95008842
,0.12167502,0.33367433,0.76103773,0.44386323
,-0.57884966,0.05616534,-0.87079715,-0.31155253
,1.94362119,-0.74745481,-1.17312341,-0.41361898
,1.78587049,0.40198936,0.01050002,0.12691209
,0.90082649,-1.53624369,-1.16514984,0.46566244
,-1.45436567,-0.18718385,2.26975462,0.04575852
,0.0519454,0.12898291,-0.90729836,0.72909056
,-0.4380743,0.77749036,-0.50965218,-1.25279536
,1.05445173,1.22244507,-1.07075262,-0.40317695
,1.46935877,0.37816252,1.53277921,0.15494743
,-1.34775906,0.96939671,1.8831507,-1.270485,
-0.35955316,-1.7262826,-0.67246045,-0.81314628
,0.4105985,1.45427351,-0.10321885,0.14404357
,1.89588918,-0.17992484,1.48825219,1.17877957
,1.48051479,0.90604466,1.92294203,1.86755896
,-0.21274028,0.3869025,-1.61389785,-0.89546656
,-0.15501009,0.92220667,0.94725197,0.61407937
,0.6536186,-0.74216502,-2.55298982,0.8644362 
])

"""
get_raw_input_from_0 = np.array([-0.15135721
 , 0.40015721
 , 0.97873798 
 ,-0.85409574 
 ,-0.97727788 
 , 0.3130677  
 ,-0.10321885 
 ,-0.20515826 
 , 0.33367433 
 , 1.49407907 
 , 0.95008842 
 , 0.12167502 
 , 1.45427351 
 , 1.86755799 
 , 0.14404357 
 , 0.4105985  
 , 0.76103773 
 , 2.2408932  
 , 0.44386323 
 , 1.76405235] )
#print get_raw_input_from_0

get_raw_input_from_1 = np.array([-1.93293125,   9.13922135,   6.2130473 ,  -9.04506322,  -6.43764326,
  -0.94107456,   5.83402606,  -5.25353885,   1.93574486,  22.29504734,
  11.95454279,   8.72161271,  21.59381426,  25.56131016,   4.89711214,
  13.56121015,   5.51833596,  29.29045258,  15.30034559,  25.45546494])
#x_exp= [1,2,3]
#y_exp= [2,4,6]
#plt.scatter(get_raw_input_from_0,get_raw_input_from_1)
#plt.plot(x_exp, y_exp)
#pylab.savefig('/Users/apple/Desktop/SPDZ_Data/Data_thesis_writing/1st_expdata/initial_gener.jpg')
#plt.show()
rows = 20
columns = 1
"""
find - index
"""
count = []
index = []
t = 0
"""
output XY data set
"""
amp_ratio = 10000
get_raw_input_from_0_amp = get_raw_input_from_0*amp_ratio
get_raw_input_from_0_final = np.around(get_raw_input_from_0_amp)

get_raw_input_from_1_amp = get_raw_input_from_1*amp_ratio
get_raw_input_from_1_final = np.around(get_raw_input_from_1_amp)

X_amp = X*amp_ratio
X_final = np.around(X_amp)

Y_amp = Y*amp_ratio
Y_final = np.around(Y_amp)
print Y_final


with open("/Users/apple/Desktop/SPDZ/Player-Data/thesis_using data/chapter_5_2_1/pre_Y.csv", "wb") as f:

    writer = csv.writer(f)
    writer.writerows([Y_final])
with open("/Users/apple/Desktop/SPDZ/Player-Data/thesis_using data/chapter_5_2_1/pre_X.csv", "wb") as f:

    writer = csv.writer(f)
    writer.writerows([X_final])

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
        #g = np.zeros(m)
         
        for i in range(n):#rows samples
            delta[i] = (interprod[i]-Y[i])/(2*n)
            row_number = m*i
            for j in range(m):#columns features
                g[j] = g[j] + delta[i]*X[j+row_number]/n   
        for j in range(m):
            w[j] = w[j] - alpha*g[j]
    plt.scatter(X,Y)
    plt.plot(X,interprod)
    plt.title("LR of experiment data obtained by SPDZ2 Based GD with 50 iterations")
   # pylab.savefig('/Users/apple/Desktop/SPDZ_Data/Data_thesis_writing/1st_expdata/A_Simple_Linear_Regression_Sample.jpg')
    plt.show()   
    return e
#g[i] = g[i] + (1.0/n * (dot(w,X)[j]-Y[j+m*i]))*X[j+m*i]
#g = np.zeros(m)
def stochastic_gradient_descend(iteration, alpha, w, X, Y, m, n,rd_index):
    e = np.zeros(iteration)
    
    for a in range(iteration):
        interprod = dot(w,X)
        e[a] = error(interprod, Y)
       # g = np.zeros(m)
         
        for i in rd_index:#rows samples
            delta[i] = (interprod[i]-Y[i])/(2*n)
            row_number = m*i
            for j in range(m):#columns features
                g[j] = delta[i]*X[j+row_number]/n   
        for j in range(m):
            w[j] = w[j] - alpha*g[j]
    plt.scatter(X,Y)
    plt.plot(X,interprod)
    plt.title("LR of experiment data obtained by SPDZ2 Based GD with 50 iterations")
   # pylab.savefig('/Users/apple/Desktop/SPDZ_Data/Data_thesis_writing/1st_expdata/A_Simple_Linear_Regression_Sample.jpg')
    plt.show()   
    return e

if __name__ == '__main__':
    n = rows
    m = columns
    g = np.zeros(m)
    alpha = 0.1
    iteration = 30000
    delta = np.zeros(n)
    w = np.zeros(m)
    prod = n*m
    X = get_raw_input_from_0
    Y = get_raw_input_from_1
    rd_index = random.sample(range(0, 20), 20)
    print rd_index
    e = gradient_descend(iteration, alpha, w, X, Y, m, n)   
    print e
#Y_hat = []    
#for i in range(n):
#    Y_hat[i] = w[0]*Y[i]
 
    
    for i in range(m):
        print('w(%d) is %s'%(i, w[i]))

"""
    
    for j in range(m):

        g[j] = sum([(interprod[i]-Y[i])*X[j+m*i] for i in range(n)])
        w[j] = w[j] - alpha*g[j]
"""
