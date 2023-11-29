import time

time.sleep(2) # dellays the exicution

t = time.localtime()
formated_time = time.strftime("%Y-%m-%d  %H:%M:%S",t)
print(formated_time)
