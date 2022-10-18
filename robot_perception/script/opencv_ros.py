#!/usr/bin/env python3
import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


class OpenCVROS(object):
    def __init__(self) -> None:
        rospy.init_node("opencv_ros", anonymous=True)
        self.img_sub = rospy.Subscriber("/usb_cam/image_raw", Image, callback = self.image_callback)
        self.bridge = CvBridge()
        self.image = None
    
    def image_callback(self, data):
        self.image = self.bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")

    def show_image(self):
        if self.image is None:
            return 0
        cv2.imshow("image", self.image)
        if cv2.waitKey(1) == ord('q'):
            exit()
    
    def main(self):
        while not rospy.is_shutdown():
            self.show_image()

if __name__ == "__main__":
    opencv_ros = OpenCVROS()
    opencv_ros.main()

