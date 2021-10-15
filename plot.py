import matplotlib.pyplot as plt

class plotter_class:
    def __init__(self, number):
        self.number = number
        self.path = "C:/Users/hah/Documents/VISUAL_STUDIO_CODE/EKG_Maxin_hrmpro_sammenligning/Sammenligningsdata/Figurer/"
    def plot_rr_from_3_sources(self, ppg_rr, ekg_rr, hrmpro_rr, lag_ppg, lag_hrmpro, title):
        self.ppg_rr = ppg_rr
        self.hrmpro_rr = hrmpro_rr
        self.lag_korregtion(lag_ppg,lag_hrmpro, 1000)

        # list_corrected = self.correct_3_lists(ppg_rr, hrmpro_rr, ekg_rr, 1000)
        # ppg_rr = list_corrected[0]
        # hrmpro_rr = list_corrected[1]
        # ekg_rr = list_corrected[2]
        
        #Laver plot og plotter rr-værdier
        i = 1
        time = []
        for value in hrmpro_rr:
            time.append(i)
            i += 1

        laengde = len(hrmpro_rr)
        plt.plot(time[0:laengde], ppg_rr[0:laengde], label="Mexrefdes103", color='b')
        plt.plot(time[0:laengde], hrmpro_rr[0:laengde], label="hrmpro",color='k')
        plt.plot(time[0:laengde], ekg_rr[0:laengde], label="Ekg", color='r')
        plt.xlabel('samples')
        plt.ylabel('RR intervals [ms]')
        plt.title(title)
        plt.legend()
        plt.axis([0, time[len(time)-1], 0, max(ppg_rr) + 100])
        plt.savefig(self.path + str(self.number) + " " + title)
        plt.show()

    def plot_hr_ppg_hrmpro_ekg(self, hr_first, hr_second, hr_third, label_first, label_second, label_third, title): #Denne metoder plotter hr-værdierne for 3 lister
        
        # list_corrected = self.correct_3_lists(hr_first, hr_second, hr_third, 60)
        # hr_first = list_corrected[0]
        # hr_second = list_corrected[1]
        # hr_third = list_corrected[2]

        i = 1
        time = []
        for value in hr_first:
            time.append(i)
            i += 1
        laengde = len(hr_first)
        plt.plot(time[0:laengde], hr_first[0:laengde], label=label_first, color='b')
        plt.plot(time[0:laengde], hr_second[0:laengde], label=label_second,color='k')
        plt.plot(time[0:laengde], hr_third[0:laengde], label=label_third,color='r')
        plt.xlabel('samples')
        plt.ylabel('Hr [bpm]')
        plt.title(title)
        plt.legend()
        plt.savefig(self.path + str(self.number) + " " + title)
        plt.show()

    def plot_hr_ppg_hrmpro(self,hr_first1, hr_second1, label_first, label_second, title, lag_first): #Denne metoder plotter rr-værdierne
        # Bruges hvis der skal indregnes lag
        if(lag_first != 0):
            print("length of " + label_first + ": " + str(len(hr_first1)))
            print("length of " + label_second + ": " + str(len(hr_second1)))
            self.ppg_rr = hr_first1.copy()
            self.hrmpro_rr = hr_second1.copy()
            self.lag_korregtion(lag_first,0, 60)
            hr_first = self.ppg_rr.copy()
            hr_second = self.hrmpro_rr.copy()
            print("length of " + label_first + ": " + str(len(hr_first)))
            print("length of " + label_second + ": " + str(len(hr_second)))
           
        else:
            hr_first = hr_first1.copy()
            hr_second = hr_second1.copy()
        if(len(hr_first)!= len(hr_second)):
            list_corrected = self.correct_3_lists(hr_first, hr_second, [], 60)
            hr_first = list_corrected[0].copy()
            hr_second = list_corrected[1].copy()

        i = 1
        time = []
        for value in hr_first:
            time.append(i)
            i += 1
        laengde = len(hr_first)
        plt.plot(time[0:laengde], hr_first[0:laengde], label=label_first, color='b')
        plt.plot(time[0:laengde], hr_second[0:laengde], label=label_second,color='k')
        plt.xlabel('samples')
        plt.ylabel('Hr [bpm]')
        plt.title(title)
        plt.legend()
        plt.savefig(self.path + str(self.number) + " " + title)
        plt.show()

    def lag_korregtion(self, lag_ppg, lag_hrmpro, correctionvalue):
        #Korrigerer for lag
        if(lag_hrmpro > 0):
            while lag_hrmpro != 0:
                self.hrmpro_rr.insert(0,correctionvalue)
                lag_hrmpro += -1
        elif(lag_hrmpro<0):
            while(lag_hrmpro!=0):
                self.hrmpro_rr.pop(0)
                lag_hrmpro += 1
        
        if(lag_ppg > 0):
            while lag_ppg != 0:
                self.ppg_rr.insert(0,correctionvalue)
                lag_ppg += -1
        elif(lag_ppg<0):
            while(lag_ppg!=0):
                self.ppg_rr.pop(0)
                lag_ppg += 1
        
    def correct_3_lists(self, list_a, list_b, list_c, append_with_value):
        dictionary= {}
        lengths = []
        dictionary[len(list_a)] = list_a
        dictionary[len(list_b)] = list_b
        dictionary[len(list_c)] = list_c

        lengths.append(len(list_a))
        lengths.append(len(list_b))
        lengths.append(len(list_c))

        lengths.sort()

        i = 1
        for element in dictionary:
            while(len(dictionary[lengths[len(lengths)-1]]) > len(dictionary[lengths[len(lengths)-i]])):
                dictionary[lengths[len(lengths)-i]].append(append_with_value)
            i += 1
        corrected_length = [list_a, list_b, list_c]

        return corrected_length