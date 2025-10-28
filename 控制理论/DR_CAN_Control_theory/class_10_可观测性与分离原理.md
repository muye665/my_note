# 可观测性

假如有一个系统
$$
\dot x = Ax + Bu \\
y = Cx + Du \\
$$
observer（观测器）

x 不可测是，设 $\hat x$ 为估计值

令
$$
\hat{\dot{x}} = A\hat x + B u+L(y - \hat y) \\
\hat y = C \hat x +D u 
$$
令 $e_x = x - \hat x$
$$
\dot{\hat e}_x = (A - LC)e_x \\ 
$$
然后用特征值来设计观测器

但是有一个前提，是否所有系统都是可测的？

### 定义

过一个系统可观测，则
$$
O = 
\begin{bmatrix}
C \\ ... \\ CA^{n-2} \\ CA^{n-1} \\
\end{bmatrix}  \\
$$
如果
$$
Rank(O) = n
$$
则系统是可观测的

### 可观测公式推导

这部分老师跳过，补充一下

#### 可控性的定义

已知从时刻 $t_0$ 开始系统在一段有限时间内（例如到 $t_1$）的所有输入 $u(t)$ 和输出 $y(t)$（离散时为序列 $u_k,y_k$ ），那么是否能够**唯一确定初始状态** $x(t_0)$（或在离散情形下的 $x_0$）

对于离散系统
$$
x_{k+1} = Ax_k + Bu_k \\
y_k = Cx_k + Du_k \\
$$


令 $u_k≡0$ 
$$
x_{k} = A^{k}x_0 \\
y_k = C x_k
$$
随时间推移，有
$$
\begin{aligned}
 y_0 &= C x_0 \\
 y_1 &= CA x_0 \\
 y_2 &= CA^2 x_0\\
&...\\
 y_{n-1} &= CA^{n-1} x_0
\end{aligned}
$$
提取出最后一个状态
$$
y_n = 
\begin{bmatrix}
C & ... & CA^{n-2} & CA^{n-1} \\
\end{bmatrix}
\; x_0 
= O x_0 
$$
**如果系统可观测，则方程应该有解。根据线性代数秩的定义，上述式子若有解，则他的秩必须为 $n$ 。即**
$$
Rank(O) = n
$$

对于连续系统同理



> 简单的例子：
> $$
> \dot x = 
> \begin{bmatrix} 0 & 1 \\ 2 & -1\end{bmatrix} x + 
> \begin{bmatrix} 0 \\ 1\end{bmatrix} u \\
> y = \begin{bmatrix} -1 & 1\end{bmatrix}x
> $$
> 计算 $O$ 矩阵及其秩
> $$
> O = \begin{bmatrix} -1 & 1 \\ 2 & -2\end{bmatrix} \\
> Rank(O) = 1 \neq n
> $$
> 所以系统不可观测
>
> 

# 观测器 + 控制器

$$
\dot x = Ax + Bu \\
y = Cx \\
$$

假如有一个系统，其状态 $x$ 不可测量，但是是可控可观测的，要我们给他设计控制器和观测器

## 1. 观测器

$$
\dot{\hat x} = A \hat x +B u + L(y - \hat y) \\
$$

$$
\dot{e}_x = (A - LC) e_x \\ \tag 1
$$

计算矩阵 $A - LC$ 的特征值

## 2. 观测器

令 $u = -k\hat x$ 
$$
\dot x = Ax -Bk\hat x \\
$$

$$
\dot x = (A - Bk)x + Bke_x \tag 2
$$



(1) 、(2) 联立得 （一个新系统）
$$
\begin{bmatrix} \dot e_x  \\ \dot x \end{bmatrix}
= 
\begin{bmatrix} A - LC &  0 \\ B & A - Bk \end{bmatrix}
\begin{bmatrix} e_x  \\ x \end{bmatrix}
$$
其中
$$
M = \begin{bmatrix} A - LC &  0 \\ B & A - Bk \end{bmatrix}
$$
如果要让 $e_x \rightarrow 0 ,x \rightarrow 0$ 

那么就要 $M$ 矩阵的所有特征值的实部一定要小于0，才能稳定

$M$ 矩阵是三角矩阵，其特征值为对角线元素的特征值，**即 $M$ 矩阵的特征值就是 $A - LC$ 和 $A - Bk$  两个矩阵的的特征值**

这就是分离原理，即把控制器和观测器分开

- 思考：当设计观测器和控制器合并的系统时，观测器要比控制器收敛快，因为要有一个准确的值来确定系统的输入

