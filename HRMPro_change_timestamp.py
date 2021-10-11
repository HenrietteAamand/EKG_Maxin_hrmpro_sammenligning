import time
import datetime
class Timestamp_HRMpro_class:
    def get_timestamp_dell(self, current_count):
        absolute_time = 1633087383150
        sensor_count_then = 101890812
        birthtime_sensor = absolute_time-sensor_count_then
        timestamp = time.ctime((birthtime_sensor+current_count)/1000)
        return timestamp 
    
    def get_timestamp_lenovo(self, current_count):
        absolute_time = 1633089995886
        sensor_count_then = 20924843
        sensor_count_then = 5504093
        birthtime_sensor = absolute_time-sensor_count_then
        timestamp = datetime.datetime.fromtimestamp((birthtime_sensor+current_count)/1000).strftime('%H:%M:%S.%f')#time.ctime((birthtime_sensor+current_count)/1000) #Deler med 1000 for at få det i skunder frem for milisekunder
        timestamp = timestamp[:-3]
        return timestamp 
    
    def get_timestamp_lenovo_absolute(self, current_count):
        absolute_time = 1633089995886
        sensor_count_then =  20924843
        birthtime_sensor = absolute_time-sensor_count_then
        current_absolute_time = birthtime_sensor+current_count
        return current_absolute_time
        #alternativt
        # return (absolute_time-sensor_count_then)+current_count

    def get_timestamp_lenovo_absolute2(self, current_count):
        absolute_time = 1633587754347
        sensor_count_then = 626718
        birthtime_sensor = absolute_time-sensor_count_then
        current_absolute_time = birthtime_sensor+current_count
        tid_forkert_dato = str(datetime.datetime.now().date().strftime("%d/%m/%y")) + " " + str(datetime.datetime.fromtimestamp(current_absolute_time/1000).strftime('%H:%M:%S.%f'))
        my_datetime = datetime.datetime.strptime(tid_forkert_dato, '%d/%m/%y %H:%M:%S.%f')
        absolute_time = int((time.mktime(my_datetime.timetuple())*1000))
        return absolute_time
        #alternativt
        # return (absolute_time-sensor_count_then)+current_count

