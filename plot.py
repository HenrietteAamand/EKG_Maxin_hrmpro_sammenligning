import matplotlib.pyplot as plt

class plotter_class:
    def __init__(self, number):
        self.number = number
        self.path = "C:/Users/hah/Documents/VISUAL_STUDIO_CODE/EKG_Maxin_hrmpro_sammenligning/Sammenligningsdata/Figurer/"
    def plot_rr_from_3_sources(self, first_rr1, second_rr1, third_rr1, lag_first, lag_second, label_first, label_second, label_third, title):
        if(lag_first != 0 or lag_second != 0):
            self.first_signal = first_rr1.copy()
            self.second_signal = second_rr1.copy()
            self.lag_correction(lag_first,lag_second, 1000)

            print("Lag korrected!")

            list_corrected = self.correct_length_3_lists(self.first_signal, self.second_signal, third_rr1, 1000)
            first_rr = list_corrected[0].copy()
            second_rr = list_corrected[1].copy()
            third_rr = list_corrected[2].copy()
            
        
        #Laver plot og plotter rr-værdier
        i = 1
        time = []
        for value in second_rr:
            time.append(i)
            i += 1

        laengde = len(second_rr)
        plt.plot(time[0:laengde], first_rr[0:laengde], label=label_first, color='b')
        plt.plot(time[0:laengde], second_rr[0:laengde], label=label_second,color='k')
        plt.plot(time[0:laengde], third_rr[0:laengde], label=label_third, color='r')
        plt.xlabel('samples')
        plt.ylabel('RR intervals [ms]')
        plt.title(title)
        plt.legend()
        plt.axis([0, time[len(time)-1], 0, max(first_rr) + 100])
        plt.savefig(self.path + str(self.number) + " " + title)
        plt.show()

    def plot_rr_from_2_sources(self, first_rr1, second_rr1, lag, label_first, label_second, title):
        first_rr = []
        second_rr = []
        if(lag != 0):
            self.first_signal = first_rr1
            self.lag_correction(lag, 0, 1000)

            list_corrected = self.correct_length_3_lists(first_rr1, second_rr1, [], 1000)
            first_rr = list_corrected[0].copy()
            second_rr = list_corrected[1].copy()
        else:
            first_rr = first_rr1.copy()
            second_rr = second_rr1.copy()

        #Laver plot og plotter rr-værdier
        i = 1
        time = []
        for value in first_rr:
            time.append(i)
            i += 1

        laengde = len(first_rr)-1
        plt.plot(time[0:laengde], first_rr[0:laengde], label=label_first, color='k')
        plt.plot(time[0:laengde], second_rr[0:laengde], label=label_second,color='r')
        plt.xlabel('samples')
        plt.ylabel('RR intervals [ms]')
        plt.title(title)
        plt.legend()
        plt.axis([0, time[len(time)-1], 0, max(first_rr) + 100])
        plt.savefig(self.path + str(self.number) + " " + title)
        plt.show()

    def plot_hr_ppg_hrmpro_ekg(self, hr_first1, hr_second2, hr_third3, label_first, label_second, label_third, title): #Denne metoder plotter hr-værdierne for 3 lister
        print(len(hr_first1))
        print(len(hr_second2))
        print(len(hr_third3))

        list_corrected = self.correct_length_3_lists(hr_first1, hr_second2, hr_third3, 60)
        hr_first = list_corrected[0].copy()
        hr_second = list_corrected[1].copy()
        hr_third = list_corrected[2].copy()

        print(len(hr_first))
        print(len(hr_second))
        print(len(hr_third))

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
            self.first_signal = hr_first1.copy()
            self.second_signal = hr_second1.copy()
            self.lag_correction(lag_first,0, 60)
            hr_first = self.first_signal.copy()
            hr_second = self.second_signal.copy()
            print("length of " + label_first + ": " + str(len(hr_first)))
            print("length of " + label_second + ": " + str(len(hr_second)))
           
        else:
            hr_first = hr_first1.copy()
            hr_second = hr_second1.copy()
        if(len(hr_first)!= len(hr_second)):
            list_corrected = self.correct_length_3_lists(hr_first, hr_second, [], 60)
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

    def lag_correction(self, lag_ppg, lag_hrmpro, correctionvalue):
        #Korrigerer for lag
        if(lag_hrmpro > 0):
            while lag_hrmpro != 0:
                self.second_signal.insert(0,correctionvalue)
                lag_hrmpro += -1
        elif(lag_hrmpro<0):
            while(lag_hrmpro!=0):
                self.second_signal.pop(0)
                lag_hrmpro += 1
        
        if(lag_ppg > 0):
            while lag_ppg != 0:
                self.first_signal.insert(0,correctionvalue)
                lag_ppg += -1
        elif(lag_ppg<0):
            while(lag_ppg!=0):
                print("length of ppg: " + str(len(self.first_signal)))
                self.first_signal.pop(0)
                lag_ppg += 1
            print("length of ppg: " + str(len(self.first_signal)))
        
    def correct_length_3_lists(self, list_a, list_b, list_c, append_with_value):
        dictionary= {}
        lengths = []
        len_lista = len(list_a)
        len_listb = len(list_b)
        len_listc = len(list_c)
        
        dictionary[len_lista] = list_a
        if(len_lista != len_listb): dictionary[len_listb] = list_b
        else: 
            len_listb += 1
            list_b.append(append_with_value)
            dictionary[len_listb] = list_b
        if(len_lista != len_listc and len_listb!=len_listc): dictionary[len_listc] = list_c
        else:
            while(len_lista == len(list_c) or len_listb == len(list_c)):
                list_c.append(append_with_value)
            len_listc = len(list_c)
            dictionary[len_listc] = list_c

        lengths.append(len(list_a))
        lengths.append(len(list_b))
        lengths.append(len(list_c))

        lengths.sort()

        i = 2
        for element in dictionary:
            len_longest_list = len(dictionary[lengths[len(lengths)-1]])
            len_current_list = len(dictionary[lengths[len(lengths)-i]])
            while(len_longest_list > len_current_list ): # (Længden af den længste liste > længden af den liste vi er i gang med)
                print("Making longer: " + str(len(dictionary[lengths[len(lengths)-i]])))
                dictionary[lengths[len(lengths)-i]].append(append_with_value) #forlænger den for korte liste med 'append_with_value')
                len_current_list += 1 #len(dictionary[lengths[len(lengths)-i]])
            i += 1
        print(len(dictionary[lengths[len(lengths)-i]]))
        corrected_length = [list_a, list_b, list_c]
        corrected_length = [dictionary[len_lista], dictionary[len_listb], dictionary[len_listc]]
        print(len(corrected_length[0]) )
        print(len(corrected_length[1]) )
        print(len(corrected_length[2]) )
        return corrected_length
    
    def plot_ekg(self, r_indexes, ekg_signal):
        i = 1
        time = []
        for value in ekg_signal:
            time.append(i)
            i += 1

        y = []
        for r_index in r_indexes:
            y.append(ekg_signal[r_index])

        laengde = len(ekg_signal)
        plt.plot(time[0:laengde], ekg_signal[0:laengde], color='k')
        plt.stem(r_indexes, y)
        plt.xlabel('samples')
        plt.ylabel('Filtered ECG data')
        plt.show()