
#This is the 2-sample t-test which is used for compare certain feature's influence. No module and no matrix #version. Used in SPDZ2 2 party communication system

#input-0, control group,
#input-1, non-control group

program.bit_length = 80
print"program.bit_length: ", program.bit_length
program.security = 40# The value in GC = 2^40
#import sys
#sys.setrecursionlimit(10000000)

#deal with raw data. load_int: convert sint to sfix.
#                   get_real_data: divide the amp_ratio



def load_int(X, num):
    X_amp = Array(num,sfix)
    for i in range(num):
        d = sfix(); d.load_int(X[i])
        X_amp[i] = d
    return X_amp

def get_real_data(X_amp, num, amp_ratio):
    X =Array(num, sfix)
    for i in range(num):
        X[i] = X_amp[i]/amp_ratio
    return X


#def mean(x, num_data):
    
    #    num_data = np.shape(x) should be true. x is array
    #    calculate mean, can be pre-calculated
    
    #    sum = sfix(0)
    #    mean = sfix(0)
    #    for i in range(num_data):
    #        sum = sum + x[i]
#    mean = sum/num_data
#    return mean

#def variance(x, num_data):
    
    #    calculate standard deviation, can be pre-calculated
    
#    sum = sfix(0)
#    mean = sfix(0)
#    std = sfix(0)
#    mean = mean(x, num_data)
#    for i in range(num_data):
#        sum = sum + (x[i] - mean)^2
#    std = (sum/num_data)^0.5
#   return std
#def df(type, num_1, num_2, std_1, std_2):
#def df(num_1,num_2)
    
    #    degree of freedom, only needed when variance of two-party are un-equal.
    #    Can delete 'if' when apply.
    
    #    df = sfix(0)
        #    if type == 'equal_variance':
        #    df = (num_1 + num_2) - 2
        #        else:
        #        df = (std_1^2/num_1 + std_2^2/num_2)^2/(std_1^2/num_1)^2/((num_1 - 1) + (std_2^2/num_2)^2/(num_2 - 1))
#    return df

#def gett(type, X_1, X_2, num_1, num_2):
def gett(mean_1, mean_2, num_1, num_2， std_1, std_2):
    #    calling std and mean to calculate the t value. All the data is encrypted.
    
    #    X_amp1 = load_int(group1, num_1)
    #    X_amp2 = load_int(group2, num_2)
    #    X_1 = get_real_data(X_amp1, num_1, amp_ratio)
    #    X_2 = get_real_data(X_amp2, num_2, amp_ratio)
    
    #    if type == 'equal_variance':
    s_p = (((num_1 - 1)*std_1 + (num_2 - 1)*std_2)/(num_1+num_2-2))^0.5
    t = (mean_1 - mean_2)/(s_p*(1/num_1 + 1/num_2)^0.5)
        #    else:
        #       s_delta = (std(X_1, num_1)^2/num1 + std(X_2, num_2)^2/nun_2)
        #        t = (mean(X_1, num_1) - mena(X_2, num_2))/s_delta
    return t

def significant(t, p_value):
    
    #   compare with p-value.
    
    if t > p-value:
        sig = 'True'
    else:
        sig = 'False'
    return sig

#if __name__ == "__main__":

#    Main program. With data_number-like data public and all other parameters are encrypted.
#    Thus, the only public value is state and data_number.

num_1 = 9577 #data 101
num_2 = 6869 #data 102
feature = 10
#totalnum_1 = num_1*feature
#totalnum_2 = num_2*feature

p_value = sfix(2.576) # p-value here is chosen as 2.576 while the df is larger than 100 and 0.005 percentage.
t_value = sfix(0)
amp_ratio = sfix(1000)
mean_1 = Array(feature, sint)
mean_2 = Array(feature, sint)
std_1 = Array(feature, sint)
std_2 = Array(feature, sint)
# 1 for control, 2 for noncontrol

#0-mean_1, 1-mean_2, 2-std_1, 3-std_2
for i in range(feature):
    mean_1_raw[i] = sint.get_raw_input_from(0)# big X
for i in range(feature):
    mean_2_raw[i] = sint.get_raw_input_from(1)
for i in range(feature):
    std_1_raw[i] = sint.get_raw_input_from(2)
for i in range(feature):
    std_2_raw[i] = sint.get_raw_input_from(3)
X_amp0 = load_int(mean_1_raw, feature)
X_amp1 = load_int(mean_2_raw, feature)
X_amp2 = load_int(std_1_raw, feature)
X_amp3 = load_int(std_2_raw, feature)

mean_1 = get_real_data(X_amp0, feature, amp_ratio)
mean_2 = get_real_data(X_amp1, feature, amp_ratio)
std_1 = get_real_data(X_amp2, feature, amp_ratio)
std_2 = get_real_data(X_amp3, feature, amp_ratio)


#for i in range(1):
#   x_control = Array(num_1, sint)
#   x_noncontrol = Array(num_2, sint)
#   for j in range(num_1):
#   for j in range(num_2):
#       x_noncontrol[j] = X_noncontrol[feature*j+i]
    
for i in range(feature)
    t_value = gett(mean_1[i], mean_2[i], num_1, num_2， std_1[i], std_2[i])
    state = significant(t_value, p_value)
    print('The t value is: %f'%t_value)
    print('This molecule leads to cancer: %s'%state)

#    """
#    for i in range(n):
#        y = sint.gent_raw_input+from(0)
#    """

