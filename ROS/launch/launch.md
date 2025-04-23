赵虚左launch教程：
http://www.autolabor.com.cn/book/ROSTutorials/5/45-rosjie-dianguan-li-launch-wen-jian.html

`<arg>`、`<param>` 和 `<rosparam>` 是三种不同的元素，各自有独特的作用域和用途。以下是它们的核心区别和关联：

------

### **1. `<arg>`：启动文件的内部参数**

- **功能**：用于定义**启动文件内部的变量**，类似脚本中的局部变量，仅在启动文件范围内有效。

- **核心特点**：

  - **作用域**：**仅在当前启动文件（或通过 `include` 传递的子文件）中有效。**
  - **不存储到参数服务器**：节点无法直接访问 `<arg>` 的值。
  - **用途**：动态配置启动文件的行为（如选择配置、路径、开关等）。

- **示例**：

  ```xml
  <!-- 定义默认值 -->
  <arg name="sim_mode" default="true" />
  <!-- 通过命令行覆盖 -->
  <arg name="map_file" default="default_map.yaml" />
  
  <!-- 使用 $(arg) 动态替换 -->
  <param name="use_sim_time" value="$(arg sim_mode)" />
  <rosparam command="load" file="$(find pkg)/maps/$(arg map_file)" />
  ```

------

### **2. `<param>`：ROS 参数服务器的参数**

- **功能**：在 **ROS 参数服务器** 上定义或修改参数，节点可通过 `ros::param::get()` 访问。

- **核心特点**：

  - **全局可见**：所有节点均可读取或修改。
  - **持久性**：参数存储在参数服务器中，直到 ROS 关闭或被覆盖。
  - **支持简单类型**：如整数、字符串、布尔值等。

- **示例**：

  ```xml
  <param name="max_speed" type="double" value="2.0" />
  <param name="sensor_enabled" value="true" />
  ```

------

### **3. `<rosparam>`：批量操作参数服务器**

- **功能**：批量加载或操作参数服务器中的参数，支持复杂数据结构（如字典、列表）和文件交互。

- **核心特点**：

  - **批量操作**：一次可加载多个参数（如从 YAML 文件）。
  - **支持嵌套结构**：例如 `camera/resolution: [1920, 1080]`。
  - **文件交互**：直接从 YAML 文件加载或保存参数。

- **示例**：

  ```xml
  <!-- 从文件加载参数 -->
  <rosparam command="load" file="$(find pkg)/config/params.yaml" />
  
  <!-- 直接在 Launch 文件中定义参数组 -->
  <rosparam command="load">
    navigation:
      max_speed: 1.5
      waypoints: [1, 2, 3]
  </rosparam>
  ```

------

### **4. 三者的关键区别**

| **特性**     | **`<arg>`**                | **`<param>`**          | **`<rosparam>`**                 |
| :----------- | :------------------------- | :--------------------- | :------------------------------- |
| **作用域**   | 启动文件内部               | ROS 参数服务器（全局） | ROS 参数服务器（全局）           |
| **存储位置** | 启动文件解析时的内存变量   | 参数服务器             | 参数服务器                       |
| **数据结构** | 简单值（字符串、布尔值等） | 简单值                 | 复杂结构（字典、列表、YAML文件） |
| **节点访问** | 节点无法直接访问           | 节点可通过 API 读取    | 节点可通过 API 读取              |
| **典型用途** | 动态配置启动文件行为       | 定义全局简单参数       | 批量加载复杂参数                 |

------
