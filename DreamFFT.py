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




# Given 2 frequency values, creates a plot of the FFT in the interval
# delimited by them
def freqZoom(yf, xf, lowFreq, highFreq, figureNumber, limit = False):
    
    N = np.int(np.prod(yf.shape))
    plt.figure(figureNumber)  
    plt.plot(xf[int(lowFreq):int(highFreq) + 1], 2.0/N * np.abs(yf[int(lowFreq):int(highFreq) + 1]))
    plt.grid()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    if not limit:
        # Draw horizontal line at y = limit (unfinished)
        pass

#TODO: add a feature that monitor the amplitudes within the interval of freqZoom


"""
values space
"""
amplitude = 1.0

#in Hz
freq1 = 1000.0
freq2 = 755.0
freq3 = 355.0

t = np.arange(0.0,1,25e-6)
#TODO: whats the best step for t variable so that we can have a good measuement?(considering the amount of harmonics)
"""
process
"""

signal = signalgenerator(freq1,freq2,freq3)
    
N = np.int(np.prod(t.shape))# list length
Fs = 1/(t[1]-t[0]) 	# sample frequency
T = 1/Fs;
print "# Samples:", N


"""
plots
"""

#Plot xy
plt.figure(1)  
plt.plot(t, signal)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid()
plt.axis([0.0,0.1,-10*amplitude,10*amplitude])

#FFT
plt.figure(2)  
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
yf = fft(signal)
plt.plot(xf, 2.0/N * np.abs(yf[0:np.int(N/2)]))
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

freqZoom(yf,xf,0,1500,3)
freqZoom(yf,xf,355,1000,4,0.8)


plt.show()
