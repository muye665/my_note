# 基本概念：

## Dockerfile

类似在虚拟机中安装操作系统和软件
自动化脚本，用于创建镜像

## image镜像
类似虚拟机的镜像，是只读的模板，包含部署的应用程序及其所有库，
可以创建多个容器

## container容器
类似一个个运行的虚拟机，每个容器独立运行
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

---

# docker教程

**教程网站：https://www.yuque.com/lart/ml-newer/fp6cla **

**官方命令教程：https://docs.docker.com/reference/cli/docker/**

## docker常用命令及其作用

- `docker pull [OPTIONS] NAME[:TAG|@DIGEST]`：从仓库中拉取指定**镜像**到本机

  - **`NAME` (必填)**
    - 镜像名称，格式通常为：`[仓库地址/][用户名/]镜像名`
    - 示例：
      - `ubuntu` → 官方 Ubuntu 镜像
      - `tencentcloudcr.com/uav_challenge/sdk` → 私有仓库镜像
  - **`:TAG` (可选)**
    - 指定镜像版本，默认 `latest`
    - 示例：
      - `nginx:1.25` → 下载 Nginx 1.25 版
      - `python:3.11-slim` → Python 3.11 精简版
  - **`@DIGEST` (可选)**
    - 通过唯一哈希值下载精确版本（防篡改）
    - 示例：
      `ubuntu@sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2`

  -  **常用选项（OPTIONS）**

    | 选项                      | 作用                     | 示例                                        |
    | :------------------------ | :----------------------- | :------------------------------------------ |
    | `-a` / `--all-tags`       | 下载镜像的所有版本       | `docker pull -a ubuntu`                     |
    | `--platform`              | 指定 CPU 架构            | `docker pull --platform linux/arm64 python` |
    | `-q` / `--quiet`          | 静默模式（仅显示镜像ID） | `docker pull -q nginx`                      |
    | `--disable-content-trust` | 跳过镜像验证（不推荐）   | 仅用于测试环境                              |

- `docker run`：**创建并启动一个全新容器**。每次执行，都会得到一个**全新的、独立的容器实例**，即使使用相同的镜像和相同的配置。它们拥有不同的容器 ID。用于**第一次启动一个容器**。

  过程：

  - **检查镜像：** 首先检查指定的镜像（例如 `nginx:latest`, `ubuntu:22.04`）是否存在于本地。如果不存在，它会自动从配置的镜像仓库（默认是 Docker Hub）**拉取**该镜像。
  - **创建容器：** 基于拉取或已有的镜像，**创建一个新的容器**。这个步骤在文件系统层面为容器建立了可写层（用于存储运行时产生的数据）。
  - **配置容器：** 应用你通过命令行选项提供的所有配置（`-d` 后台运行、`-p` 端口映射、`-v` 卷挂载、`-e` 环境变量、`--name` 指定容器名、`--network` 网络设置等等）。
  - **启动容器：** 最后，在新建的容器内部**执行默认命令**（通常是 Dockerfile 中定义的 `CMD` 或 `ENTRYPOINT`）来启动容器的主进程。

  里面有很多常用的参数：
  
  - 例子：
  
    ```bash
    docker run -d --gpus all --name race_user_sdk_container uav-challenge.tencentcloudcr.com/uav_challenge_2025/uav_challenge:sdk tail -f /dev/null
    ```
    
  - **`-d`**：在后台运行
  
  - **`--gpus all`**：允许容器访问宿主机上的**所有 GPU 资源**
  
  - **`--name race_user_sdk_container`**：为容器指定易读的名称（代替自动生成的 ID）
  
  - **`tail -f /dev/null`**（保持容器运行的技巧）：`/dev/null` 是空设备文件，永远不产生数据，`tail -f` 会持续等待新内容（实际永远等不到）




- `docker load`：从tar压缩文件，或从一个文件或者STDIN中, 加载镜像或仓库. 它可以**恢复镜像**和标签

  

- `docker images`：查看本机已保存的**镜像**

- `docker ps`：查看**正在运行的容器**信息列表，

  
    - 加上 `-a ` 查看所有容器信息：`docker ps -a`
    
      



- `docker rm`：删除指定**容器**

- `docker rmi`：删除指定**镜像**

  删除有多种方式：

  - 使用IMAGE ID：`docker rmi fd484f19954f`

  - 使用TAG：`docker rmi test:latest`

  - 使用DIGEST： `docker rmi localhost:5000/test/busybox@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf`

    

- `docker start`：启动一个已停止的**容器**，

- `docker restart`：重启一个容器，`start`  或者 `restart`  启动的容器**会自动以分离模式运行**

- `docker stop`：停止**容器**运行，正常关闭（如数据库、Web服务）

