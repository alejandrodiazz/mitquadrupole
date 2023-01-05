# Converting from txt file to fft


# t=pd.read_csv('~/Research/dropbox_folder/ThesisBackup/file1.csv')
# a=pd.read_csv('~/Research/dropbox_folder/ThesisBackup/file1.csv',usecols=[1])
# ampA=pd.read_csv('~/Research/dropbox_folder/ThesisBackup/file1.csv',usecols=[2])
# n=len(a)
# dt=3.571428470421675*10**(-11) #time increment in each data

# # print(list(t["V(quada)"]))

# acc=a.values.flatten() #to convert DataFrame to 1D array
# #acc value must be in numpy array format for half way mirror calculation

# fft=rfft(acc)*dt
# freq=rfftfreq(n,d=dt)

# FFT=abs(fft)

# # plt.plot(freq,FFT)
# df = pd.DataFrame()
# df2 =df.assign(frequency = freq, FFT = FFT)
# df2.to_csv('~/Research/dropbox_folder/ThesisBackup/testa.csv')


import pandas as pd
import numpy as np
from numpy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt



# my_file = open("ltspice.txt", "r")
# content = my_file.read()
# # print(content)
# content_list = content.split(",")
# my_file.close()
# print(content_list)


# time=pd.read_csv('~/Research/dropbox_folder/ThesisBackup/sines1.csv',usecols=[0], float_precision='high')
# voltagea=pd.read_csv('~/Research/dropbox_folder/ThesisBackup/sines1.csv',usecols=[1], float_precision='high')
# voltageb=pd.read_csv('~/Research/dropbox_folder/ThesisBackup/sines1.csv',usecols=[2], float_precision='high')

# dt=3.571428470421675*10**(-11)#time increment in each data



df = pd.read_excel(r'~/Research/dropbox_folder/ThesisBackup/c6sine.xlsx')
print(df)

start = 0
end = -1
time = df['Sequence'].values.flatten()[start:end]
voltagea = df['CH2'].values.flatten()[start:end]
voltageb = df['CH3'].values.flatten()[start:end]



n=len(time)
dt=time[3]-time[2] #time increment in each data
ending = int(n/20) # choose how much to shorten the x axis

# take fft for first sinusoidal wave
fft=rfft(voltagea)*dt
freq=rfftfreq(n,d=dt)
FFT=abs(fft)
plt.figure(1)
plt.plot(freq[:ending],FFT[:ending])

# take fft for second sinusoidal wave
fft2=rfft(voltageb)*dt
freq2=rfftfreq(n,d=dt)
FFT2=abs(fft2)
plt.figure(2)
plt.plot(freq2[:ending],FFT2[:ending])
plt.show()




# from scipy.fftpack import fft, ifft

# X = fft(voltagea)
# N = len(X)
# n = np.arange(N)
# # get the sampling rate
# sr = 1/(time[3]-time[2])
# T = N/sr
# freq = n/T 
# print("frequency: ", freq)

# # Get the one-sided specturm
# n_oneside = N//2
# # get the one side frequency
# f_oneside = freq[:n_oneside]

# length = int(len(xf))
# ending = int(length/20)
# plt.figure(figsize = (12, 6))
# plt.plot(f_oneside[:ending], np.abs(X[:n_oneside])[:ending], 'b')
# plt.xlabel('Freq (Hz)')
# plt.ylabel('FFT Amplitude |X(freq)|')
# plt.show()


# from scipy.fft import fft, fftfreq
# # Number of sample points
# N = len(time)
# # sample spacing
# T = (time[3]-time[2])
# x = np.linspace(0.0, N*T, N, endpoint=False)
# y = voltagea
# yf = fft(y)
# xf = fftfreq(N, T)[:N//2]
# import matplotlib.pyplot as plt
# length = int(len(xf))
# ending = int(length/20)
# plt.plot(xf[:ending], (2.0/N * np.abs(yf[0:N//2]))[:ending])
# plt.grid()
# plt.show()



# n = end-start
# acc=voltagea.values.flatten()[start:end] #to convert DataFrame to 1D array
# #acc value must be in numpy array format for half way mirror calculation

# fft=rfft(acc)*dt
# freq=rfftfreq(n,d=dt)

# FFT=abs(fft)


# plt.plot(freq,FFT)




# data = pd.read_csv('~/Research/dropbox_folder/ThesisBackup/file1.csv',index_col=0)
# data = data["V(quada)"].astype(float).values
# print(data)

# N = data.shape[0] #number of elements
# t = np.linspace(0, 300, N) 
# #t=np.arange(N)
# s = data

# fft = np.fft.fft(s)
# fftfreq = np.fft.fftfreq(len(s))

# T = t[1] - t[0]
# print(T)

# f = np.linspace(0, 1 / T, N)
# plt.ylabel("Amplitude")
# plt.xlabel("Frequency [Hz]")
# plt.plot(fftfreq, np.absolute(fft))
# #plt.xlim(0,100)






