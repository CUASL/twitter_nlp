import threading
import ipcx
import json
from twythonx import twit
import time
#---------------- create node : name example ----------------#
ipc = ipcx.IPC("example")
#---------- start server : publish topic : "test"  ----------#
serv1  = ipcx.server("test")
#---------- class that use to send msg to matlab  -----------#
class twitstream:
    def stream():
        time.sleep(5)
        global waitlist
        while True:
            if waitlist != []:
                msg=json.dumps(waitlist[0]['text'])
                serv1.publish(msg,show = "on")
                #dequeue
                waitlist = waitlist[1:]
                time.sleep(0.5)
#--------- class that use to get twit from twitter  ----------#
class twitupdate:
    def autoupdate():
        alltwit=[]
        
        global waitlist
        waitlist=[]
        while True:
            a1=twit()
#------------ search twit with #covid19 hashtag  -------------#
            a2=a1.search("#covid19")
            #print(waitlist)
            a2.reverse()
            #a3=alltwit+a2
            #alltwit=list( dict.fromkeys(a3) )
            for a3 in a2:
                if a3 not in alltwit:
                    alltwit.append(a3)
                    waitlist.append(a3)
            time.sleep(6)
            print(waitlist)
    def cutwaitlist():
        global waitlist
        waitlist.pop(0)




#---------- define threads that will run parallelly  -----------#
thread1  = threading.Thread(target= twitupdate.autoupdate)
thread2  = threading.Thread(target= twitstream.stream)
#------------------- start those 2 threads  --------------------#
thread1.start()
thread2.start()
