from matplotlib.pyplot import *
from numpy import *

T = 6.0
dt = 0.01

t = arange(0,T,dt)
y = sin(2*pi*t)

figure(1)
clf()
plot(t,y)

Y_fft = fft.fft(y)

dt = t[1]-t[0]
T_check = t.max() + dt
df = 1.0/T

N = len(t)
nvect = arange(N)
freq = df*nvect
mag_scale = abs(Y_fft)*2.0/N

figure(2)
clf()
plot(freq, mag_scale)

show()
