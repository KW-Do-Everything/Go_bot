from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    return LaunchDescription([
        # 첫 번째 USB 카메라 노드 (예: /dev/video0)
        Node(
            package="usb_cam",
            executable="usb_cam_node_exe",
            name="usb_cam0_node",
            namespace="camera0",
            output="screen",
            parameters=[{
                'video_device': '/dev/video0',
                'frame_id': 'camera0_frame',
                'image_width': 1280,
                'image_height': 960,
                'pixel_format': 'mjpeg2rgb',
                'camera_name': 'usb_cam0'
            }],
        ),
        # 두 번째 USB 카메라 노드 (예: /dev/video1)
        Node(
            package="usb_cam",
            executable="usb_cam_node_exe",
            name="usb_cam1_node",
            namespace="camera1",
            output="screen",
            parameters=[{
                'video_device': '/dev/video4',
                'frame_id': 'camera1_frame',
                'image_width': 1280,
                'image_height': 960,
                'pixel_format': 'mjpeg2rgb',
                'camera_name': 'usb_cam1'
            }],
        ),
        
        Node(
            package="baduk_vision",
            executable="server_listener",
            name="server_listener_node",
            output="screen",
        ),
        Node(
            package="baduk_vision",
            executable="server_updater",
            name="server_updater_node",
            output="screen",
        ),
        Node(
            package="baduk_vision",
            executable="baduk_vision",
            name="baduk_vision_node",
            output="screen",
        ),
        Node(
            package="baduk_vision",
            executable="othello_vision",
            name="othello_vision_node",
            output="screen",
        ),
    ])
