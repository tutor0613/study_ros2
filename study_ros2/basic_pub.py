import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import Int32


class BasicPublisher(Node):
    def __init__(self):
        super().__init__('basic_publisher')
        qos_profile = QoSProfile(depth=10)  # queue size
        self.publisher_ = self.create_publisher(Int32, 'topic', qos_profile)
        timer_period = 1  # sec
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int32(); msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().warn('Published : %s'%msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    pub_node = BasicPublisher()

    try:
        rclpy.spin(pub_node)
    except Exception as e:
        pub_node.get_logger().warn('Exception - %s'%e)
    finally:
        pub_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()