from Ekg_extract_ibi import*
from PPG_extract_rr import*
from Save_to_file import*
from krydskorellation import*
from HRMpro_extract_rr import*
from plot import *
import datetime


ekg = EKG_extract_class()
ppg = ppg_extract_class()
writer = Filewriter_class()
kryds = krydskorellation_class()
hrmpro = HRMpro_extract_class()
plotter = plotter_class()

ppg_rr = ppg.extract_rr_values('ppg_sammenligningsdata4.csv')
timelim_begin = ppg.getAbsoluteTime_first()
timelim_end  = ppg.getAbsoluteTime_last()
ekg_rr = ekg.extracct_rr_values('EKG_sammenligningsdata4.txt', timelim_begin, timelim_end)
hrmpro.extract_rr_values('HRMpro_sammenligningsdata4.txt', timelim_begin, timelim_end)
#print("timelimit_begin: " + str(timelim_begin))
#print("timelimit_end: " + str(timelim_end))
hrmpro_rr = hrmpro.get_rr(5)
hr_hrmpro = hrmpro.get_hr()
hr_ppg = ppg.get_hr()
#plotter.plot_hr_ppg_hrmpro(hr_ppg, hr_hrmpro)
print("length HRM_pro: " + str(len(hrmpro_rr)) + " Length ppg: " + str(len(ppg_rr)) + " Length EKG: " + str(len(ekg_rr)))
#print(hrmpro_rr)

#writer.SaveLineToFile_ekg_ppg_hrmpro('sammenligning2.txt', ekg_rr, ppg_rr, hrmpro_rr, 0, ppg.get_timestamp())

lag_ppg = kryds.get_korrelation(ekg_rr, ppg_rr)
#lag_hrmpro = kryds.get_korrelation(ekg_rr, hrmpro_rr)
lag_ppg = 2
lag_hrmpro = -2
plotter.plot_rr_from_3_sources(ppg_rr,ekg_rr,hrmpro_rr, lag_ppg, lag_hrmpro)
"""

print("ppg is lagging the ekg with " + str(lag_ppg)) #minus betyder, at de første -x værdier i ppg_rr ligger før EG'signalet, svarende til at slette de første x celler i excel
1633506561181
1633420157000

#Udskriver og gemmer til fil
print('EKG')
print(ekg_rr)

print('PPG')
print(ppg_rr)

writer.SaveLineToFile('Accel3_pp_ekg_rr.txt', ekg_rr, ppg_rr, lag, ppg.get_timestamp())
ekg.plot_ekg()
"""