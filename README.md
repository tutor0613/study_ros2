# study_ros2
2022.02.03 ~ , Youngpyeong Kim
ROS2 personal study repo. 

<br>

### Study 기록

- **22.02.03** : ROS2 설치 및 환경 세팅
- **22.02.04** : repo 및 package 생성, `basic_pub`, `basic_sub` 작성
- **22.02.05** : `basic_msgs` pkg 생성, `argument_pub`, `calculator` 작성

<br>

### Package 구성

#### basic_pkg

- Python package (`build_type == ament_python`)
- `basic_pub.py`, `basic_sub.py`
  - 기본적인 ROS2 Publisher, Subscriber의 format.
- `argument_pub.py`, `calculator.py`
  - `argument_pub` 노드가 임의의 두개 변수 (`Int32`) 생성하여 Publish.
    (topic : `/argument`, type : `basic_msgs/msg/TwoInt32`)
  - `calculator` 노드에서 `argument` topic Subscribe하고,
    `operate_cmd` service를 통해 연산자 (+,-,/,*)를 입력받아 두 변수에 해당 연산 실행하여 return.
    - **Command Line을 통한 서비스 call 방법** (ROS1과 달리 자동완성 안 됨, 불친절함..)
      - `ros2 service call /operate_cmd basic_msgs/srv/OperateArgs "{cmd: '+'}"`

#### basic_msgs

- **msg**

  - `TwoInt32.msg`

    ```
    int32 a
    int32 b
    ```

- **srv**

  - `OperateArgs.srv`

    ```
    string cmd
    ---
    int32 result
    ```

    

<br>

### Requirements

- `basic_msgs` 패키지의 `CMakeLists.txt`에서 메시지 및 서비스 생성을 위해 `rosidl_default_generators` 패키지를 참조하는 과정에서, `openssl` dependency가 발생한다.
  - `sudo apt install libssl-dev` 로 설치하여 해결.

<br>





<br>

### Reference

- [ROS1/2 강좌 by 표윤석](https://cafe.naver.com/openrt/24070)
