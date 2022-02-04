#!/usr/bin/env python3

 

import rospy 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 
 
def callback(data):
 
  
  br = CvBridge()
 
  # Output debugging information to the terminal
  rospy.loginfo("Getting Da feed man")
   
  # Convert ROS Image message to OpenCV image
  Present_frame = br.imgmsg_to_cv2(data)
  grayFrame = cv2.cvtColor(Present_frame, cv2.COLOR_BGR2GRAY) 
  
  Useless, BAndWFrames = cv2.threshold(grayFrame, 80, 255, cv2.THRESH_BINARY)
  # Display image
  cv2.imshow("camera", BAndWFrames )
   
  cv2.waitKey(1)
      
def receive_message():
 
  # Tells rospy the name of the node.
  # Anonymous = True makes sure the node has a unique name. Random
  # numbers are added to the end of the name. 
  rospy.init_node('video_sub_py', anonymous=True)
   
  # Node is subscribing to the video_frames topic
  rospy.Subscriber('video_frames', Image, callback)
 
  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()
 
  # Close down the video stream when done
  cv2.destroyAllWindows()
  
if __name__ == '__main__':
  receive_message()
