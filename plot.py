import matplotlib.pyplot as plt

class plotter_class:
    def plot_rr_from_3_sources(self, ppg_rr, ekg_rr, hrmpro_rr, lag_ppg, lag_hrmpro):
        # while(lag_ppg !=0):
        #     ppg_rr.insert(0,1000)
        #     lag_ppg += -1
        if(lag_hrmpro > 0):
            while lag_hrmpro != 0:
                hrmpro_rr.insert(0,1000)
                lag_hrmpro += -1
        elif(lag_hrmpro<0):
            while(lag_hrmpro!=0):
                hrmpro_rr.pop(0)
                lag_hrmpro += 1
        
        if(lag_ppg > 0):
            while lag_hrmpro != 0:
                ppg_rr.insert(0,1000)
                lag_ppg += -1
        elif(lag_ppg<0):
            while(lag_ppg!=0):
                ppg_rr.pop(0)
                lag_ppg += 1

        i = 0
        ppg_difference = 0
        if(len(ppg_rr) < len(ekg_rr)) :
            ppg_difference = len(ekg_rr) - len(ppg_rr)
            #print("ekg is "+ str(ppg_difference) + " sample(s) longer than ppg")
            while(i<ppg_difference):
                ppg_rr.append(0)
                i+=1
        elif(len(ppg_rr) > len(ekg_rr)) :
            difference = len(ppg_rr) - len(ekg_rr)
            #print("ppg is "+ str(difference) + " sample(s) longer than ekg")
            while(i<difference):
                ekg_rr.append(0)
                i+=1
        i = 0
        if(len(hrmpro_rr) < len(ekg_rr)) :
            difference = len(ekg_rr) - len(hrmpro_rr)
            #print("ekg is "+ str(difference) + " sample(s) longer than hrmpro")
            while(i<difference):
                hrmpro_rr.append(0)
                i+=1
        elif(len(hrmpro_rr) > len(ekg_rr)) :
            difference = len(hrmpro_rr) - len(ekg_rr)
            #print("Hrmpro is "+ str(difference) + " sample(s) longer than ekg")
            while(i<difference):
                ekg_rr.append(0)
                i+=1
            if(len(ppg_rr) < len(hrmpro_rr)) :
                i = 0
                difference = len(hrmpro_rr) - (len(ppg_rr) - ppg_difference)
                #print("Hrmpro is "+ str(difference) + " sample(s) longer than ppg")
                while(i<difference):
                    ppg_rr.append(0)
                    i+=1

        i = 1
        time = []
        for value in hrmpro_rr:
            time.append(i)
            i += 1

        laengde = len(hrmpro_rr)
        plt.plot(time[0:laengde], ppg_rr[0:laengde], label="Ppg", color='b')
        plt.plot(time[0:laengde], hrmpro_rr[0:laengde], label="hrmpro",color='k')
        plt.plot(time[0:laengde], ekg_rr[0:laengde], label="Ekg", color='r')
        plt.xlabel('samples')
        plt.ylabel('RR intervals [ms]')
        plt.title('Plot of rr-values from EKG(red), MAXREFDES(blue) and HRM-pro (black)')
        plt.show()

    def plot_hr_ppg_hrmpro(self,hr_ppg, hr_hrmpro):
        len_ppg = len(hr_ppg)
        len_hrmpro = len(hr_hrmpro)
        if(len_ppg != len_hrmpro):
            differense = abs(len_ppg-len_hrmpro)
            if(len_ppg > len_hrmpro):
                while(differense !=0):
                    hr_hrmpro.append(60)
                    differense -= 1
            if(len_ppg < len_hrmpro):
                while(differense !=0):
                    hr_ppg.append(60)
                    differense -= 1
        i = 1
        time = []
        for value in hr_ppg:
            time.append(i)
            i += 1
        laengde = len(hr_ppg)
        plt.plot(time[0:laengde], hr_ppg[0:laengde], label="Ppg", color='b')
        plt.plot(time[0:laengde], hr_hrmpro[0:laengde], label="hrmpro",color='k')
        plt.xlabel('samples')
        plt.ylabel('Hr [bpm]')
        plt.title('Plot of HR from HRM-pro and MAXREFDES103')
        plt.show()
        
            