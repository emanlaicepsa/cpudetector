import psutil
import time
import datetime


pids = psutil.pids()
rec= open("out.txt", "w")
cnt=0
while True:
    a=(int)(psutil.cpu_percent())
    if(a>90):
        cnt+=1
    else:
        cnt=0
    if(cnt>10):
        time_stamp = datetime.datetime.now()
        print(time_stamp.strftime('%Y.%m.%d-%H:%M:%S'),file=rec)
        print(time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))
        cnt=0
        
    time.sleep(10)

# for pid in pids:
#     p = psutil.Process(pid)
#     #print(p.name)
#     print(p.cpu_percent(None))