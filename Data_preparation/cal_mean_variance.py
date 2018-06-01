# -*- coding: utf-8 -*-
import numpy as np

class mean_variance:
    
    def mean(self,address_control, address_noncontrol):
        self.control = np.genfromtxt(address_control, delimiter=",")
        self.noncontrol = np.genfromtxt(address_noncontrol, delimiter=",")
        print(np.shape(self.control))
        mean_control = np.zeros(np.shape(self.control)[1])
        mean_noncontrol = np.zeros(np.shape(self.noncontrol)[1])
        for i in range(np.shape(self.control)[1]):
            mean_control[i] = np.mean(self.control[:, i])
        for i in range(np.shape(self.noncontrol)[1]):
            mean_noncontrol[i] = np.mean(self.noncontrol[:, i])
        return (mean_control, mean_noncontrol)
    def variance(self, address_control, address_noncontrol):
        variance_control = np.zeros(np.shape(self.control)[1])
        variance_noncontrol = np.zeros(np.shape(self.noncontrol)[1])
        for i in range(np.shape(self.control)[1]):
            variance_control[i] = np.std(self.control[:, i])
        for i in range(np.shape(self.noncontrol)[1]):
            variance_noncontrol[i] = np.std(self.noncontrol[:, i])
        return (variance_control, variance_noncontrol)
    def amp_round(self, array, amp_ratio):
        self.amp_ratio = amp_ratio
        self.array = array
        self.amp = array
        for i in range(np.shape(self.array)[0]):
            self.amp[i] = self.array[i]*amp_ratio
        for i in range(np.shape(self.array)[0]):
            self.amp[i] = np.round(self.amp)[i]
        return(self.amp)


address_control = '/Users/apple/Desktop/SPDZ_Data/t-test_data/full_data/tuned_data_amplified_ratio1000/final_data101'
address_noncontrol = '/Users/apple/Desktop/SPDZ_Data/t-test_data/full_data/tuned_data_amplified_ratio1000/final_data102'
amp_ratio = 1000
mv = mean_variance()

(mean_control, mean_noncontrol) = mv.mean(address_control,address_noncontrol)
(variance_control, variance_noncontrol) = mv.variance(address_control,address_noncontrol)
(amp_mean_control) = mv.amp_round(mean_control, amp_ratio)
(amp_mean_noncontrol) = mv.amp_round(mean_noncontrol, amp_ratio)
(amp_variance_control) = mv.amp_round(variance_control, amp_ratio)
(amp_variance_noncontrol) = mv.amp_round(variance_noncontrol, amp_ratio)
"""
print('mean_control\n')
for i in range (np.shape(mean_control)[0]):
    print('%10.0f'%amp_mean_control[i])
print('mean_noncontrol\n')
for i in range (np.shape(mean_control)[0]):
    print('%10.0f'%amp_mean_noncontrol[i])  
"""  
#print('amplified control variance is %s\n noncontrol variance is %5f'%(amp_variance_control[i], amp_variance_noncontrol[i]))
#print(mean_noncontrol)
print('variance_control\n')
for i in range (np.shape(variance_control)[0]):
    print('%10.0f'%amp_variance_control[i])
print('mean_noncontrol\n')
for i in range (np.shape(variance_control)[0]):
    print('%10.0f'%amp_variance_noncontrol[i])  
