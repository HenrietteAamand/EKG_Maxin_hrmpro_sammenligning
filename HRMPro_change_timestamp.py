import time
import datetime
class Timestamp_HRMpro_class:
    def __init__(self):
        self.absolute_time = 1633587754347
        self.sensor_count_at_absolute_time = 626718

    def get_timestamp(self, current_count):
        absolute_time = self.absolute_time
        sensor_count_then = self.sensor_count_at_absolute_time
        birthtime_sensor = absolute_time-sensor_count_then
        current_absolute_time = birthtime_sensor+current_count
        tid_forkert_dato = str(datetime.datetime.now().date().strftime("%d/%m/%y")) + " " + str(datetime.datetime.fromtimestamp(current_absolute_time/1000).strftime('%H:%M:%S.%f'))
        my_datetime = datetime.datetime.strptime(tid_forkert_dato, '%d/%m/%y %H:%M:%S.%f')
        absolute_time = int((time.mktime(my_datetime.timetuple())*1000))
        return absolute_time
        #alternativt
        # return (absolute_time-sensor_count_then)+current_count

