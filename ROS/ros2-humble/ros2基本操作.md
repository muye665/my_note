

# ROS2 Humble：Ubuntu 22.04 下创建工作空间与功能包流程笔记

本文整理 ROS2 Humble 常用的基础操作，包括 **创建工作空间（workspace）** 与 **创建功能包（package）** 的标准流程。适合经常使用 ROS1、偶尔忘记 ROS2 指令时快速回顾使用。

------

## 🗂️ 一、创建 ROS2 工作空间（colcon 构建体系）

### 1. 创建工作空间目录结构

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

ROS2 默认使用 `colcon`，不再使用 catkin_make / catkin build。

------

### 2. 构建工作空间

```bash
colcon build
```

构建后会生成：

- `build/`
- `install/`
- `log/`

------

### 3. 让环境生效（source）

每次启动终端（或写入 `.bashrc`）后执行：

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```

若希望自动生效，可加入 `~/.bashrc`：

```bash
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
```

------

## 📦 二、在工作空间中创建功能包

### 1. 进入工作空间的 src 目录

```bash
cd ~/ros2_ws/src
```

------

### 2. 创建功能包

ROS2 使用 `ros2 pkg create`。

#### 创建 C++ 功能包（ament_cmake）

```bash
ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp std_msgs
```

#### 创建 Python 功能包（ament_python）

```bash
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy std_msgs
```

常用参数：

| 参数                        | 说明                                  |
| --------------------------- | ------------------------------------- |
| `--build-type ament_cmake`  | C++ 包（类似 catkin）                 |
| `--build-type ament_python` | Python 包                             |
| `--dependencies`            | 自动写入 CMakeLists.txt / package.xml |

------

## ⚙️ 三、再次构建整个工作空间

```bash
cd ~/ros2_ws
colcon build
```

如果你只想编译其中一个包：

```bash
colcon build --packages-select my_cpp_pkg
```

------

## ▶️ 四、运行 ROS2 节点

### 1. 进入终端并 source 工作空间环境

```bash
source ~/ros2_ws/install/setup.bash
```

### 2. 运行节点（示例）

C++：

```bash
ros2 run my_cpp_pkg my_node_exe
```

Python：

```bash
ros2 run my_py_pkg my_node.py
```

> 注意：Python 的节点可执行权限需设置：

```bash
chmod +x my_py_pkg/my_py_pkg/my_node.py
```

------

## 🔎 五、检查包、节点

列出所有包：

```bash
ros2 pkg list
```

检查某个包的信息：

```bash
ros2 pkg xml my_cpp_pkg
```

列出可执行节点：

```bash
ros2 run my_cpp_pkg --ros-args
```

查看 topic：

```bash
ros2 topic list
```

查看参数：

```bash
ros2 param list
```

------

## 📌 六、ROS1 与 ROS2 的命令差异备忘

### 🔧 构建体系

| ROS1                       | ROS2         |
| -------------------------- | ------------ |
| catkin_make / catkin build | colcon build |

### 📦 创建包

| ROS1                           | ROS2                                        |
| ------------------------------ | ------------------------------------------- |
| catkin_create_pkg pkg std_msgs | ros2 pkg create pkg --dependencies std_msgs |

### ▶️ 运行节点

| ROS1            | ROS2              |
| --------------- | ----------------- |
| rosrun pkg node | ros2 run pkg node |

### 📡 topic 指令

| ROS1               | ROS2                 |
| ------------------ | -------------------- |
| rostopic list      | ros2 topic list      |
| rostopic echo /xxx | ros2 topic echo /xxx |

------

## ✔️ 七、总结流程（速查版）

```bash
# 1. 创建工作空间
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source ~/ros2_ws/install/setup.bash

# 2. 创建包
cd ~/ros2_ws/src
ros2 pkg create demo_pkg --build-type ament_cmake --dependencies rclcpp std_msgs

# 3. 构建
cd ~/ros2_ws
colcon build --packages-select demo_pkg

# 4. 运行节点
source install/setup.bash
ros2 run demo_pkg demo_node
```

这样就完成了 ROS2 Humble 的基本使用流程。
