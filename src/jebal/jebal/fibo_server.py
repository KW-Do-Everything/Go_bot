import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action import CancelResponse
from rclpy.action import GoalResponse
from baduk_msgs.action import Fibonacci

class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__('fibonacci_action_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback)
        self.get_logger().info('Fibonacci Action Server has been started.')

    def goal_callback(self, goal_request):
        self.get_logger().info('Received goal request with order %d' % goal_request.order)
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request.')
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        feedback_msg = Fibonacci.Feedback()
        result = Fibonacci.Result()
        order = goal_handle.request.order
        sequence = [0, 1]

        for i in range(2, order):
            sequence.append(sequence[-1] + sequence[-2])
            feedback_msg.partial_sequence = sequence
            self.get_logger().info('Publishing feedback: %s' % sequence)
            goal_handle.publish_feedback(feedback_msg)

        result.sequence = sequence
        self.get_logger().info('Returning result: %s' % sequence)
        goal_handle.succeed()

        return result

def main(args=None):
    rclpy.init(args=args)
    action_server = FibonacciActionServer()
    rclpy.spin(action_server)

    action_server.destroy()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
