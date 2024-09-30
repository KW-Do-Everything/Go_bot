from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'baduk_vision'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='capstone',
    maintainer_email='capstone@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server_updater=baduk_vision.server_updater:main',
            'test_publisher=baduk_vision.test_publisher:main',
            'baduk_vision=baduk_vision.baduk_vision:main',
            'server_listener=baduk_vision.server_listener:main',
            'othello_vision=baduk_vision.othello_vision:main',

            #'python_executable_name = pkg_name.python_executable_name:main'
        ],
    },
)
