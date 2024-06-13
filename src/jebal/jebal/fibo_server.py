import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action import CancelResponse
from rclpy.action import GoalResponse
from baduk_msgs.action import Fibonacci
import time
from std_msgs.msg import String
from baduk_msgs.srv import Square

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

        self.client = self.create_client(Square, 'square') # 여기 클라이언트 생성함,

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')


    def send_request(self, number):
        self.req = Square.Request()
        self.req.number = number
        self.future = self.client.call_async(self.req)


    def run(self,a):
        self.get_logger().info('Please enter two integers:')
        self.send_request(a)
        self.future.add_done_callback(self.handle_response)


    def handle_response(self, future):
        try:
            self.response = future.result()
            self.get_logger().info(f'Result of add_two_ints: {self.response}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {str(e)}')


    def goal_callback(self, goal_request):
        self.get_logger().info('Received goal request with order %d' % goal_request.order)
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request.')
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):
        msg = String()
        msg.data = ()
        self.get_logger().info('Executing goal...')
        feedback_msg = Fibonacci.Feedback()
        result = Fibonacci.Result()
        order = goal_handle.request.order
        sequence = [0, 1]

        for i in range(2, order):
            sequence.append(sequence[-1] + sequence[-2])
            feedback_msg.partial_sequence = sequence
            time.sleep(1)
            self.get_logger().info('Publishing feedback: %s' % sequence)
            goal_handle.publish_feedback(feedback_msg)
        self.run(sequence[-1])

        result.sequence = self.response 
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