- `docker kill` ：直接关闭容器，立即杀死进程


    - `-t`  : 关闭容器的限时, 如果超时未能关闭则用 `kill`  强制关闭, 默认值10s, 这个时间用于容器的自己保存状态


​      



- `docker attach`：**进入容器**，退出后会把容器关闭

- `docker exec`：**进入容器**，退出后不会把容器关闭


    - `docker exec [OPTIONS] CONTAINER COMMAND [ARG...]`

  - | 参数        | 说明                                                      |
    | :---------- | :-------------------------------------------------------- |
    | `CONTAINER` | 容器名或容器ID（`docker ps` 可查）                        |
    | `COMMAND`   | 要在容器内执行的命令（如 `/bin/bash`、`python`、`ls` 等） |
    | `ARG...`    | 命令的参数（如 `ls -l /app` 中的 `-l` 和 `/app`）         |


    - 常用：`docker exec -it 容器名称 bash`，  **进入正在运行的 Docker 容器内部**，并启动一个交互式的 Bash Shell
      
    - （`-i` ：保持标准输入（STDIN）打开，允许交互式操作（如输入命令）；`-t`：分配一个伪终端（TTY），使 Shell 操作更直观（支持格式化输出、快捷键等））




- `exit`：**退出容器**

  

- `docker cp`：用于容器与主机之间的数据拷贝

- `docker build`：**从零构建新镜像**，通过读取**Dockerfile** 中的指令，**自动构建一个全新的 Docker 镜像**

- `docker commit`：**将容器的当前状态保存为新镜像**，相当于给容器拍"快照"并固化为镜像

- `docker save`：**将镜像导出为 tar 归档文件**，把**已存在的镜像**（包括所有层）打包成单个文件

  

- `docker system prune`：最全面的**清理无用数据**，把你暂时关闭的容器, 以及暂时没有用到的 Docker 镜像都删掉.。

- `docker volume prune`：对于数据卷volumes的删除

- `docker container prune`：对于容器的删除

- `docker image prune`：对于镜像的删除

- `systemctl restart docker`：重启docker

---

## docker大概的流程：

1. **`docker build`**
   → **从 Dockerfile 构建镜像**
   *（输入：Dockerfile + 代码文件；输出：镜像）*

   ```bash
   docker build -t my-image:1.0 .  # 构建并命名镜像
   ```

2. **`docker run`**
   → **根据镜像创建并启动新容器**
   *（基于镜像生成容器实例）*

   ```bash
   docker run -d --name my-container my-image:1.0  # 后台启动容器
   ```

3. **`docker exec`**
   → **进入运行中的容器调试**
   *（在已运行的容器内执行临时命令）*

   ```bash
   docker exec -it my-container bash  # 进入容器终端
   ```

4. **修改并测试**
   → 在容器内修改文件/配置（**注意：这些修改默认仅存在于当前容器中，不会影响原始镜像！**）

------

### ⚠ 关键纠正：如何永久保存修改？

1. **`docker commit`**（必要步骤！）
   → **将容器的修改保存为新镜像**
   *（把调试后的容器状态固化为新镜像）*

   ```bash
   docker commit my-container my-modified-image:1.1  # 保存容器为新镜像
   ```

2. **验证新镜像**
   → 基于新镜像启动容器测试

   ```bash
   docker run -d --name test-container my-modified-image:1.1
   ```

------

### 后续操作

1. **生命周期管理**

   ```bash
   docker stop test-container  # 停止容器
   docker start test-container # 重启容器（保留文件修改）
   docker rm test-container    # 删除容器
   ```

2. **分发镜像（二选一）**

   - **推荐：`docker push`（上传到镜像仓库）**

     ```bash
     docker tag my-modified-image:1.1 my-repo.com/my-image:1.1
     docker push my-repo.com/my-image:1.1
     ```

   - **离线方案：`docker save`（导出为文件）**

     ```bash
     docker save -o my-image.tar my-modified-image:1.1  # 导出镜像
     # 对方用 docker load -i my-image.tar 导入
     ```

---

## docker容器挂载：

#### 1. **绑定挂载（Bind Mount）** - 最常用

直接将宿主机**特定路径**映射到容器内

```bash
# 语法
docker run -v /宿主机/路径:/容器内/路径 镜像名

# 示例：将宿主机的 /home/user/data 映射到容器的 /app/data
docker run -d -v /home/user/data:/app/data nginx
```

**特点**:

- 路径需绝对路径
- 宿主机目录不存在时会自动创建
- 适合开发环境（代码实时同步）

#### 2. **卷挂载（Volume Mount）** - 生产推荐

使用 Docker 管理的**命名卷**（存储在 `/var/lib/docker/volumes/`）

