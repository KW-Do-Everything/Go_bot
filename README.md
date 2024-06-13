# GoBot

2024 Capstone Design Poject. Department of Robotics. KwangWoon Univ.

This Repository contains Vision and AI part of GoBot project.

## Contents
- [Hardware](#hardware)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)


## Hardware
This Repository is for robot playing go. We use the following hardware.

- Camera: [APKO APC925](https://www.abko.co.kr/brand/detail.php?it_id=1611728230&device=pc)
- Robot Joint: [Dynamixel XL430](https://emanual.robotis.com/docs/kr/dxl/x/) x3, [Dynamixel XM430](https://emanual.robotis.com/docs/kr/dxl/x/) x3
- Robot Gipper: [Dynamixel XM330](https://emanual.robotis.com/docs/kr/dxl/x/) x2

![Robot Image](https://github.com/KW-Do-Everything/Go_bot/blob/9by9/github_img/Robot_Image.JPG?raw=true)

## Installation

Required [ROS2 Humble](https://docs.ros.org/en/humble/index.html), Ubuntu 22.04, python >= 3.10, pip, CUDA, CUDNN</br>


``` bash
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


```bash
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

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## Acknowledgements

This project uses code from the following projects:

- [usb_cam](https://github.com/username/awesome-library) - To using usb webcam in ROS2, Licensed under the BSD 2-Clause License.

- [KataGo](https://github.com/lightvector/KataGo) - This project relies on several other libraries, parts of libraries, or external files. For detailed license information, see the individual readmes and/or license files within the respective subdirectories of KataGo's repository.

### License Information for KataGo

KataGo is licensed under the MIT License. For the full license text, please refer to the [LICENSE](https://github.com/lightvector/KataGo/blob/master/LICENSE) file in the KataGo repository.

Additionally, KataGo relies on several other libraries, parts of libraries, or external files including clblast, filesystem-1.5.8, half-2.1.0, httplib, mozilla-cacerts, nlohmann_json, sgfmill, and tclap-1.2.2. For the licenses for those libraries and/or files, see the individual readmes and/or license files for each one within their respective subdirectories within `cpp/external`. Additionally, `cpp/core/sha2.cpp` derives from another piece of external code and embeds its own license within that file.

## Contact
//
