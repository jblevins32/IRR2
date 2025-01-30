import rclpy
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Float32
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from cv_bridge import CvBridge
from find_orange_ball import capture

class FindObject(Node):
    def __init__(self):
        super().__init__('find_object')

        # Create a custom QoS profile
        custom_qos_profile=QoSProfile(reliability=QoSReliabilityPolicy.BEST_EFFORT,history=QoSHistoryPolicy.KEEP_LAST,durability=QoSDurabilityPolicy.VOLATILE,depth=1)

        # Create the subscription
        self.subscription = self.create_subscription(
            CompressedImage, 
            '/image_raw/compressed', 
            self._image_callback, 
            custom_qos_profile
        )

    def _image_callback(self, frame)
        capture(frame)

def main(args=None):
    rclpy.init(arg=args)

    find_object = FindObject()

    rclpy.spin(find_object)

    find_object.destroy_node()

    find_object.shutdown()
