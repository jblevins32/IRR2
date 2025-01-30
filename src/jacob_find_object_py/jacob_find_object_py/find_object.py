import rclpy
from sensor_msgs.msg import CompressedImage
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from jacob_find_object_py.find_orange_ball import capture

class FindObject(Node):
    def __init__(self):
        super().__init__('jacob_find_object_py')

        # Create a custom QoS profile
        custom_qos_profile=QoSProfile(reliability=QoSReliabilityPolicy.BEST_EFFORT,history=QoSHistoryPolicy.KEEP_LAST,durability=QoSDurabilityPolicy.VOLATILE,depth=1)

        # Create the subscription
        self.subscription = self.create_subscription(
            CompressedImage, 
            '/image_raw/compressed', 
            self._image_callback, 
            custom_qos_profile
        )

    def _image_callback(self, frame):
        self.get_logger().info('Received an image')
        capture(frame)

def main(args=None):
    rclpy.init(args=args)

    find_object = FindObject()

    rclpy.spin(find_object)

    find_object.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
