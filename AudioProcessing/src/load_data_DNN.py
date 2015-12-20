import numpy as np

    
input_dir = "/home/danglab/Features/Input/input.txt"
output_dir = "/home/danglab/Features/Output/output.txt"

def read_data(filename, num_features, *arg):   
    input_file = open(filename,'r')
    feature = np.zeros((num_features))
    features_arr = []
    factor_arr = []
    
    count = 0
    for line in input_file:
        count += 1
        if count > 1000:
            break
        sequential_number = line.split(" ")
        if len(arg) > 0:
            start = 1
            factor_arr.append(float(sequential_number[0]))
        else:
            start = 0 
        for i in xrange(start, num_features):
            try:
                feature[i] = (float(sequential_number[i]))
            except:
                continue
        features_arr.append(feature)
        
    if len(arg) > 0:
        return np.array(features_arr).astype(np.float32), np.array(factor_arr).astype(np.float32)
    return np.array(features_arr).astype(np.float32)
    
def load_data():
    input_data = read_data(input_dir, 108)
    output_data, factor_data = read_data(output_dir, 36, "True")
    print input_data.shape, output_data.shape
    return input_data, output_data, factor_data

#load_data()
