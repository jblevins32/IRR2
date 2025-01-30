import rclpy
from sensor_msgs.msg import CompressedImage
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from jacob_find_object_py.find_orange_ball import capture
from std_msgs.msg import Float64
from geometry_msgs.msg import Point
import numpy as np

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

        self.publisher_ = self.create_publisher(Point, '/obj_coords', 10)

    def _image_callback(self, frame):
        # self.get_logger().info('Received an image')
        obj_coords = float(capture(frame))

        if obj_coords == 0:
            obj_coords = float(0)
        else:
            obj_coords = 2*(obj_coords/160) # Normalize the coordinates for velocity commands 

        # Convert message to ROS message
        obj_coords_ros = Point()
        obj_coords_ros.x = obj_coords

        print(f'vel_cmd = {obj_coords_ros}')
        self.publisher_.publish(obj_coords_ros)

def main(args=None):
    rclpy.init(args=args)

    find_object = FindObject()

    rclpy.spin(find_object)

    find_object.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
