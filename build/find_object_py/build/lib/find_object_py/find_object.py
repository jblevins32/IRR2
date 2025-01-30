#bin/bash/python3
import rclpy
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Float32
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from cv_bridge import CvBridge
from find_object_py.color_blob_detect import hsv_contour_detect

hueLow=0
hueHigh=40
satLow=100
satHigh=255
valLow=100
valHigh=255
hueLow2=0
hueHigh2=40

class find_object(Node):
    def init(self):
        # Creates the node.
        super().__init__(node_name='image_processor')
        rclpy.logging.get_logger("PreQoS...").info("info info")
        custom_qos_profile=QoSProfile(reliability=QoSReliabilityPolicy.BEST_EFFORT,history=QoSHistoryPolicy.KEEP_LAST,durability=QoSDurabilityPolicy.VOLATILE,depth=1)
        # Subscribe to recieve images from turtlbot camera
        rclpy.logging.get_logger("About to Subscribe...").info("info info")
        self._img_subscriber = self.create_subscription(CompressedImage, '/image_raw/compressed', self._image_callback, custom_qos_profile)
        self._coordinate_publisher=self.create_publisher(msg_type=Float32,topic='/obj_coords',qos_profile=custom_qos_profile)
    def _image_callback(self, CompressedImage):	
        rclpy.logging.get_logger("Image Callback").info("info info")
        print("Image Callback")
		# The "CompressedImage" is transformed to a color image in BGR space and is store in "_imgBGR"
        self._imgBGR = CvBridge().compressed_imgmsg_to_cv2(CompressedImage, "bgr8")
        target=hsv_contour_detect(
                self._imgBGR,
                hueLow=hueLow,
                hueHigh=hueHigh,
                satLow=satLow,
                satHigh=satHigh,
                valLow=valLow,
                valHigh=valHigh,
                hueLow2=hueLow2,
                hueHigh2=hueHigh2,
            )
        msg=Float32
        msg.data=target
        self._coordinate_publisher.publish(msg=msg)
def main():
    rclpy.logging.get_logger("Node Launching").info("Node Launching")
    print("Initializing ROS API")
    rclpy.init()
    object_Finder = find_object()
    rclpy.spin(object_Finder)
    object_Finder.destroy_node()  
    rclpy.shutdown()

if __name__=="__main__":
    main()
