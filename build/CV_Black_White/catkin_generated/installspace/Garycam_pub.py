#!/usr/bin/env python3
# Basics ROS program to publish real-time streaming 
# video from your built-in webcam

 
					# Import the necessary libraries
import rospy 				# Python library for ROS
from sensor_msgs.msg import Image 	# Image is the message type
from cv_bridge import CvBridge 	# Package to convert between ROS and OpenCV Images
import cv2 				# OpenCV library
  
def publish_message():
 
                         # the message type Image allow image to be sent through ros
                          			 #|
                          			 #v
  pub = rospy.Publisher('video_frames', Image, queue_size=10)
     

  
  rospy.init_node('video_pub_py', anonymous=True)
     
  # Go through the loop 10 times per second
  rate = rospy.Rate(10) # 10hz
     
 
  cap = cv2.VideoCapture(0)
     
  # Used to convert between ROS and OpenCV images
  br = CvBridge()
 
  
  while not rospy.is_shutdown():
     
      
      ret, frame = cap.read()
         
      if ret == True:
        # Print debugging information to the terminal
        rospy.loginfo('publishing video frame')
             
        # Publish the image.
        # The 'cv2_to_imgmsg' method converts an OpenCV
        # image to a ROS image message
        pub.publish(br.cv2_to_imgmsg(frame))
             
     
      rate.sleep()
         
if __name__ == '__main__':
  try:
    publish_message()
  except rospy.ROSInterruptException:
    pass
