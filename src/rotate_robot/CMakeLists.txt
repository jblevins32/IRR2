cmake_minimum_required(VERSION 3.8)
project(rotate_robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

# Add the executable
add_executable(rotate_robot_pubsub rotate_robot_pubsub/rotate_robot_pubsub.cpp)
add_executable(test_publisher rotate_robot_pubsub/test_publisher.cpp)
ament_target_dependencies(rotate_robot_pubsub rclcpp geometry_msgs)
ament_target_dependencies(test_publisher rclcpp geometry_msgs)

# Install the executable
install(TARGETS rotate_robot_pubsub DESTINATION lib/rotate_robot)
install(TARGETS
  test_publisher
  DESTINATION lib/rotate_robot)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
