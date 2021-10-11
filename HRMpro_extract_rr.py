from HRMPro_change_timestamp import *
from HRM_pro_calculate_RR import HRMpro_caculate_rr_class

class HRMpro_extract_class:
    def __init__(self) -> None:
        self.timestamp = Timestamp_HRMpro_class()
        self.rr_calculator = HRMpro_caculate_rr_class()

    def extract_rr_values(self, filename, timelim_begin, timelim_end):

        # Læser data ind fra filen:
        file = open(filename, 'r')
        lines_From_Logfile = file.readlines()

        # Opdeler data efter ':', omregner counter til tid, så jeg herefter kan tilgå både tiden og heart rate data
        list_splitted_data = []
        i = -3
        for line in lines_From_Logfile:
            if(i >= 0):
                list_splitted_data.append(line.split(':'))
                list_splitted_data[i][0] = self.timestamp.get_timestamp_lenovo_absolute2(int(list_splitted_data[i][0]))
            i += 1
        file.close()

        
        oldtogglebit = 0
        # I den hexadecimale streng udtrækkes hver byte og gemmes i et dictionary sammen med den udregnede tid
        self.New_list_with_logged_values_as_dictionay = []
        for sensordata in list_splitted_data:
            dictionary_with_hex ={} 
            if len(sensordata) == 3:
                if 'Rx' in sensordata[1] and sensordata[0] >= timelim_begin and sensordata[0] <= timelim_end: #Jeg gemmer kun sensordata, hvis det er inden for det rigtige timescope. 
                    temporary_List = sensordata[2][1:-2].split('][')
                    if(oldtogglebit != temporary_List[6]): #Yderligere gemmes kun data, når der har været et nyt 'heart-beat-event svarende til at hr_count er blevet en større
                        dictionary_with_hex["b0"] = temporary_List[0]
                        dictionary_with_hex["b1"] = temporary_List[1]
                        dictionary_with_hex["b2"] = temporary_List[2]
                        dictionary_with_hex["b3"] = temporary_List[3]
                        dictionary_with_hex["LSB"] = temporary_List[4]
                        dictionary_with_hex["MSB"] = temporary_List[5]
                        dictionary_with_hex["hr_count"] = temporary_List[6]
                        dictionary_with_hex["hr"] = temporary_List[7]
                        dictionary_with_hex["time"] = sensordata[0]
                        self.New_list_with_logged_values_as_dictionay.append(dictionary_with_hex)

                    oldtogglebit = temporary_List[6]
        #Bruger data page 4 til at omregne til RR-værdier
        self.list_of_rr_and_time = self.rr_calculator.rr_4(self.New_list_with_logged_values_as_dictionay)
        return self.list_of_rr_and_time

    def get_rr(self, given_delay):
        # Modificerer rr-værdierne ved at udtrække rr værdier uden tiden.
        rr = []
        number = 0
        if len(self.list_of_rr_and_time) > 0:
            for dict in self.list_of_rr_and_time:
                rr.append(dict['rr'])
                if number == given_delay:
                   number = -1
                   rr.append(dict['rr'])
                number += 1
        else:
            print("please extract rr data with the extract_rr_values-method before getting the rr-values in a separate list")
        return rr
    
    def get_hr(self):
        hr = []
        for measurement in self.New_list_with_logged_values_as_dictionay:
            hr.append(int(measurement["hr"],16))
        return(hr)


# extract = HRMpro_extract_class()
# extract.extract_rr_values('HRM_pro_testdata.txt')
# print(extract.get_rr())