```bash
# 创建卷
docker volume create my_vol

# 挂载卷
docker run -d -v my_vol:/容器内/路径 镜像名

# 示例
docker run -d -v db_data:/var/lib/mysql mysql
```

**特点**：

- Docker 自动管理存储位置
- 支持权限控制、备份、迁移
- 适合数据库、生产环境数据

#### 3. **临时文件系统挂载（tmpfs）** - 特殊场景

将数据存储在**内存**中（容器销毁后消失）

```bash
docker run -d --tmpfs /容器内/路径 镜像名
# 示例：敏感临时数据
docker run --tmpfs /app/tmp nginx
```

**特点**：

- 数据只存在内存中
- 读写速度极快
- 适合处理敏感临时数据

------

###  挂载操作详解

#### 常用参数：

| 参数               | 作用                                               |
| :----------------- | :------------------------------------------------- |
| `-v` 或 `--volume` | 传统挂载方式（推荐简单场景）                       |
| `--mount`          | 更详细的挂载语法（支持高级配置）                   |
| `:ro` / `:rw`      | 设置只读/读写（默认rw）如 `-v /host:/container:ro` |
| `--tmpfs`          | 内存挂载                                           |

#### 示例对比：

```bash
# 方式1：-v 简写
docker run -v /host/data:/container/data nginx

# 方式2：--mount 详细配置
docker run \
  --mount type=bind,source=/host/data,target=/container/data,readonly \
  nginx
```

------

### 查看挂载信息

```bash
# 查看容器挂载详情
docker inspect 容器名 | grep Mounts -A 20

# 列出所有卷
docker volume ls
```

------

### ⚠️ 挂载注意事项

1. **目录覆盖规则**
   - 如果挂载到**非空容器目录**：容器原有内容会被隐藏（仍存在，但不可访问）
   - 挂载**空宿主机目录**到容器非空目录：容器内容会复制到宿主机目录








## docker网络环境配置解决方案
### 第一步：检查并调整代理设置
```bash
# 1. 查看当前代理设置
env | grep -i proxy
# 2. 临时禁用代理（当前终端会话）
unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY
# 3. 再次测试连接
curl -v https://registry-1.docker.io/v2/
```

### 第二步：检查代理服务状态
```bash
# 1. 检查代理服务是否运行
netstat -tuln | grep 7897
# 2. 测试代理服务器是否工作
curl -x http://127.0.0.1:7897 https://www.google.com
```

### 第三步：配置 Docker 使用代理
```bash
# 1. 创建 Docker 代理配置文件
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo nano /etc/systemd/system/docker.service.d/http-proxy.conf
添加以下内容（根据您的代理设置调整）：

ini
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:7897"
Environment="HTTPS_PROXY=http://127.0.0.1:7897"
Environment="NO_PROXY=localhost,127.0.0.1,192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,::1"
```

```bash
# 2. 重新加载并重启 Docker
sudo systemctl daemon-reload
sudo systemctl restart docker

# 3. 检查代理是否生效
sudo systemctl show --property=Environment docker
```
### 第四步：配置 Docker 使用镜像加速器（推荐）
```bash
# 1. 创建配置文件
sudo nano /etc/docker/daemon.json
添加以下内容（使用阿里云镜像加速器）：

json
{
  "registry-mirrors" : ["https://docker.registry.cyou",
"https://docker-cf.registry.cyou",
"https://dockercf.jsdelivr.fyi",
"https://docker.jsdelivr.fyi",
"https://dockertest.jsdelivr.fyi",
"https://mirror.aliyuncs.com",
"https://dockerproxy.com",
"https://mirror.baidubce.com",
"https://docker.m.daocloud.io",
"https://docker.nju.edu.cn",
"https://docker.mirrors.sjtug.sjtu.edu.cn",
"https://docker.mirrors.ustc.edu.cn",
"https://mirror.iscas.ac.cn",
"https://docker.rainbond.cc",
"https://do.nark.eu.org",
"https://dc.j8.work",
"https://dockerproxy.com",
"https://gst6rzl9.mirror.aliyuncs.com",
"https://registry.docker-cn.com",
"http://hub-mirror.c.163.com",
"http://mirrors.ustc.edu.cn/",
"https://mirrors.tuna.tsinghua.edu.cn/",
"http://mirrors.sohu.com/" 
],
 "insecure-registries" : [
    "registry.docker-cn.com",
    "docker.mirrors.ustc.edu.cn"
    ],
"debug": true,
"experimental": false
}
```
```bash
# 2. 重启 Docker
sudo systemctl daemon-reload
sudo systemctl restart docker

# 3. 查看镜像加速器配置
docker info | grep "Registry Mirrors"
```

 
