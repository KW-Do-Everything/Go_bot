from setuptools import find_packages, setup

package_name = 'kata_test_pkg'

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
    maintainer='yungoon',
    maintainer_email='sirius584@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest', 'rclpy', 'numpy'],
    entry_points={
        'console_scripts': [
            'kata_test = kata_test_pkg.kata_test:main',
            'go_game_processor = kata_test_pkg.point_sub_n_gtp_pub:main',
            'game_state_subsciber = kata_test_pkg.gtp_sub:main'
        ],
    },
)
