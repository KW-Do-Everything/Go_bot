import rclpy as rp
from rclpy.node import Node
from baduk_msgs.msg import Go, State
from baduk_vision.robotInfo import url, robot_num
import requests

# Only Subscriber needed
class ServerUpdater(Node):

    def __init__(self):
        super().__init__('server_updater')
        self.last_ai_msg = None
        self.subscriber = self.create_subscription(
            Go,
            'game_state_topic',
            self.ai_listener_callback,
            10
        )

        self.last_state_msg = "."*361
        self.subscriber1 = self.create_subscription(
            State,
            'game_state',
            self.state_listener_callback,
            10
        )

    def ai_listener_callback(self, msg):
        # update when data changed
        if self.last_ai_msg != msg:
            self.ai_update(msg)
            self.last_ai_msg = msg
    
    def state_listener_callback(self, msg):
        if self.last_state_msg != msg:
            self.state_update(msg)
            self.last_state_msg = msg
    
    # AI 분석 업데이트
    def ai_update(self, msg):
        self.updater(url, robot_num, "finish", msg.finish)
        try:
            re = []
            for i in range(5):
                re.append(msg.re_point[i])
                re.append(int(msg.re_rate[i]))
            data = {
                'territory': msg.territory,
                'winRate': msg.winrate.tolist(),
                'recommend': re
            }
            
            self.updater(url, robot_num, "AI", data)
        except:
            self.get_logger().error("re length not 5")

    # 바둑판 상황 업데이트
    def state_update(self, msg):
        data = msg.state

        self.updater(url, robot_num, "state", data)

    # Firebase 실시간 데이터 베이스에 데이터 업데이트
    def updater(self, url, robot_num, key, data):
        print("update to server! -", key, data)
        res = requests.patch(
            f"{url}/{robot_num}.json",
            json={key: data}
        )


def main(args=None):
    rp.init(args=args)

    serverUpdater = ServerUpdater()
    rp.spin(serverUpdater)

    serverUpdater.destroy_node()
    rp.shutdown


if __name__ == '__main__':
    main()
