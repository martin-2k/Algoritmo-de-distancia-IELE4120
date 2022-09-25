from array import array
from scipy.signal import butter,filtfilt

def Filtro(fs,order,cutoff,data)->array:#Recibe la frecuecnia de muestreo (fs), orden del filtro, f de corte, y el array de datos.
    nyq = 0.5 * fs  # Nyquist Frequency
    y=butter_lowpass_filter(data, cutoff, order, nyq)
    return y

def butter_lowpass_filter(data, cutoff, order, nyq):
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients 
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

