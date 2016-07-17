from matplotlib.pyplot import *
from numpy import *
import os

fs = 10.0
f = 9
dt = 1.0/fs
T = 2.0
t = arange(0,T,dt)
y1 = cos(2*pi*(fs-f)*t)
y2 = cos(2*pi*f*t)

figure(1)
clf()
plot(t,y1,'bs')
plot(t,y2,'r+', markersize=15)
xlabel('Time (sec.)')
ylabel('$y(t)$')
legend(['1 Hz','9 Hz'], loc=(0.62,0.78))


# generate frequency vector
df = 1.0/T
N = len(t)
nvect = arange(N)
freq = df*nvect

# take FFT with proper scaling
fft1 = fft.fft(y1)*2.0/N
fft2 = fft.fft(y2)*2.0/N
A1 = real(fft1)
A2 = real(fft2)
B1 = imag(fft1)
B2 = imag(fft2)


figure(2)
clf()
plot(freq, A1, linewidth=2)
plot(freq, A2,'--', linewidth=3)
xlabel('Freq. (Hz)')
ylabel('FFT Mag.')
title('real(fft)')
legend(['$A_1$','$A_2$'], loc='upper center')


figure(3)
clf()
plot(freq, B1, linewidth=2)
plot(freq, B2, '--', linewidth=3)
xlabel('Freq. (Hz)')
ylabel('FFT Mag.')
title('imag(fft)')
ylim([-0.1,1])
legend(['$B_1$','$B_2$'], loc='upper center')


if os.getlogin() == 'rkrauss':
    import pylab_util as PU
    PU.mysave('aliasing_example_cosine.eps',1)
    PU.mysave('mirror_image_A_coeffs.eps',2)
    PU.mysave('mirror_image_B_coeffs.eps',3)

    
show()
