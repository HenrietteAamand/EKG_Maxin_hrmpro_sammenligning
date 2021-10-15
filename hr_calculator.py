class hr_calculator_class:
    def __init__(self):
        pass
    def Calculate_hr_from_rr(self, rr_list, midling):
        hr_list = []
        rr_to_hr_list = []
        n = 0
        to_save = -10
        while(n<len(rr_list)):
            rr_to_hr_list.append(rr_list[n])
            #print(rr_list[n])
            if(len(rr_to_hr_list) == midling):
                hr_list.append(float("{:.1f}".format(60000/(sum(rr_to_hr_list)/len(rr_to_hr_list)))))
                rr_to_hr_list.pop(0)# = rr_to_hr_list[to_save:]
            n += 1
        if(len(rr_to_hr_list)>0):
            hr_list.append(float("{:.1f}".format(60000/(sum(rr_to_hr_list)/len(rr_to_hr_list)))))
            rr_to_hr_list = rr_to_hr_list[to_save:]
        return hr_list

    def Calculate_hr_from_rr_resiprokke(self, rr_list):
        hr_list = []
        for rr in rr_list:
            hr_list.append(60000/rr)
        return hr_list