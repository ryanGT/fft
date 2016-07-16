from matplotlib.pyplot import *
from numpy import *

T = 2.0
dt = 0.01

t = arange(0,T,dt)
y = sin(2*pi*t)

figure(1)
clf()
plot(t,y)

Y_fft = fft.fft(y)

figure(2)
clf()
plot(abs(Y_fft))

show()
