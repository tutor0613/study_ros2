import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import Int32


class BasicSubscriber(Node):
    def __init__(self):
        super().__init__('basic_subscriber')
        qos_profile = QoSProfile(depth=10)
        self.subscriber_ = self.create_subscription(Int32, 'topic', self.topic_callback, qos_profile)

    def topic_callback(self, msg):
        self.get_logger().warn('Received : %s'%msg.data)


def main(args=None):
    rclpy.init(args=args)
    sub_node = BasicSubscriber()

    try:
        rclpy.spin(sub_node)
    except Exception as e:
        sub_node.get_logger().warn('Exception - %s'%e)
    finally:
        sub_node.destroy_node()
        rclpy.shutdown()