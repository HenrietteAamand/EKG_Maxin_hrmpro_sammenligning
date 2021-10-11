import scipy as sp
import csv
import matplotlib.pyplot as plt
from numpy import sign
import scipy as sp
from scipy.fft import fft as fft

"""
class scipy_class():

    def ReadData(self):
        self.signal = []
        #Creating the csv reader
        csv_file_original =  open('Ekg_data.csv', mode='r')
        csv_reader = csv.reader(csv_file_original)
        #Reading each row and deciding what to do with it
        i = 0
        for value in csv_reader:
            self.signal.append(value)
        csv_file_original.close()

    def FindPeaks(self, fs):
        distance = fs/4
        self.peks, self.properties = sp.signal.find_peaks(self.signal,390, distance)

        print(self.peaks)

obj = scipy_class()

obj.ReadData()
obj.FindPeaks(200)
"""

signal_list = []
#Creating the csv reader
csv_file_original =  open('Ekg_data.csv', mode='r')
csv_reader = csv.reader(csv_file_original)
#Reading each row and deciding what to do with it
i = 0
for value in csv_reader:
    signal_list.append(value)

csv_file_original.close()

fs = 200
distance = fs/4
peaks, properties = sp.signal.find_peaks(signal_list,390, distance)

print(peaks)
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
#https://docs.scipy.org/doc/scipy/reference/signal.html 