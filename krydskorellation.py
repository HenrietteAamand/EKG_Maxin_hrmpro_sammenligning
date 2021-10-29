import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import argmin

class krydskorellation_class:
    def get_korrelation(self, dominant_signal1, second_signal1, appending_with):
        i = 0
        dominant_signal = dominant_signal1.copy()
        second_signal = second_signal1.copy()
        if(len(second_signal) > len(dominant_signal)) :
            difference = len(second_signal) - len(dominant_signal)
            #print("ppg is "+ str(difference) + " sample(s) longer than ekg")
            while(i<difference):
                dominant_signal.append(appending_with)
                i+=1

        elif(len(second_signal) < len(dominant_signal)) :
            difference = len(dominant_signal) - len(second_signal)
            #print("ekg is "+ str(difference) + " sample(s) longer than ppg")
            while(i<difference):
                second_signal.append(appending_with)
                i+=1

        fig, axs = plt.subplots()
        corr = np.correlate(
            dominant_signal - np.mean(dominant_signal),  # Reference - uden DC offset
            second_signal - np.mean(second_signal),  # Input signalet til undersøgelse - uden Offset
            mode="full",
            # mode{‘full’, ‘valid’, ‘same’}, optional
            # ‘full’:
            # By default, mode is ‘full’. This returns the convolution at each point of overlap, with an output shape of (N+M-1,).
            # At the end-points of the convolution, the signals do not overlap completely, and boundary effects may be seen.
            # ‘same’:
            # Mode ‘same’ returns output of length max(M, N). Boundary effects are still visible.
            # ‘valid’:
            # Mode ‘valid’ returns output of length max(M, N) - min(M, N) + 1.
            # The convolution product is only given for points where the signals overlap completely. Values outside the signal boundary have no effect.
        )

        corr /= corr[len(dominant_signal) - 1]
        if(corr.max()<abs(corr.min())):
            lag = corr.argmin() - (len(second_signal) - 1)
        else:
            lag = corr.argmax() - (len(second_signal) - 1)
        
        # lags_axis = np.arange(-len(ekg_rr) + 1, len(ekg_rr))  # so last value is nx - 1
        # axs.plot(lags_axis, corr)
        # axs.set_xlabel("Lag [samples]")
        # plt.show()
        return(lag)