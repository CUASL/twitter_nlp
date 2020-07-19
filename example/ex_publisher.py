import ipcx
import time
#-------------- create node : name example --------------#
ipc = ipcx.IPC("example")

#-------- start server : publish topic : "test"  --------#
ipc.server("test")

while ipc.isRun():
    msg = "Hello World!"
    ipc.publish(msg,show = "on")

    #sleep 1 sec
    time.sleep(1)