import twythonx
import time
#import threading

#-------------- create node : name example --------------#
ipc = twythonx.IPC("example")
api = twythonx.twit()
#-------- start server : publish topic : "test"  --------#
serv = twythonx.server("test")

while ipc.isRun():
    resultDict = api.search2('#cuasl','text','tweet_when')
    
    msg = twythonx.toJson(resultDict)
    #print(msg)

    serv.publish(msg,show = "on")

    #sleep 1 sec
    time.sleep(5)
