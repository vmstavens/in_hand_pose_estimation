#!/usr/bin/env python3

import rospy
from ros_utils_py.utils import devprint, keep_alive
import math

from shadow_hand import ShadowHand

from gazebo_msgs.msg import ContactsState
#  * /contacts/rh_ff/distal [gazebo_msgs/ContactsState] 1 publisher


def callback(data: ContactsState):
	devprint(rospy.get_name() + " I heard " + str(data.states))


def main() -> None:

	# create shadow hand object
	sh : ShadowHand = ShadowHand()
 
	 # joint configuration, from base to tip (does this make contact with the pen? yes)
	test_q: list = [0.0, 0.0, math.pi / 2.0]
	
	# set the index finger to the specified q
	sh.set_finger(sh.FINGERS.INDEX_FINGER ,test_q)
	
	# subscribe and print the found contacts
	sub = rospy.Subscriber("/contacts/rh_ff/distal",ContactsState,callback=callback)
	
	keep_alive(rospy.get_name())

if __name__ == '__main__':
	try:
		rospy.init_node("sr_tactile_perception", anonymous=True)
		main()

	except rospy.ROSInterruptException:
		pass
