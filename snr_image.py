"""
============================
SNR of communication signal.
============================
Simple calculation of variance of an image and noise in an image and its ratio to find SNR
inputs: image(clean image)
noisy_image(corrupted image)
output: snr
created: 30/12/2013
auhor: sujitdeokar@ymail.com
"""

import numpy as np

image = np.array() ## input orignal image
mean_image = np.mean(signal)

noisy_image = np.array() ## input noisy image
noise = noisy_image - image
mean_noise = np.mean(noise)
noise_diff = noise - mean_noise
var_noise = np.sum(np.mean(noise_diff**2)) ## variance of noise

if var_noise == 0:
      snr = 100 ## clean image
else:
      snr = (np.log10(mean_signal/var_noise))*20 ## SNR of the image
      
snr
