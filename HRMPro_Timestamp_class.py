import time
import datetime
class HRMpro_Timestamp_class:
    def __init__(self):
        absolute_time = 1633587754347
        sensor_count_at_absolute_time = 626718
        self.birthtime_sensor = absolute_time-sensor_count_at_absolute_time

    def get_timestamp(self, current_count):
        current_absolute_time = self.birthtime_sensor+current_count
        tid_forkert_dato = str(datetime.datetime.now().date().strftime("%d/%m/%y")) + " " + str(datetime.datetime.fromtimestamp(current_absolute_time/1000).strftime('%H:%M:%S.%f'))
        my_datetime = datetime.datetime.strptime(tid_forkert_dato, '%d/%m/%y %H:%M:%S.%f')
        absolute_time = int((time.mktime(my_datetime.timetuple())*1000))
        return absolute_time
        # alternativt?
        # return (absolute_time-sensor_count_then)+current_count

