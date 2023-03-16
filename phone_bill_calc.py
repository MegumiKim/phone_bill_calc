# Converting str to dictionary

def dic (string):
    call_dic = dict((duration.strip(), number.strip())
                 for duration, number in (element.split(',') 
                 for element in log_string.split('\n')))
    return call_dic

log_string = "01:04:07,111-333-222\n02:03:04,222-334-998\n00:03:04,222-334-000"
  
print("1: ", dic(log_string))


# Converting duration to timedelta

from datetime import timedelta
import math

def conv_timedelta(string):
    
    for duration in dic(log_string).keys():
        call_h = duration[:2]
        call_m = duration[3:5]
        call_s = duration[6:8]
        duration_delta = timedelta(hours = int(call_h), minutes = int(call_m), seconds= int(call_s))
        
        return(duration_delta)

print("2: ", conv_timedelta(log_string))



#Calculate phone bill

def calculate(log_string):
    

# Converting duration in seconds and minutes

    duration_in_seconds = conv_timedelta(log_string).total_seconds()
    print("3a:", duration_in_seconds, "seconds")

    duration_in_minutes = duration_in_seconds / 60
    print("3b:", duration_in_minutes, "minutes")
    
    charge = 0
    for i in dic(log_string):
        if conv_timedelta(log_string) < timedelta(minutes = 5) == True:
            charge += duration_in_seconds*3
        else:
            charge += math.ceil(duration_in_minutes)*150
        
    return int(charge)

print("Total amount: NOK", calculate(log_string))