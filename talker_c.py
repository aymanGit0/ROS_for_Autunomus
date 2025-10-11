#!/usr/bin/env python3
import rospy
from lab1_ros.msg import Num
def talker():
		pub = rospy.Publisher('chatter', Num, queue_size=10)
		rospy.init_node('talker_c', anonymous=True)
		rate = rospy.Rate(10) # 10hz
		while not rospy.is_shutdown():
			msg= Num()
			msg.num= 23
			pub.publish(msg)
			rate.sleep()
if __name__ == '__main__':
		try:
			talker()
		except rospy.ROSInterruptException:
			pass
