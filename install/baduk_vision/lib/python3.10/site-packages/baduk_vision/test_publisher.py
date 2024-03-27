import rclpy as rp
from rclpy.node import Node
from baduk_msgs.msg import Go

class TestPulbisher(Node):
    def __init__(self):
        super().__init__('test_publisher')
        self.publisher = self.create_publisher(Go, 'test_topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.count = 0
    
    def timer_callback(self):
        msg = Go()

        msg.territory = "W+0.5"

        msg.winrate = [5300, 4700]
        msg.re_point = ['R16', 'R4', 'C16', 'C4', 'D3']
        
        if self.count < 50:
            msg.re_rate = ['5500', '4444', '3333', '2222', '1111']

            msg.winrate = [5300, 4700]
        else:
            msg.re_rate = ['5543', '4233', '3112', '3232', '1233']

            msg.winrate = [5000, 5000]

        self.publisher.publish(msg)
        self.get_logger().info(
            'territory: "%s", winrate: %s, repoint: %s, re_rate: %s'% (
                msg.territory,
                msg.winrate,
                msg.re_point,
                msg.re_rate
            )
        )
        self.count += 1


def main(args=None):
    rp.init(args=args)
    publisher_node = TestPulbisher()
    rp.spin(publisher_node)
    publisher_node.destroy_node()
    rp.shutdown()


if __name__ == '__main__':
    main()
