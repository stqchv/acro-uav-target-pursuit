from launch import LaunchDescription
from launch.actions import LogInfo, ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        LogInfo(msg="Starting drone simulation..."),

        ExecuteProcess(
            cmd=['/home/stqchv/Micro-XRCE-DDS-Agent/build/MicroXRCEAgent',
                  'udp4', '-p', '8888'],
            output='screen'
        )

    ])