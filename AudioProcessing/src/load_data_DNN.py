import numpy as np

    
input_dir = "/home/danglab/Features/Input/input.txt"
output_dir = "/home/danglab/Features/Output/output.txt"
num_features = 108

def read_data(filename):   
    input_file = open(filename,'r')
    feature = np.zeros((num_features))
    features_arr = []
    count = 0
    for line in input_file:
        sequential_number = line.split(" ")
        for i in xrange(0, num_features):
            try:
                feature[i] = (float(sequential_number[i]))
            except:
                continue
        features_arr.append(feature)
        count += 1
        if count > 100:
            break
    return np.array(features_arr).astype(np.float32)
    
def load_data():
    input_data = read_data(input_dir)
    output_data = read_data(output_dir)
    print input_data.dtype, output_data.shape
    #print input_data[0]
    return input_data, output_data

#load_data()