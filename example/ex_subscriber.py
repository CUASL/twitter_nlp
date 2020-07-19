import ipcx
import rospy

def callbackfx(msg):

    print(msg.data)

ipc = ipcx.IPC("example_sub")

#-------- start client : subscribe topic : "test"  --------#
cli = ipc.client("test",callbackfx)

ipcx.spin()
