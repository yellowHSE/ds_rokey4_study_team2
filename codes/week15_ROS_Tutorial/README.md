# 컴퓨터비전 스터디 기록 📚  

## 15주차 - ROS2 사용자 정의 인터페이스 및 통신 구조 실습

### ✅ 학습 목표
- ROS 2의 Topic 기반 비동기 통신 구조와 Service 기반 동기 통신 구조 이해  
- 사용자 정의 메시지(.msg)와 서비스(.srv) 생성 및 활용 방법 숙지  
- Publisher/Subscriber, Service/Client 구성 실습을 통해 ROS 2 통신 흐름 체험  
- Python 및 C++ 패키지를 통한 실제 예제 구현과 빌드/실행 과정 실습  
- ROS 2 Humble 공식 문서를 기반으로 실습하며 기본 구조와 사용법 체득  

> 📚 실습 참조 자료:  
> - [Writing a Simple Python Publisher and Subscriber (ros2 doc)](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)  
> - [Writing a Simple Python Service and Client (ros2 doc)](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html)  
> - [Creating Custom ROS 2 Interfaces (ros2 doc)](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html)  

---

### 🧩 주요 학습 내용
#### 전효재
- Topic 기반 통신 구조 학습  
 - Publisher는 토픽으로 데이터를 발행  
 - Subscriber는 해당 토픽을 구독해 데이터 수신  
 - ROS 전체 통신의 약 70% 이상을 차지하는 주요 방식  
- 실습 명령어  
 - `ros2 run my_first_package my_first_node`  
 - `ros2 run my_first_package my_subscriber`  
 - `ros2 run py_pubsub listener`  

#### 김사웅
- Service 기반 통신 구조 실습 (C++)  
 - `ros2 pkg create cpp_srvcli --build-type ament_cmake`  
 - `add_two_ints_server.cpp`, `add_two_ints_client.cpp` 작성  
 - `CMakeLists.txt`에서 `add_executable`, `ament_target_dependencies`, `install()` 설정  
 - Service는 명시적 요청에만 응답, 토픽과 달리 동기 구조  

#### 홍송은
- ROS 2 Custom Interface 생성 및 활용 실습 (Python)  
 - `tutorial_interfaces` 패키지 생성, `msg`, `srv` 디렉토리 구성  
 - `Num.msg`, `Sphere.msg`, `AddThreeInts.srv` 정의  
 - `rosidl_generate_interfaces()` 호출, `package.xml` 의존성 설정  
 - Python 패키지(py_pubsub, py_srvcli)에서 import 및 실행 설정  
 - `call_async()`와 `rclpy.spin_once()`를 통한 비동기 클라이언트 구조
 - `ros2 run`으로 서비스 요청/응답 테스트 진행  