import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from rclpy.callback_groups import ReentrantCallbackGroup
from basic_msgs.msg import TwoInt32
from basic_msgs.srv import OperateArgs


class Calculator(Node):
    def __init__(self):
        super().__init__('calculator')

        self.callback_group = ReentrantCallbackGroup()  # Multi-thread callback
        self.arg_a = 0
        self.arg_b = 0

        qos_profile = QoSProfile(
            reliability = QoSReliabilityPolicy.RELIABLE,
            history = QoSHistoryPolicy.KEEP_LAST,
            depth = 10,
            durability = QoSDurabilityPolicy.VOLATILE
        )

        self.argument_subscriber = self.create_subscription(
            TwoInt32, 'argument', self.argument_callback, qos_profile, 
            callback_group=self.callback_group
        )

        self.operate_srv_server = self.create_service(
            OperateArgs, 'operate_cmd', self.operate_cmd_callback,
            callback_group=self.callback_group
        )

    def argument_callback(self, msg):
        try:
            self.arg_a = msg.a
            self.arg_b = msg.b
            self.get_logger().warn("[Calculator] Subscribed Args : %d, %d"%(msg.a, msg.b))
        except Exception as e:
            self.get_logger().warn("[Calculator] Exception : %s"%e)
            return

    def operate_cmd_callback(self, req, resp):
        try:
            operator = req.cmd
            a = self.arg_a; b = self.arg_b
            formula = "%d %s %d"%(a, operator, b)
            resp.result = eval(formula)

            self.get_logger().warn("[Calculator] %s = %d"%(formula, resp.result))
            return resp

        except Exception as e:
            self.get_logger().warn("[Calculator] Exception : %s"%e)
            return -1


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