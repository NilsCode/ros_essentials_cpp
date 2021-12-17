#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def move():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node('robot_talker', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1) # 1hz
    #keep publishing until a Ctrl-C is pressed
    i = 0
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 1.0
        
        rospy.loginfo(twist)
        pub.publish(twist)
        rate.sleep()
        i=i+1

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
