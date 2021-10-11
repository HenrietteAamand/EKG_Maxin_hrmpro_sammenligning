import csv
import datetime
import time

class filereader_class:
    def readFromCsv(self,filename):
        csv_file_original =  open(filename, mode='r')
        csv_reader = csv.reader(csv_file_original)
        #Reading each row and deciding what to do with it
        signal_list = []
        i = 0
        for value in csv_reader:
            if(i == 0):
                i+=1
                pass
            else:
                signal_list.append(value[0])
        csv_file_original.close()
        return signal_list

    def readFrom_txt(self, filename, timelimit_absolutetime_begin, timelimit_absolutetime_end):
        file = open(filename, 'r')
        lines_From_Logfile = file.readlines()

        # Opdeler data efter ':', omregner counter til tid, så jeg herefter kan tilgå både tiden og heart rate data
        Ekg_data = []
        temp_List = []
        self.timedata = []
        i = 0
        date = str(datetime.datetime.now().date().strftime('%d/%m/%y'))
        print("EKG: " + str(date))
        #print("Date: " + date)
        #Denne lille algoritme sørger for at tidsalligne EKG-data med PPG-data
        for line in lines_From_Logfile:
            temp_List = line.split(' ')
            timestamp = date + " " + temp_List[0]
            my_datetime = datetime.datetime.strptime(timestamp, '%d/%m/%y %H:%M:%S.%f')
            absolute_ekg_time = time.mktime(my_datetime.timetuple())*1000
            if(timelimit_absolutetime_end<absolute_ekg_time):
                break
            if(timelimit_absolutetime_begin <= absolute_ekg_time):
                string = temp_List[2][0:-1]
                Ekg_data.append(int(string))
                self.timedata.append(absolute_ekg_time)
            i += 1
        file.close()
        #print("EKG: " + str(Ekg_data[0]) + " time_start: " + str(self.timedata[0]) + " Timelimit_begin: " + str(timelimit_absolutetime_begin) + " Time_end: " + str(self.timedata[len(self.timedata)-1]) + " Timelimit_end: " + str(timelimit_absolutetime_end))
        return(Ekg_data)

        
        