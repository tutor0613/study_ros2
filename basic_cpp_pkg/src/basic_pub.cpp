#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

using namespace std::chrono_literals;

class BasicCppPublisher : public rclcpp::Node
{
    public:
        BasicCppPublisher()
        : Node("basic_cpp_pub"), count_(0)
        {
            auto qos_profile = rclcpp::QoS(rclcpp::KeepLast(10));
            basic_publisher_ = this->create_publisher<std_msgs::msg::Int32>("topic", qos_profile);
            timer_ = this->create_wall_timer(1s, std::bind(&BasicCppPublisher::publish_msg, this));
        }
    
    private:
        void publish_msg()
        {
            auto msg = std_msgs::msg::Int32();
            msg.data = count_++;
            RCLCPP_WARN(this->get_logger(), "[BasicCppPub] Published : %d", msg.data);
            basic_publisher_->publish(msg);
        }
        rclcpp::TimerBase::SharedPtr timer_;
        rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr basic_publisher_;
        size_t count_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<BasicCppPublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}