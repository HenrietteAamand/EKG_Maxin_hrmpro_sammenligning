from Correction_of_lists_with_different_lengths import correction_class
from Ekg_extract_ibi import*
from PPG_extract_rr import*
from Save_to_file import*
from krydskorellation import*
from HRMpro_extract_rr import*
from plot import *
import datetime
from hr_calculator import*
from Correction_of_lists_with_different_lengths import *


nummer = 2
ekg = EKG_extract_class()
ppg = ppg_extract_class()
writer = Filewriter_class()
kryds = krydskorellation_class()
hrmpro = HRMpro_extract_class()
hr_calculator = hr_calculator_class()
lengthcorrection = correction_class()
plotter = plotter_class(nummer)

# Udtrækker r-r værdier fra data
ppg_rr = ppg.extract_rr_values('ppg_sammenligningsdata' + str(nummer) + '.csv')
timelim_begin = ppg.getAbsoluteTime_first()
timelim_end  = ppg.getAbsoluteTime_last()
ekg_rr = ekg.extracct_rr_values('EKG_sammenligningsdata' + str(nummer) + '.txt', timelim_begin, timelim_end)
hrmpro.extract_rr_values('HRMpro_sammenligningsdata' + str(nummer) + '.txt', timelim_begin, timelim_end)

hrmpro_rr = hrmpro.get_rr(0) # !!! MODIFIED !!! sæt den til 6 og se magien(4. datasæt) og 0 for originalen

# Korrigerer længderne af rr-værdierne ved at tilføje 1000 i ende:
list_corrected = plotter.correct_3_lists(ppg_rr, hrmpro_rr, ekg_rr, 1000)
ppg_rr = list_corrected[0]
hrmpro_rr = list_corrected[1]
ekg_rr = list_corrected[2]

# print(len(ppg_rr))
# print(len(hrmpro_rr))
# print(len(ekg_rr))


# Udtrækker hr
hr_hrmpro_algo = hrmpro.get_hr()
hr_ppg_algo = ppg.get_hr()

# Beregner hr
hr_hrmpro_calculated = hr_calculator.Calculate_hr_from_rr(hrmpro_rr,15)
hr_ppg_calculated = hr_calculator.Calculate_hr_from_rr(ppg_rr,15)
hr_ekg = hr_calculator.Calculate_hr_from_rr(ekg_rr,15)

# rekorrigerer hr værdierne fra ppg som jeg har beregnet. Disse må nødvendigvis ligge en faktor 1.04 over de hr værdier maxrefdes103 algoritmen beregner
hr_ppg_calculated_modified = []
for hr in hr_ppg_calculated:
    hr_ppg_calculated_modified.append(hr*0.96)

#lag_hr_ppg_calculated_vs_algo = kryds.get_korrelation(hr_ppg_algo,hr_ppg_calculated_modified,60) #- 10
lag_hr_ppg_calculated_vs_algo = -13
print("Lag of ppg_calculated is " + str(lag_hr_ppg_calculated_vs_algo))

# #Dette plotter alle interessante koblinger af hr værdier på skift - bedre med subplot?    
# plotter.plot_hr_ppg_hrmpro(hr_hrmpro_algo, hr_hrmpro_calculated, "hr_algorithm", "hr_calculated", "hr from hrm_pro algorithm and calculated", 0)
plotter.plot_hr_ppg_hrmpro(hr_ppg_algo, hr_ppg_calculated_modified, "hr_algorithm", "hr_calculated", "hr from maxrefdes103 algorithm and calculated lag 0", 0) # !!! MODIFIED !!!
plotter.plot_hr_ppg_hrmpro(hr_ppg_algo, hr_ppg_calculated_modified, "hr_algorithm", "hr_calculated", "hr from maxrefdes103 algorithm and calculated lag = " + str(lag_hr_ppg_calculated_vs_algo), lag_hr_ppg_calculated_vs_algo) # !!! MODIFIED !!!
# plotter.plot_hr_ppg_hrmpro(hr_ppg_algo, hr_hrmpro_algo, "hrm_pro", "Mexrefdes103", "hr from Mexrefdes103 and hrmpro, Algorithm hr", 0)
# plotter.plot_hr_ppg_hrmpro(hr_ppg_calculated, hr_hrmpro_calculated, "Mexrefdes103", "hrm_pro", "hr from ppg and hrmpro calculated", 0)

# # Gemmer rr værdier i en fil. 
# writer.SaveLineToFile_ekg_ppg_hrmpro('sammenligning' + str(nummer) + '.txt', ekg_rr, ppg_rr, hrmpro_rr, 0, ppg.get_timestamp())
# # Plotter EKg_hr, ppg_hr og hrmpro_hr hvor jeg selv har beregnet dem:
# plotter.plot_hr_ppg_hrmpro_ekg(hr_ppg_calculated, hr_hrmpro_calculated, hr_ekg, 'maxRefDes103', 'Hrm_pro', 'EKG', 'hr ekg, hrm_pro og ppg calculated')

# lag_ppg = kryds.get_korrelation(ekg_rr, ppg_rr, 0)
# lag_hrmpro = kryds.get_korrelation(ekg_rr, hrmpro_rr,0)
# print(lag_hrmpro)
# print(lag_ppg)
# # lag_ppg = 0
# # lag_hrmpro = 0
# plotter.plot_rr_from_3_sources(ppg_rr,ekg_rr,hrmpro_rr, lag_ppg, lag_hrmpro, 'rr from ekg, maxrefdes103 and hrmpro')

