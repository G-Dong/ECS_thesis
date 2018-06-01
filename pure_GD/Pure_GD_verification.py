# (C) 2016 University of Bristol. See License.txt

# sfix and cfix is just two function which can be called during the programming.
# the semantic is indent-sensitive

#program.bit_length = 80
#print "program.bit_length: ", program.bit_length
#program.security = 40# The value in GF = 2^40
import numpy as np
import sklearn
from sklearn.datasets.samples_generator import make_regression 
"""
# Set regression (x,y) data set    
if __name__ == '__main__':

    X, Y = make_regression(n_samples=30, n_features=3, n_informative=50, 
                        random_state=0, noise=35) 
    print 'x.shape = %s y.shape = %s' %(X.shape, Y.shape)
"""
import time
start_time = time.time()


    
get_raw_input_from_0 = np.genfromtxt('/Users/apple/Desktop/SPDZ_Data/validation_real_samples/Xian_data_smaller_group101/X.csv')
get_raw_input_from_1 = np.genfromtxt('/Users/apple/Desktop/SPDZ_Data/validation_real_samples/Xian_data_smaller_group101/Y.csv')

for i in range (np.shape(get_raw_input_from_0)[0]):
    for j in range(np.shape(get_raw_input_from_0)[1]):
        get_raw_input_from_0[i, j] = get_raw_input_from_0[i, j]/(10^5)
for i in range(np.shape(get_raw_input_from_0)[1]):
    get_raw_input_from_1[i] = get_raw_input_from_1[i]/(10^5)

print np.shape(get_raw_input_from_0)

rows = 9577
columns = 140

def dot(w,X):
    n = rows #rows
    m = columns  #columns
    t = np.zeros((n,1))
    #t = Array(n,sfix)
    #for i in range(n):
    #   t[i] = sfix(0)
    for i in range(n):#rows
        for j in range(m):#columns
           t[i] = t[i] + X[i, j]*w[j]
    return t
    
    ## compute error
def error(h, y):
    #wX = dot(w,X)
    e = 0
    delta = 0
    for i in range(n):
        delta = h[i] - y[i]
        e = e + delta**2
    return e
    
    
n = rows
m = columns
prod = n*m



#X = Array(prod,sint)
#X = np.empty([1,prod],dtype = int)
#Y = Array(n,sint)
#Y = np.empty([1,n],dtype = int)
#for i in range(prod):
#    X[i] = get_raw_input_from_0  #data
#for i in range(n):
#    Y[i] = get_raw_input_from_1 #label
X = get_raw_input_from_0
Y = get_raw_input_from_1


# define array of fixed points
#X = Array(n,sint)
#Y = Array(n,sint)

i = 0
g = np.zeros(m) # initial value of gradient
w = np.zeros(m)
"""
#for i in range(m):
#    w[i] = sfix(0)
#for i in range(m):
#    g[i] = sfix(0)

#X[i] = sint(0)
#e = sfix(i)# initial value of error
#sum = 0
"""
alpha = 0.0000001
iteration = 10

#g[i] = g[i] + (1.0/n * (dot(w,X)[j]-Y[j+m*i]))*X[j+m*i]
delta = np.zeros(n)
e = np.zeros(iteration)
for a in range(iteration):
    interprod = dot(w,X)
    e[a] = error(interprod, Y)
    #print(e[a])
    g = np.zeros(m)
         
    for i in range(n):#rows samples
        delta[i] = (interprod[i]-Y[i])/(2*n)
        #row_number = m*i
        for j in range(m):#columns features
            g[j] = g[j] + delta[i]*X[i,j]/n   
    for j in range(m):
            w[j] = w[j] - alpha*g[j]



for i in range(m):
    print('wwwwwwwwwwwwwwwwwwwwwww %s', w[i])
for i in range(iteration):
    print('erroe is %s', e[i])

print("--- %s seconds ---" % (time.time() - start_time))
