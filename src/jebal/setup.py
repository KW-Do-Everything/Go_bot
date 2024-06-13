from setuptools import find_packages, setup

package_name = 'jebal'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='capstone',
    maintainer_email='sirius584@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'game_state_subscriber = jebal.gtp_sub:main',
            'black_stone_publisher = jebal.point_pub:main',
            'go_game_processor = jebal.point_sub_n_gtp_pub:main',
            'solo_play = jebal.solo_play:main',
            'fibonacci_action_client = jebal.fibo_cli:main',
            'fibonacci_action_server = jebal.fibo_server:main',
            'square_service = jebal.service_server:main',
            'add_two_ints_client = jebal.service_cli:main',
            'add_two_ints_server = jebal.service_serv:main',
            'add_two_ints_server2 = jebal.service_serv2:main'
        ],
    },
)
