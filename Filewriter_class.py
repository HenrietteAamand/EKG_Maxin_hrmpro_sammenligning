import csv
class Filewriter_class:
    def SaveLineToFile_ekg_ppg(self, filename, ekg, ppg, lag, timestamp):
        #print("Printing JSON til file with path: " + str(self.full_path))
        #print("")
        data_file = open(filename, 'w+', newline='')

        data_file.write('EKG,')
        for element in ekg:
            data_file.write(str(element) + ",")
        
        data_file.write('\nPPG,')
        for element in ppg:
            data_file.write(str(element) + ",")

        data_file.write('\ntimestamp,')
        for element in timestamp:
            data_file.write(str(element) + ",")

        data_file.write("\nlag of ppg, " + str(lag)) #minus betyder, at de første -x værdier i ppg_rr ligger før EG'signalet, svarende til at slette de første x celler i excel
        data_file.close()

    def SaveLineToFile_ekg_ppg_hrmpro(self, filename, ekg, ppg, hrmpro, lag, timestamp):
        #print("Printing JSON til file with path: " + str(self.full_path))
        #print("")
        data_file = open(filename, 'w+', newline='')

        data_file.write('EKG,')
        for element in ekg:
            data_file.write(str(element) + ",")
        
        data_file.write('\nPPG,')
        for element in ppg:
            data_file.write(str(element) + ",")

        data_file.write('\nHRMpro,')
        for element in hrmpro:
            data_file.write(str(element) + ",")

        data_file.write('\ntimestamp,')
        for element in timestamp:
            data_file.write(str(element) + ",")

        data_file.write("\nlag of ppg, " + str(lag)) #minus betyder, at de første -x værdier i ppg_rr ligger før EG'signalet, svarende til at slette de første x celler i excel
        data_file.close()