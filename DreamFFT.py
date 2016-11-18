# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:23:09 2016

@author: Dream Team - OCunha

Modificações Possíveis:

1- Transformar isso em uma função e usar o sinal como argumento.

2- Se, em vez dos valores de tempo, for fornecido o valor de frequencia de aquisição, criar o
   vetor de tempo a partir de Fs.

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft



t = np.arange(0,10,0.001)
x = 10*np.sin(2*np.pi*100*t) + 20.0*np.sin(2*np.pi*10.0*t)

N = np.int(np.prod(t.shape))# tamanho da lista
Fs = 1/(t[1]-t[0]) 	# frequencia de aquisição
T = 1/Fs;
print "# Pontos:", N

#Plot xy
plt.figure(1)  
plt.plot(t, x)
plt.xlabel('Tempo (segundos)')
plt.ylabel('Medida')
plt.grid()


#FFT
plt.figure(2)  
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
yf = fft(x)
plt.plot(xf, 2.0/N * np.abs(yf[0:np.int(N/2)]))
plt.grid()
plt.xlabel('Frequencia (Hz)')
plt.ylabel('Medida')
plt.show()