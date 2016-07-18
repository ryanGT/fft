from matplotlib.pyplot import *
from numpy import *

close('all')

def fft_case(rhs_str, fs, T, startfi=1, legloc='upper center'):
    ystr = 'y = ' + rhs_str
    dt = 1.0/fs
    t = arange(0,T,dt)
    print(ystr)
    exec(ystr)

    mytitle = '%s, $f_s=%0.3g$, T=%0.3g' % (ystr, fs, T)
    
    figure(startfi)
    clf()
    plot(t, y, 'ro')
    xlabel('Time (sec.)')
    ylabel('$y(t)$')
    title(mytitle)
    
    N = len(t)
    Y_fft = fft.fft(y)*2.0/N
    A = real(Y_fft)
    B = imag(Y_fft)
    
    nvect = arange(N)
    df = 1.0/T
    freq = df*nvect

    figure(startfi+1)
    clf()
    plot(freq, A, freq, B)
    
    legend(["$A_i$", "$B_i$"], loc=legloc)
    xlabel('Freq. (Hz.)')
    ylabel('FFT Mag.')
    title(mytitle)
    
    out_dict = {'t':t, \
                'y':y, \
                'freq':freq, \
                'A':A, \
                'B':B, \
                }
    return out_dict


case = 3

if case == 1:
    # 1Hz Cosine wave, fs = 10Hz, sampled for 1 second
    out1 = fft_case('cos(2*pi*t)', fs=10.0, T=1.0)

    # Same signal sampled for 2 seconds (1Hz Cosine wave, fs = 10Hz)
    out2 = fft_case('cos(2*pi*t)', fs=10.0, T=2.0, startfi=3)

elif case == 2:
    # 1Hz Cosine wave, fs = 10Hz, sampled for 1 second
    out1 = fft_case('cos(2*pi*t)', fs=10.0, T=1.0)

    # 1Hz Sine wave, fs = 10Hz, sampled for 1 second
    out2 = fft_case('sin(2*pi*t)', fs=10.0, T=1.0, startfi=3)

elif case == 3:
    # 1Hz Cosine wave, fs = 10Hz, sampled for 1 second
    out1 = fft_case('cos(16*pi*t)', fs=10.0, T=1.0)

    # 1Hz Sine wave, fs = 10Hz, sampled for 1 second
    out2 = fft_case('3.0*sin(14*pi*t)', \
                    fs=10.0, T=1.0, startfi=3)





show()
