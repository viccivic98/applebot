import rclpy
from geometry_msgs.msg import Twist

def main():
    rclpy.init()
    node = rclpy.create_node('wheel_controller')
    publisher = node.create_publisher(Twist, '/cmd_vel', 10)

    # Your control logic here to determine linear and angular velocities
    linear_velocity = 0.1  # Adjust as needed
    angular_velocity = 0.0  # Adjust as needed

    msg = Twist()
    msg.linear.x = linear_velocity
    msg.angular.z = angular_velocity

    publisher.publish(msg)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()