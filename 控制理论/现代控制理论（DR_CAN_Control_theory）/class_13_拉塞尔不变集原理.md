## 回顾

回到上节课单摆加上摩擦的例子
$$
\ddot \theta + \frac gl\sin \theta +\frac{k}{ml}\dot \theta= 0 \\
$$

$$
\begin{aligned}
\dot x_1 &= x_2 \\
\dot x_2 &= -\frac gl\sin x_1 - \frac{k}{ml}x_2 \\
\end{aligned}
$$

找 $V$ 函数

​	还是从能量入手，令
$$
V = T+V = \frac12m x_2^2 l^2 + mgl(1-\cos x_1)
$$
分析 $V$ ：
$$
\dot V = \begin{bmatrix}\frac{\partial V}{\partial x_1}&\frac{\partial V}{\partial x_2}\end{bmatrix}
\begin{bmatrix}f_1 \\ f_2\end{bmatrix}
= 
-lkx_2^2
$$
按照往常来说，根据李雅普诺夫稳定性的分析，系统应该是稳定的。但是从物理常识来说，带摩擦的单摆最后应该停止才对（即渐进稳定）。为什么会这样呢？

回顾李雅普诺夫第二定理：

>
>
> $V(x)$ 的定义：广义能量函数
>
>1. 当且仅当 $x = 0$ 时，才有 $V(x) = 0$ 
>2. 当且仅当 $x≠0$ 时，才有 $V(x)>0$ 
>
>$\dot V(x)$ 的定义：$\dot V(x) = \frac{d}{dt}V(x) = \frac{\partial V(x)}{\partial x} \cdot \frac{dx}{dt}$ 
>
>- 若 $x≠0$ ， 有 $\dot V(x) \le 0$ ，则称系统在李雅普诺夫意义下是稳定的
>- 若 $x≠0$ ， 有 $\dot V(x)<0$ ，则系统是渐进稳定的 
>
>

以上分析都是系统稳定或者渐进稳定的充分条件，因此具有很大的保守性。也就是说，有些系统虽然基于李雅普诺夫定理推理出 $\dot V \le 0$ ，系统稳定的结论，但系统可能实际上是渐进稳定的。

**La Salle不变集（拉萨尔不变集）原理**就是基于 $\dot V \le 0$ ，却可能得到系统渐进稳定的结论，或者告诉你系统具体收敛到哪个值

## 拉塞尔不变集定理（LaSalle’s Invariance Principle）

这是李雅普诺夫方法的**推广与强化版本**。
它解决了李雅普诺夫第二定理中**$ \dot V(x)$ 半负定**时，无法得出 “渐近稳定” 的结论的问题。

设系统同样为

$$
\dot x = f(x)
$$

并且存在一个李雅普诺夫函数 $V(x)$，使得：

1. $V(x)$ 正定；
2. $\dot V(x) \le 0$ 

定义集合：
$$
E = \{x \mid \dot V(x) = 0\}
$$
设 $M$ 为系统在 $E$ 中的**最大不变集**（maximal invariant set），即所有轨迹一旦进入 $M$，就永远停留在 $M$ 中的点的集合。

**定理内容：**

> 所有系统轨迹最终都会收敛到集合 $M$。
>  如果 $M = \{0\}$，则原点是**渐近稳定**。

### 计算流程

1. 选 $V(x)$ ：设计一个在区域 $\Omega_l$ 内正定连续的标量函数

2. 计算 $\dot V(x)$ ：$\dot V(x) = L_fV(x) = \nabla V\cdot f(x)$ 

   - 如果 $\dot V(x) > 0$：重新设计 $V(x)$ 

   - 如果 $\dot V(x)<0$ ：直接得出原点在区域 $\Omega_l$ 内渐进稳定的结论 
   - 如果 $\dot V(x)\leq0$ ：进入下一步

3. LaSalle（拉塞尔）分析

   - 写出集合 $E = \{x\in \Omega_l:\dot V (x) = 0\}$ ，将 $\dot V$ 因式分解，得到若干的约束 $g_i(x) = 0$ 
   - 找最大不变集 $M$ ，对每个约束 $g_i$ 计算 Lie 导数 $L_fg_i = \nabla g_i\cdot f(x)$ 
     - 如果 $g_i(x) = 0$ 上的点有 $L_fg_i \ne 0$ ，则说明点会立刻离开流形，不属于不变集 $M$ ，将其剔除
     - 如果 $L_fg_i = 0$ 恒成立，该流形可能是不变的；可能还需继续对联合约束或对新得到的约束做相同检验（即迭代，或用高阶 Lie 导数 $L_f^2 g$ 等）。

   - 如果最后计算出来的 $M = \{ 0\}$ ，则说明系统的原点是渐进稳定的；若 $M$ 含有其他点，则不能推出渐进稳定
   - 所有系统轨迹最终都会收敛到集合 $M$。

4. **结合线性化/可达性判断细化**：当 $M$ 包含若干平衡点时，常用线性化判断这些平衡的稳定性。若它们是不稳定鞍且其稳定流形测度为零，则几乎所有初值会收敛到原点，但这不是 LaSalle 本身直接给出的——是组合结论（LaSalle + 局部线性化/不变流形理论）。

## 分析摆球阻尼系统的稳定性

回到之前的系统来
$$
\dot V = \begin{bmatrix}\frac{\partial V}{\partial x_1}&\frac{\partial V}{\partial x_1}\end{bmatrix}
\begin{bmatrix}f_1 \\ f_2\end{bmatrix}
= 
-lkx_2^2
$$
$\dot V = 0$ 时，将 $\dot V$ 因式分解，得到有
$$
g(x) = x_2 = 0
$$

$$
\begin{aligned}
L_fg &= \nabla g_i\cdot f(x) \\
&=
\begin{bmatrix}\frac{\partial g}{\partial x_1}&\frac{\partial g}{\partial x_2}\end{bmatrix}
\begin{bmatrix}f_1 \\ f_2\end{bmatrix}\\
&= \begin{bmatrix}0&1\end{bmatrix} 
\begin{bmatrix}x_2 \\ -\frac gl\sin x_1 - \frac{k}{ml}x_2\end{bmatrix}\\
&= -\frac gl\sin x_1 - \frac{k}{ml}x_2 \\
&= -\frac gl\sin x_1 \\
\end{aligned}
$$

由于 $x_1\in (-\pi, \pi)$ ，所以，当且仅当 $x_1 = 0$ 时，才有 $L_fg = 0$ 

得到最大不变集为  $M = \{ 0\}$ ，所以系统在 $x_1\in (-\pi, \pi)$ 内，**是渐进稳定的**

## 再举一个例子

对于系统
$$
\begin{aligned}
\dot x_1 &= x_2  \\
\dot x_2 &= -x_1 - x_2 - (x_1+x_2)^2x_2
\end{aligned}
$$
令 $V = x_1^2 + x_2 ^2$ 

得 
$$
\begin{aligned}
\dot V &= 2x_1\dot x_1 + 2x_2 \dot x_2 \\
&= 2x_1x_2 + 2x_2 (-x_1 - x_2 - (x_1+x_2)^2x_2) \\
&= -2x_2^2 (1 + (x_1+x_2)^2)
\end{aligned}
$$
令 $\dot V = 0$ ，得 
$$
g(x) = x_2 = 0
$$

$$
L_fg = -x_1 - x_2 - (x_1+x_2)^2x_2 = -x_1
$$

当且仅当 $x_1 = 0$ 时，才有 $L_fg = 0$ 

得到最大不变集为  $M = \{ 0\}$ ，所以系统**是渐进稳定的**

