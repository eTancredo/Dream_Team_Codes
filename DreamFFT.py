# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:23:09 2016

@author: Dream Team

Pending Changes

1- Transform code into function and use signal as input

2- If the sensor raise only the measured values, without the associated time,
   add a feature that, given the sampling frequency, generates the time vector

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft




"""
functions space
"""

############### Signal Generator #################

#create a sin function signal with 3 base frequencies and its 3 first harmonics
def signalgenerator(freq1, freq2 = 0, freq3 = 0):
    
    #base frequencies
    wave1 = (amplitude) * np.sin(2.0*np.pi*freq1*t)
    wave2 = (amplitude) * np.sin(2.0*np.pi*freq2*t)
    wave3 = (amplitude) * np.sin(2.0*np.pi*freq3*t)
    
    #1st harmonics
    wave4 = (amplitude/2) * np.sin(2.0*np.pi*2*freq1*t)
    wave5 = (amplitude/2) * np.sin(2.0*np.pi*2*freq2*t)
    wave6 = (amplitude/2) * np.sin(2.0*np.pi*2*freq3*t)

    
    #creates noise
    # 0 is the mean of the normal distribution you are choosing from
    # 1 is the standard deviation of the normal distribution
    # last one is the number of elements you get in array noise
    
    noise = np.random.normal(0,1,40000)
#TODO: create a method that generates more waves and maybe add noise

    
    signal = wave1 + wave2 + wave3 + wave4 + wave5 + wave6 + noise
    return signal


################### csv_data #####################

# Reads a .csv file and converts the data to a time vector t and a vector x
# with the measured values
def csv_data(file_path):
    return np.genfromtxt(file_path,delimiter=',', unpack=True)



################## freqZoom #######################

# Given 2 frequency values, creates a plot of the FFT in the interval
# delimited by them
def freqZoom(yf, xf, lowFreq, highFreq, noisePct = 0, limit = False):
    
    N = np.int(np.prod(yf.shape))
    Fs = 2*xf[-1]
    index0 = int(lowFreq*N/Fs)
    indexF = int(highFreq*N/Fs) + 1
    x_plot = xf[index0:indexF]
    y_plot = 2.0/N * np.abs(yf[index0:indexF])
    peak_value = np.max(y_plot)
    ax = plt.figure().add_subplot(111)
    ax.plot(x_plot, y_plot)
    ax.grid()
    ax.set_ylim([peak_value*noisePct, peak_value])
    ax.set_xlim([int(lowFreq)-10, int(highFreq) + 10])
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Amplitude')
    
    message = "NO DANGER"
    if limit != False:     
        ax.plot(x_plot, [limit for x in x_plot] , color = 'r')
        if peak_value >= limit:
            message = "DANGER"
    ax.set_title("%.1f Hz to %.1f Hz - %s"%(lowFreq,highFreq,message))

#TODO: add a feature that monitor the amplitudes within the interval of freqZoom




"""
values space
"""

###### If generating a signal ######
amplitude = 1.0

#in Hz
freq1 = 1000.0
freq2 = 755.0
freq3 = 355.0
#t = np.arange(0.0,1,25e-6)  

####################################

###### If using a csv file #########

file_name = "car_engine.csv"


####################################

#TODO: whats the best step for t variable so that we can have a good measuement?(considering the amount of harmonics)
"""
process
"""


#signal = signalgenerator(freq1,freq2,freq3)
t, signal = csv_data("CSV_FILES/" + file_name)
  
N = np.int(np.prod(t.shape))# list length
Fs = 1/(t[1]-t[0]) 	# sample frequency
T = 1/Fs;


"""
plots
"""

#Plot xy
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
ax1.plot(t, signal)
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Amplitude')
ax1.grid()
#ax1.axis([0.0,0.1,-10*amplitude,10*amplitude])
ax1.set_title("Time Domain")

#FFT
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
yf = fft(signal)
ax2.plot(xf, 2.0/N * np.abs(yf[0:np.int(N/2)]))
ax2.grid()
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Amplitude')
ax2.set_title("Frequency Domain")

freqZoom(yf, xf, 0, 1000, noisePct = 0, limit = 0.05)
freqZoom(yf, xf, 0, 500, noisePct = 0.5, limit = 0.08)
freqZoom(yf, xf, 500, 1000, noisePct = 0.2, limit = 0.04)


plt.show()