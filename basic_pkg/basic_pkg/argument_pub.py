import rclpy, random
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from rcl_interfaces.msg import SetParametersResult
from std_msgs.msg import Int32MultiArray


class ArgumentPublisher(Node):
    def __init__(self):
        super().__init__('argument_publisher')

        self.declare_parameter('min_random_num', 0)
        self.declare_parameter('max_random_num', 9)
        self.min_random_num = self.get_parameter('min_random_num').value
        self.max_random_num = self.get_parameter('max_random_num').value
        self.add_on_set_parameters_callback(self.update_parameter)  # Param Set Callback!!

        qos_profile = QoSProfile(
            reliability = QoSReliabilityPolicy.RELIABLE,
            history = QoSHistoryPolicy.KEEP_LAST,
            depth = 10,
            durability = QoSDurabilityPolicy.VOLATILE
        )

        self.argument_publisher = self.create_publisher(Int32MultiArray, 'argument', qos_profile)
        self.timer = self.create_timer(1, self.publish_arguments)

    def publish_arguments(self):
        arg1 = random.randint(self.min_random_num, self.max_random_num)
        arg2 = random.randint(self.min_random_num, self.max_random_num)
        msg = Int32MultiArray(); msg.data = [arg1, arg2]

        self.argument_publisher.publish(msg)
        self.get_logger().warn("[ArgumentPub] Publish Args : %d, %d"%(msg.data[0], msg.data[1]))

    def update_parameter(self, params):  # Param Set Callback!!
        for param in params:
            if param.type_ == Parameter.Type.INTEGER:
                if param.name == 'min_random_num': self.min_random_num = param.value
                if param.name == 'max_random_num': self.max_random_num = param.value
            else:
                self.get_logger().warn("[ArgumentPub] Update param - invalid type (ONLY integer)")
                return SetParametersResult(successful=False)
        
        return SetParametersResult(successful=True)


def main(args=None):
    try:
        rclpy.init(args=args)
        arg_pub_node = ArgumentPublisher()
        
        rclpy.spin(arg_pub_node)

    except Exception as e:
        arg_pub_node.get_logger().warn('[ArgumentPub] Exception : %s'%e)
    
    finally:
        arg_pub_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()