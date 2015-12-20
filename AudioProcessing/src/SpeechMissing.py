import numpy
from wave import Wave_read
from scipy.io.wavfile import *
import matplotlib.pyplot as plt
file_wav_dir = "../Data/wav/"
file_mat_dir = "../Data/mat/"
filename = "usctimit_ema_f1_001_005"

silence_gap = 2000 #samples

def remove_data(fileWav, gap):
    # http://stackoverflow.com/questions/2060628/how-to-read-wav-file-in-pythons
    wav_file = Wave_read(file_wav_dir + fileWav + ".wav")    
    nframes =  wav_file.getnframes()    
    sample_rate, wav_data = read(file_wav_dir + fileWav + ".wav")
    print wav_data.dtype
    print wav_data.min(), wav_data.max()
    plt.plot(wav_data)
    plt.show()
    start = 0
    #write("/home/danglab/Desktop/abc.wav", sample_rate, wav_data)
    
remove_data(filename)
    