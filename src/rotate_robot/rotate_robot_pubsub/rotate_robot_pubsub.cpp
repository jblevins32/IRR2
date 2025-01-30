#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/point.hpp"
#include "geometry_msgs/msg/twist.hpp"

// use literals instead of std:chrono every time
using std::placeholders::_1;

// This class inherits from rclcpp::Node
class RotateRobot : public rclcpp::Node
{
    public:
        RotateRobot():Node("rotate_robot_pubsub") // This is initializing the node
        {
            RCLCPP_INFO(this->get_logger(), "Starting Rotate Robot Node");

            // Create a subscription to the topic "coordinates"
            subscription_ = this->create_subscription<geometry_msgs::msg::Point>(
                "/obj_coords", 10, std::bind(&RotateRobot::topic_callback, this, _1)); // _1 means the function will allow one argument

            publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/cmd_vel", 10);
        }

    private:
        void topic_callback(const geometry_msgs::msg::Point & msg)
        {
            // Instantiate a Twist message
            auto twist_msg = geometry_msgs::msg::Twist();

            // Calculate proportional control command which is a twist around the z axis
            twist_msg.angular.z = 320/2 - msg.x;

            // Publish the command velocity
            publisher_->publish(twist_msg);
        }

        // memory management in cpp
        rclcpp::Subscription<geometry_msgs::msg::Point>::SharedPtr subscription_;
        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv); // Setup ros2 system
    rclcpp::spin(std::make_shared<RotateRobot>());
    rclcpp::shutdown();
    return 0;
}