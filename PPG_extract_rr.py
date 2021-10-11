import csv
from decimal import*
import datetime, time

class ppg_extract_class: 
    def extract_rr_values(self, filename):
        #Creating the csv reader
        csv_file_original =  open(filename, mode='r')
        csv_reader = csv.DictReader(csv_file_original, delimiter = ';')
        line_count = 0
        csv_reader = list(csv_reader)
        rr = []
        self.timestamp = []
        self.hr = []
        self.first_time = str(datetime.datetime.now().date().strftime("%d/%m/%y")) + " " + csv_reader[0]['timestmp']
        self.last_time = str(datetime.datetime.now().date().strftime("%d/%m/%y")) + " " + csv_reader[len(csv_reader)-1]['timestmp']
        #print("PPG self.first_time: " + str(self.first_time))
        #print("PPG self.last_time: "+ str(self.last_time))
        
        #Reading each row and deciding what to do with it
        for row in csv_reader:
            if row["rr5"] != "0.0": #Hvis rr er lig 0, så vil jeg ikke gemme data
                rr_korr = float("{:.1f}".format(0.96*float(row["rr5"]))) #korrigerer med den faktor vi fandt i excel
                rr.append(rr_korr)
                self.timestamp.append(row["timestmp"])
                self.hr.append(float(row["hr3"]))
            line_count += 1
        csv_file_original.close()
        return(rr)
    
    def get_timestamp(self):
        return self.timestamp

    def getAbsoluteTime_first(self):
        my_datetime = datetime.datetime.strptime(self.first_time, '%d/%m/%y %H:%M:%S.%f')
        absolute_time = int((time.mktime(my_datetime.timetuple())*1000))
        return absolute_time
    
    def getAbsoluteTime_last(self):
        my_datetime = datetime.datetime.strptime(self.last_time, '%d/%m/%y %H:%M:%S.%f')
        absolute_time = int("{:.0f}".format(time.mktime(my_datetime.timetuple())*1000))
        return absolute_time
    
    def get_hr(self):
        return self.hr
