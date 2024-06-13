# GoBot

2024 Capstone Design Poject. Department of Robotics. KwangWoon Univ.

This Repository contains Vision and AI part of GoBot project.

## Contents
- [Hardware](#hardware)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)


## Hardware
This Repository is for robot playing go. We use the following hardware.

- Camera: [APKO APC925](https://www.abko.co.kr/brand/detail.php?it_id=1611728230&device=pc)
- Robot Joint: [Dynamixel XL430](https://emanual.robotis.com/docs/kr/dxl/x/) x3, [Dynamixel XM430](https://emanual.robotis.com/docs/kr/dxl/x/) x3
- Robot Gipper: [Dynamixel XM330](https://emanual.robotis.com/docs/kr/dxl/x/) x2

![Robot Image](https://github.com/KW-Do-Everything/Go_bot/blob/9by9/github_img/Robot_Image.JPG?raw=true)

## Installation

Required [ROS2 Humble](https://docs.ros.org/en/humble/index.html), Ubuntu 22.04, python >= 3.10, pip, CUDA, CUDNN</br>


``` 
# For Camera in Linux System
$ sudo apt-get install v4l-utils

$ git clone https://github.com/KW-Do-Everything/Go_bot.git
$ cd Go_bot
$ pip install -r requirements.txt
$ cd src && git clone https://github.com/ros-drivers/usb_cam.git
```


This project using Google Firebase realtime database, then need your firebase realtime database admin sdk json file. 
</br>
Paste your admin sdk json file to **'Go_bot/src/badukvision/'**.

## Usage
You can check current board state with [flutter app](https://github.com/KW-Do-Everything/baduk_app).

[web version](https://kw-do-everything.web.app)

Click "add robot" button and the robot number that appears in the popup window is your robot number. Please remember it and use it.

Edit robot_num in 'Go_bot/src/baduk_vision/baduk_vision/robotInfo.py' to yours.


```
# At Go_bot/
$ colcon build
$ 최종 런치 파일 > 추후 수정 예정
```

## Contribution
1. Fork the repository.
2. Create a new branch for your feature (git checkout -b feature/new-feature).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature/new-feature).
5. Create a pull request.


## Contact
//