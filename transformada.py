from scipy.fft import fft, fftfreq

def FFT(y):
    SOL=fft(y)
    return SOL

def FFT_f(N,Tf):
    SOL_f = fftfreq(N, Tf)
    SOL_f=SOL_f[0:N//2]
    return SOL_f
    