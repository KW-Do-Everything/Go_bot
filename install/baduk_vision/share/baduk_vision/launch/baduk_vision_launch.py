from launch import LaunchDescription
from launch.actions import ExecuteProcess

"""ExecuteProcess(
            cmd=["ros2", "run", "usb_cam", "usb_cam_node_exe"], output="screen"
        ),"""
                
def generate_launch_description():
    
    return LaunchDescription([
        
        ExecuteProcess(
            cmd=["ros2", "run", "baduk_vision", "server_listener"], output="screen"
        ),
        ExecuteProcess(
            cmd=["ros2", "run", "baduk_vision", "server_updater"], output="screen"
        ),
        ExecuteProcess(
            cmd=["ros2", "run", "baduk_vision", "baduk_vision"], output="screen"
        ),
    ])