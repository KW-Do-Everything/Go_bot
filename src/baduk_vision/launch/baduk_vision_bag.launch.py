from launch import LaunchDescription
from launch.actions import ExecuteProcess

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