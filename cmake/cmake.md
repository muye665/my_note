### 🧩 常用变量/宏及其用途

| 变量名                             | 说明                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| `catkin_INCLUDE_DIRS`              | 所有 catkin 依赖包导出的头文件路径（用于 `include_directories`） |
| `catkin_LIBRARIES`                 | 所有 catkin 依赖包导出的库（用于 `target_link_libraries`）   |
| `catkin_PACKAGE_BIN_DESTINATION`   | 安装可执行文件的目标路径                                     |
| `CMAKE_CURRENT_SOURCE_DIR`         | 当前处理的 `CMakeLists.txt` 所在的目录                       |
| `CMAKE_CURRENT_BINARY_DIR`         | 当前构建的中间文件目录（build 目录下的子目录）               |
| `PROJECT_SOURCE_DIR`               | 顶层 CMakeLists.txt 所在的目录                               |
| `PROJECT_NAME`                     | 项目的名称（由 `project()` 设置）                            |
| `catkin_PACKAGE_SHARE_DESTINATION` | 安装资源文件的路径（如 `.launch`、`.yaml`）                  |
| `CATKIN_DEVEL_PREFIX`              | `devel` 目录的路径（开发空间）                               |
| `CMAKE_INSTALL_PREFIX`             | 安装目录前缀，默认是 `/opt/ros/<distro>`                     |

1、指定 CMake 的最低版本要求：

```
cmake_minimum_required(VERSION 版本号)
```

例如：

```cmake
cmake_minimum_required(VERSION 3.10)
```

2、定义项目的名称和使用的编程语言：

```cmake
project(项目名)
```

例如：

```cmake
project(MyProject)
```

3、指定要生成的可执行文件和其源文件：

```cmake
add_executable(可执行文件的名称（自己命名） 文件来源（路径）)
```

例如：

```cmake
add_executable(MyExecutable main.cpp other_file.cpp)
```

4、创建一个库（静态库或动态库）及其源文件：

```cmake
add_library(库名称（自己命名） 文件来源)
```

例如：

```cmake
add_library(drone_control_lib library.cpp)
```

5、链接目标文件与其他库：

```cmake
target_link_libraries(可执行文件的名称（自己命名） 库名称（自己命名）)
```

例如：

```cmake
target_link_libraries(MyExecutable drone_control_lib)
```

6、添加头文件搜索路径，用于指定头文件搜索路径的命令。它会告诉编译器在指定的目录中查找头文件（`.h` 文件），这样在代码中使用 `#include` 时就不需要写完整路径了。

```cmake
include_directories(<dirs>...)
```

例如：

```cmake
include_directories(${PROJECT_SOURCE_DIR}/include)
```

7、安装规则：

```cmake
install(TARGETS target1 [target2 ...]
        [RUNTIME DESTINATION dir]
        [LIBRARY DESTINATION dir]
        [ARCHIVE DESTINATION dir]
        [INCLUDES DESTINATION [dir ...]]
        [PRIVATE_HEADER DESTINATION dir]
        [PUBLIC_HEADER DESTINATION dir])
```

例如：

```cmake
install(TARGETS MyExecutable RUNTIME DESTINATION bin)
```

