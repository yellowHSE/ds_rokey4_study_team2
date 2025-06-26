# 컴퓨터비전 스터디 기록 📚  

## 14주차 - ROS2 CLS (Node, Topic, Service, Parameter)

### ✅ 학습 목표
- ROS2의 기본 구성 요소(Node, Topic, Service, Parameter)에 대한 구조적 이해
- 각 기능의 명령어 실습을 통해 실제 통신 흐름 및 설정 방식 숙지
- rqt 도구를 활용하여 시각적으로 시스템 구성 파악
- ROS2 Humble 공식 문서를 기반으로 기초 개념과 CLI 실습 체득  

> 📚 실습 참조 자료:  
> - [Introducing Turtlesim](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html)  
> - [Understanding ROS 2 Nodes](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)  
> - [Understanding ROS 2 Topics](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)  
> - [Understanding ROS 2 Services](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)  
> - [Understanding ROS 2 Parameters](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters.html)  

---

### 🧩 주요 학습 내용

#### 🔹 Node(전효재)
- ROS 시스템의 최소 실행 단위
- 하나의 노드는 센서 처리, 제어 명령 등 하나의 기능 수행
- `ros2 node list` 명령어로 활성 노드 확인 가능

#### 🔹 Topic(김사웅)
- 메시지를 퍼블리셔 → 서브스크라이버 구조로 비동기 전송
- `ros2 topic pub`으로 주기적 메시지 발행 가능
- `/turtle1/cmd_vel`은 대표적인 속도 제어 토픽

#### 🔹 Service(홍송은)
- 클라이언트가 명시적 요청(Request)을 보내면 서버가 응답(Response) 반환
- 단발성 1:1 동기식 통신에 적합
- 주요 명령어:
  - `ros2 service list`  
  - `ros2 service call <name> <type> <args>`  
  - `ros2 interface show <type>`

#### 🔹 Parameter(홍송은)
- 노드의 설정값을 런타임에 읽고 수정 가능
- `ros2 param set`, `dump`, `load` 명령어 사용
- `.yaml` 파일을 통한 파라미터 저장 및 불러오기 가능

#### 🔹 rqt(전효재)
- GUI 기반 시각화 도구
- `rqt` 실행 후 turtle 제어 가능 (r, g, b 색상 및 선 굵기 조정)
- 복수 터틀봇 제어 시 리매핑 사용:
  - `--ros-args -r /turtle1/cmd_vel:=/turtle2/cmd_vel`