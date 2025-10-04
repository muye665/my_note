## 状态空间方程的解

对于一个**一阶常系数微分方程** $\dot{x}(t) = ax(t)$ 来说，其解为 $x(t) = x(0)e^{at}$

- 推导：

对其两边进行拉普拉斯变换得

$$
sX(s) - x(0) = aX(s) \\
$$

其中 $x(0)$ 是函数 $x(t)$ 在 $t = 0$  时的初始值，化简得

$$
X(s) = \frac{x(0)}{s - a}
$$

已知函数 $\frac{1}{s-a}$ 的拉普拉斯逆变换是 $e^{at}$ ，所以解得

$$
x(t) = x(0)e^{at}
$$

---

现在分析一个多变量耦合的状态空间方程

$$
\dot{x}_1(t) = x_1(t)+x_2(t) \\
\dot{x}_2(t) = 4x_1(t)-2x_2(t)
$$

根据状态空间方程

$$
\boxed{
\frac{d\vec{x}}{dt} = A\vec{x}
}
$$

有

$$
A = 
\begin{bmatrix}
1 & 1 \\
4 & -2 \\
\end{bmatrix}
$$

如果要求解 $\vec{x}$ ，按照我们之前的解，有

$$
\vec{x}(t) = e^{At}\,\vec{x}(0)
\tag{1}
$$

已知 $\vec{x}(t)$ 、 $\vec{x}(0)$ 都是 $n*1$ 的向量，所以 $e^{At}$ 应该是 $n*n$ 的矩阵

至于  $e^{At}$ 具体应该是怎么样的？我们把 (1) 带入到前面方框中去，得到

$$
\frac{de^{At}\,\vec{x}(0)}{dt} 
=
Ae^{At}\,\vec{x}(0)
$$

$\vec{x}(0)$ 为常数，消去得

$$
\frac{de^{At}}{dt} 
=
Ae^{At}
\tag{2}
$$

现在，我们对 $e^{At}$ 和 $\frac{de^{At}}{dt}$ 进行泰勒展开

$$
e^{At} = I + At + \frac{1}{2!}(At)^2 + \frac{1}{3!}(At)^3 + ...
\tag{3}
$$

$$
\frac{de^{At}}{dt} = 0 + A + A^2t + \frac{1}{2!}A^3t^2 + ... = Ae^{At}
$$

(3) 就被称为**矩阵的指数函数** 

现在我们分析，当矩阵 $A$ 不同时，其指数函数 $e^{At}$ 是怎么样的？

1. $A = 0$ :

$$
  e^{At} = I
$$

2. $A = \Lambda = \text{diag}(\, \lambda_{1}, \lambda_{2}, \lambda_{3} \,)$  

   $$
   \begin{aligned}
   e^{ \Lambda t} 
   &=
   I + \Lambda t + \frac{1}{2!}(\Lambda t)^2 + \frac{1}{3!}(\Lambda t)^3 + ... \\
   &=
   \begin{bmatrix}
   1 + \lambda_1 t + \frac{1}{2!}(\lambda_1)^2 +  &  \\
   & 1 + \lambda_2 t + \frac{1}{2!}(\lambda_2)^2 + \\
   && \ddots \\
   &&& 1 + \lambda_n t + \frac{1}{2!}(\lambda_n)^2 + \\
   \end{bmatrix}\\
   &=
   \begin{bmatrix}
   e^{\lambda_1} &  \\
   & e^{\lambda_2}  \\
   && \ddots \\
   &&& e^{\lambda_n} \\
   \end{bmatrix}
   \end{aligned}
   $$

3. $A$ **有 n 个线性无关的特征向量**， $A = P\Lambda P^{-1}$ ， $\Lambda$ 的元素都是 $A$ 的特征值，过渡矩阵 $P$ 为 $A$ 的特征向量

   $$
   \begin{aligned}
   e^{At} &= I + At + \frac{1}{2!}(At)^2 + \frac{1}{3!}(At)^3 + ... \\
   e^{At} &= PP^{-1} + P\Lambda P^{-1}t + \frac{1}{2!}(P\Lambda P^{-1}t)^2 + \frac{1}{3!}(P\Lambda P^{-1}t)^3 + ... \\
   P^{-1}e^{At}P &= I + \Lambda t + \frac{1}{2!}(\Lambda t)^2 + \frac{1}{3!}(\Lambda t)^3 + ... \\ 
   e^{At} &= Pe^{ \Lambda t}P^{-1}
   \end{aligned}
   $$

   ---

现在我们来解状态空间方程 $\frac{d\vec{x(t)}}{dt} = A\vec{x(t)} + B \vec u(t) $ 

对方程左右两边同乘 $e^{-At}$

$$
\begin{aligned}
e^{-At}\frac{d\vec{x}(t)}{dt} &= Ae^{-At}\vec{x}(t) + Be^{-At} \vec u(t) \\
e^{-At}\frac{d\vec{x}(t)}{dt} -  Ae^{-At}\vec{x}(t)  &= Be^{-At} \vec u(t) \\
\frac{d[e^{-At}\vec{x}(t)]}{dt} &= Be^{-At} \vec u(t) \\

\end{aligned}
$$

然后对两边求积分，范围从 $t_0$ 到$t$（此时的 $t_0$ 和 $t$ 为常数，为了不和方程里的变量弄混，我们让方程里的 $t$ 变成 $\tau$）

$$
\begin{aligned}
\int_{t_0}^t \frac{d[e^{-A\tau}\vec{x}(\tau)]}{d\tau}d\tau &= \int_{t_0}^t Be^{-A\tau} \vec u(\tau)d\tau \\
e^{-At}\vec{x}(t) - e^{-At_0}\vec{x}(t_0)   &= \int_{t_0}^t Be^{-A\tau} \vec u(\tau)d\tau \\
\vec{x}(t) &= e^{A(t-t_0)}\vec{x}(t_0)  + e^{At}\int_{t_0}^t Be^{-A\tau} \vec u(\tau)d\tau \\
\vec{x}(t) &= e^{A(t-t_0)}\vec{x}(t_0)  + \int_{t_0}^t B e^{A(t-\tau)} \vec u(\tau)d\tau \\
\end{aligned}
$$

所以，状态空间方程的解为

$$
\boxed{
\vec{x}(t) = e^{A(t-t_0)}\vec{x}(t_0)  + \int_{t_0}^t B e^{A(t-\tau)} \vec u(\tau)d\tau \\
}
$$

其中

- $e^{A(t-t_0)}$ ：状态转移矩阵，表示系统状态 $x$ 由 $t_0$ 到 $t$ 的变化，也写做 $\Phi (t-t_0)$ 。
-  $A$ 矩阵的特征值决定状态转移矩阵随时间的变化，**$A$ 矩阵的特征值都小于0时，状态转移矩阵会越来越小。**（系统稳定性分析的重要结论）









