catkin build 后报错

> Errors     << odom_visualization:make /home/ham/all_ws/ego_planner/logs/odom_visualization/build.make.011.log /usr/bin/ld: 找不到 -lpose_utils collect2: error: ld returned 1 exit status make[2]: *** [CMakeFiles/odom_visualization.dir/build.make:110：/home/ham/all_ws/ego_planner/devel/.private/odom_visualization/lib/odom_visualization/odom_visualization] 错误 1 make[1]: *** 
>
> [CMakeFiles/Makefile2:200：CMakeFiles/odom_visualization.dir/all] 错误 2 make: *** [Makefile:141：all] 错误 2 cd /home/ham/all_ws/ego_planner/build/odom_visualization; catkin build --get-env odom_visualization | catkin env -si  /usr/bin/make --jobserver-auth=3,4; cd -

将 `odom_visualization`、 `multi_map_server` 这两个包的 `Cmakelist.txt` 的 `target_link_libraries{}` 中的 `pose_utils` 移动到 `catkin_package{}` 部分即可

