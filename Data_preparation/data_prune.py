import numpy as np
import scipy
import csv
from scipy import io 
  
class normalise():
    def loadmat(self, data_address, key):
        """
        key needs to be string !!!!
        """
        self.data_address = data_address
        self.rawdata = scipy.io.loadmat(self.data_address)
        self.targetdata = self.rawdata[key]
        return self.targetdata
   
    def normalisation(self, data):
        """
        range_alldata:target range
        nor_matrix: Normalisation of whole matrix as 'A1'
        count_col: how many 1 in each col as '1s'
        nor_col: if each col is true or '1'(1s/nA > 95)
        """
        self.data = data
        nor_matrix = np.zeros(np.shape(self.data))
        count_col = np.zeros((1,np.shape(self.data)[1]))
        nor_col = np.zeros((1, np.shape(self.data)[1]))
        range_alldata = np.percentile(self.data, (0, 100))
        
        for i in range(np.shape(self.data)[0]):
            for j in range(np.shape(self.data)[1]):
                if self.data[i][j] > range_alldata[0]*0.25 and self.data[i][j] < range_alldata[1]*0.75:# judgement the value fallen into the range or not
                    nor_matrix[i][j] = 1
        for j in range(np.shape(self.data)[1]):
            for i in range(np.shape(self.data)[0]):#given col j to addup each row i
                if nor_matrix[i][j] == 1:
                    count_col[0,j] += 1

        for i in range(np.shape(self.data)[1]):
            if float(count_col[0, i])/float(np.shape(self.data)[0]) > 0.95:# (number of 1)/(nA the row number)
                nor_col[0, i] = 1
        return  (nor_matrix, nor_col, count_col)

    def compare(self, Array1, Array2):
        """
        Compare two arrays and output same value index.
        two arrays must be in the same dimension
        """
        index = np.zeros(np.shape(Array1)[1])
        for i in range(np.shape(Array1)[1]):
            if Array1[0,i] == Array2[0,i] and Array1[0,i] == 1 :
                index[i] = 1

        return index
    def data_output_to_SPDZ2(self, dic_name, content):
        """
        The first value in the result is amount of data
        dic_name can be explicit by using '/Users/apple/Desktop/SPDZ/gfp_vals.in'
        """
        amount = np.shape(content)[0]
        output = np.insert(content, 0, amount)
        np.savetxt(dic_name, output, fmt= '%1.0f', delimiter='')
            # with open(name, 'wb') as csvfile:
            #     content = csv.writer(csvfile, delimiter=' ')
        return()
if __name__ == '__main__':
    """
    availabel key for data_Xian.mat: label1, label2, data101_Xian, data102_Xian
    """
    data_adress = '/Users/apple/Desktop/SPDZ_Data/t-test_data/full_data/data101_201_Xian.mat' # change to local address
    nm = normalise()
    
    data101_xian = nm.loadmat(data_adress, 'data101_Xian')
    (nor_matrix101, nor_col101, count_col101) = nm.normalisation(data101_xian)
    data102_xian = nm.loadmat(data_adress, 'data102_Xian')
    (nor_matrix102, nor_col102, count_col102) = nm.normalisation(data101_xian)
    cross = np.zeros(np.shape(nor_col101))
    cross = nm.compare(nor_col101, nor_col102)
    #print(np.shape(nor_col101))
    
    """
    print('Data101 normalisation of matrix __A__ has the shape: \n %s \n'%[np.shape(nor_matrix101)])
    print('Data101 normalisation of matrix __A__ is: \n %s \n'%nor_matrix101)
    print('Data101 number of true colums __1s__ is: \n %s \n'%count_col101)
    print('Data101 normalisation of colums __vA__ is: \n %s \n'%nor_col101)     
    """
    print('the intersection of two groups is %s'%cross)
    nm.data_output_to_SPDZ2('gfp_vals.in', cross)



