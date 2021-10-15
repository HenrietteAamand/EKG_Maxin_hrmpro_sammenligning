import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import argmin

class krydskorellation_class:
    def get_korrelation(self, ekg_rr1, ppg_rr1, appending_with):
        i = 0
        ekg_rr = ekg_rr1.copy()
        ppg_rr = ppg_rr1.copy()
        if(len(ppg_rr) > len(ekg_rr)) :
            difference = len(ppg_rr) - len(ekg_rr)
            #print("ppg is "+ str(difference) + " sample(s) longer than ekg")
            while(i<difference):
                ekg_rr.append(appending_with)
                i+=1

        if(len(ppg_rr) < len(ekg_rr)) :
            difference = len(ekg_rr) - len(ppg_rr)
            #print("ekg is "+ str(difference) + " sample(s) longer than ppg")
            while(i<difference):
                ppg_rr.append(appending_with)
                i+=1

        fig, axs = plt.subplots()
        corr = np.correlate(
            ekg_rr - np.mean(ekg_rr),  # Reference - uden DC offset
            ppg_rr - np.mean(ppg_rr),  # Input signalet til undersøgelse - uden Offset
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

        corr /= corr[len(ekg_rr) - 1]
        if(corr.max()<abs(corr.min())):
            lag = corr.argmin() - (len(ppg_rr) - 1)
        else:
            lag = corr.argmax() - (len(ppg_rr) - 1)
        
        # lags_axis = np.arange(-len(ekg_rr) + 1, len(ekg_rr))  # so last value is nx - 1
        # axs.plot(lags_axis, corr)
        # axs.set_xlabel("Lag [samples]")
        # plt.show()
        return(lag)