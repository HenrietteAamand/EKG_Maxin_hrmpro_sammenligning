#from scipy.fft import fft as fft
from HRVpy_class import *
from Filereader import *

class EKG_extract_class:
    def extracct_rr_values(self,filename, timelim_begin, timelim_end):
        filereader = filereader_class()

        self.signal = []
        self.r_indexes = []

        #self.signal = filereader.readFromCsv(filename)
        self.signal = filereader.readFrom_txt(filename, timelim_begin, timelim_end)

        #Bestemmer ved hvilket index der findes en R-værdi. Vi får ikke første og sidste R-værdi
        self.r_indexes = HRVpy_class.get_RtoR(self.signal)

        time_between_samples = (1/200)*1000 #i ms
        i = 1
        rr_intervals = []
        #Beregne tiden mellem R-værdier i ms
        while i < len(self.r_indexes):
            rr_interval = (self.r_indexes[i]-self.r_indexes[i-1])*time_between_samples
            rr_intervals.append(int(rr_interval))
            i += 1
        return(rr_intervals)

    def get_r_indexes(self):
        return self.r_indexes
    
    def get_ekg_signal(self):
        return self.signal


