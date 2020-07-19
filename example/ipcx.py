import rospy
import time
import json
from std_msgs.msg import String


class IPC:

    def __init__(self,node):
        self.node = node
        self.publisher = None
        self.subscriber = None
        self.topic = None
        self.data = list()
        rospy.init_node(node)

    def server(self,topic):
        self.topic = topic
        self.publisher = rospy.Publisher(topic, String, queue_size=10)
        

    def publish(self,message,**kwargs):
        if kwargs["show"] == "on": 
            print(message)

        self.publisher.publish(message)

    def client(self,topic,callback = None):
        self.topic = topic
        self.subscriber = rospy.Subscriber(topic, String, callback)

        return self.subscriber

    def addData(self,newData):
        self.data.append(newData)

    def isRun(self):
        return not rospy.is_shutdown()
        

def spin():
    rospy.spin()

def off():
    rospy.signal_shutdown("bye")

def toJson(data):
    return json.dumps(data)

def toDict(data):
    return json.loads(data)
        