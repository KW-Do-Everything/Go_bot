from setuptools import find_packages, setup

package_name = 'baduk_engine'

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
    maintainer='capstone1',
    maintainer_email='sirius584@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'solo_play = baduk_engine.solo_play_engine:main',
            'fight_ai = baduk_engine.fight_ai:main'
        ],
    },
)
