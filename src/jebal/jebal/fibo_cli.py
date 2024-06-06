import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from example_interfaces.action import Fibonacci

class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Fibonacci, 'fibonacci')
        self.send_goal(10)  # 초기 목표를 설정합니다.

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info('Received feedback: %s' % feedback_msg.feedback.partial_sequence)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: %s' % result.sequence)
        self.get_logger().info('Ready for next goal.')

        # 사용자 입력을 받아서 새로운 목표를 설정합니다.
        new_order = int(input('Enter the next Fibonacci order: '))
        self.send_goal(new_order)

def main(args=None):
    rclpy.init(args=args)
    action_client = FibonacciActionClient()
    rclpy.spin(action_client)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
