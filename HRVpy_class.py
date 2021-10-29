import biosppy
import numpy as np
# import pyhrv.tools as tools
# import csv
# from opensignalsreader import OpenSignalsReader

class HRVpy_class:
    def get_RtoR(EKG_data_list):
        #Creating the csv reader
        signal, rpeaks = biosppy.signals.ecg.ecg(EKG_data_list, sampling_rate = 200.0, show=False)[1:3]

        # Compute NNI
        #nni = tools.nn_intervals(rpeaks)
        return rpeaks