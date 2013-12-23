"""
============================
SNR of communication signal.
============================
Simple calculation of variance of signal and noise and its ratio to find SNR
inputs:  signal(orignal data)
         noisy_signal(corrupted data)
output:  snr
created: 23/10/2013
auhor:   sujitdeokar@ymail.com
"""

import numpy as np

signal = np.array()                                   ## input orignal data
mean_signal = np.mean(signal)
signal_diff = signal - mean_signal
var_signal = np.sum(np.mean(signal_diff**2))          ## variance of orignal data

noisy_signal = np.array()                             ## input noisy data
noise = noisy_signal - signal
mean_noise = np.mean(noise)
noise_diff = noise - mean_noise
var_noise = np.sum(np.mean(noise_diff**2))            ## variance of noise

if var_noise == 0:
      snr = 100                                       ## clean image
else:
      snr = (np.log10(var_signal/var_noise))*10       ## SNR of the data
      
snr
