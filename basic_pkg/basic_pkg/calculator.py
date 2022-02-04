import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from rclpy.callback_groups import ReentrantCallbackGroup
from std_msgs.msg import Int32MultiArray


class Calculator(Node):
    def __init__(self):
        super().__init__('calculator')

        self.callback_group = ReentrantCallbackGroup()  # Multi-thread callback

        qos_profile = QoSProfile(
            reliability = QoSReliabilityPolicy.RELIABLE,
            history = QoSHistoryPolicy.KEEP_LAST,
            depth = 10,
            durability = QoSDurabilityPolicy.VOLATILE
        )

        self.argument_subscriber = self.create_subscription(
            Int32MultiArray, 'argument', self.argument_callback, qos_profile, 
            callback_group=self.callback_group
        )

        self.operate_srv_server = self.create_service(
            
        )

    def argument_callback(self, msg):
        if not len(msg.data) == 2:
            self.get_logger().warn("[Calculator] Invalid input. ")
            return

        self.arg_a = msg.data[0]
        self.arg_b = msg.data[1]
        self.get_logger().warn("[Calculator] Subscribed Args : %d, %d"%(msg.data[0], msg.data[1]))



def main(args=None):
    try:
        rclpy.init(args=args)
        calc_node = Calculator()

        rclpy.spin(calc_node)
    
    except Exception as e:
        calc_node.get_logger().warn("[Calculator] Exception : %s"%e)
    
    finally:
        calc_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()