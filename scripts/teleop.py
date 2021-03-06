#!/usr/bin/env python

from std_msgs.msg import String
import rospy

"""
### Steps for this file:

1. Make this into a node called 'teleop'
2. Create a publisher for the 'move_command' topic, of type std_msgs/String.
3. Don't forget import the String message.
4. Publish the command verbatim.
5. Do you need to call rospy.spin()?

### Helpful resources

- [ROS tutorial on publisher / subscribers](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
- [Official rospy documentation on publisher / subscribers](http://wiki.ros.org/rospy/Overview/Publishers%20and%20Subscribers)
"""

def main():
    """Publishes a movement command based on user input.
    
    The robot will listen for movement commands on the 'move_command' topic.
    This is a text-based user interface that allows us to manually move the
    robot, by publishing to this topic.
    """
    rospy.init_node('teleop')
    cmd_publisher = rospy.Publisher('move_command', String)
    while True:
        try:
            cmd = raw_input('Movement command ("up", "down", "left", or "right"): ')
            if cmd != 'up' and cmd != 'down' and cmd != 'left' and cmd != 'right':
                continue
            cmd_publisher.publish(cmd)
        except EOFError: # Exit the program on Ctrl-D.
            print
            return

if __name__ == '__main__':
    main()
