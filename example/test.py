import twythonx

"""
import time
#-------------- create node : name example --------------#
ipc = twythonx.IPC("example")

#-------- start server : publish topic : "test"  --------#
ipc.server("test")

while ipc.isRun():
    msg = "Hello World!"
    ipc.publish(msg,show = "on")

    #sleep 1 sec
    time.sleep(1)

"""

api = twythonx.twit()

resultDict = api.search2('Hello')
filecsv = twythonx.fileAPI('out.csv')

filecsv.writeFile(resultDict)
print(resultDict)