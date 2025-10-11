#!/usr/bin/env python3
import rospy
from lab1_ros.msg import Num
def callback(msg):
	print ("I heard " + str(msg.num))
def listener():
	rospy.init_node('listener_c', anonymous=True)
	rospy.Subscriber("chatter", Num, callback)
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
if __name__ == '__main__':
	listener() 
