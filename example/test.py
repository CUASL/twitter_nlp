import twythonx

import time
#-------------- create node : name example --------------#
ipc = twythonx.IPC("example")

#-------- start server : publish topic : "test"  --------#
serv = twythonx.server("test")
count = 0

while ipc.isRun():
    msg = "Hello World!"
    serv.publish(msg,show = "on")
    if count>5: ipc.off
    count+=1
    #sleep 1 sec
    time.sleep(1)

#-------------- tract Data from twitter ----------------#

api = twythonx.twit()

resultDict = api.search2('Hello')
filecsv = twythonx.fileAPI('out.csv')

filecsv.writeFile(resultDict)
print(resultDict)

