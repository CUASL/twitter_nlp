import ipcx
import rospy

count = 0

def callbackfx(msg):
    global count
    count+=1 
    if count == 10:
        ipcx.off()
    print(msg.data,count)

ipc = ipcx.IPC("example_sub")

#-------- start client : subscribe topic : "test"  --------#
cli = ipc.client("test",callbackfx)

ipcx.spin()
