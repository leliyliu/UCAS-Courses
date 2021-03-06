# 量子信息与量子密码 

[toc]

## 量子力学基础

### 线性代数基础

酉矩阵是 复数形式下的正交矩阵，而厄米阵是 复数形式下的对称（共轭转置）矩阵，对于这种形式，存在奇异值分解，并有奇异值的定义。 

- [ ] 奇异值分解 和 极式分解
- [ ] 直积的定义 （最需要注意 转置 和 求逆过程 与传统矩阵乘法的不同） 
- [ ] 酉变换和酉矩阵
- [ ] 正规算子 与 谱分解 定理 
- [ ] 同时酉对角化
- [ ] Gram-Schmidt 正交化 
- [ ] 矩阵的外积表示
- [ ] 算子函数

### 量子力学基础

#### 基本假设

1. 波函数假设
2. 算符假设 
3. 测量假设
4. 态演化假设
5. 全同性假设

![image-20220321181410520](image-20220321181410520.png)

![image-20220321182042467](image-20220321182042467.png)

![image-20220321182053251](image-20220321182053251.png)

![image-20220321182812540](image-20220321182812540.png)

![image-20220321182851974](image-20220321182851974.png)

#### 基本概念

![image-20220321184224468](image-20220321184224468.png)

![image-20220321184246154](image-20220321184246154.png)

测不准原理（不确定性原理）

![image-20220321185051666](image-20220321185051666.png)

#### 量子测量

![image-20220321192019589](image-20220321192019589.png)

测量算子的完备性原则

![image-20220321195807466](image-20220321195807466.png)

![image-20220322102631603](image-20220322102631603.png)

#### 密度算符

密度算子的定义：（对于纯态系综）

![image-20220322102726665](image-20220322102726665.png)

系统完全由密度算子描述， 密度算子为作用在态空间上的半正定算子。 而量子力学的第二个基本假设表明一个闭的量子系统的演化是由一个酉算子 U 来刻画。

![image-20220322105237801](image-20220322105237801.png)

![image-20220322112039941](image-20220322112039941.png)

![image-20220322112220833](image-20220322112220833.png)

![image-20220322112711770](image-20220322112711770.png)

![image-20220322113152952](image-20220322113152952.png)

#### 复合体系

![image-20220321194740220](image-20220321194740220.png)

![image-20220322113611465](image-20220322113611465.png)

![image-20220322181220232](image-20220322181220232.png)

![image-20220322183221382](image-20220322183221382.png)

#### Bell 定理 （不等式）

![image-20220321204048442](image-20220321204048442.png)

## 量子信息论与早期量子算法

### 量子信息论简介

![image-20220328184049911](image-20220328184049911.png)

![image-20220328184507439](image-20220328184507439.png)

![image-20220328184758667](image-20220328184758667.png)

### 量子通信

![image-20220328185937874](image-20220328185937874.png)

bell 态： 四个纠缠态

![image-20220328192213666](image-20220328192213666.png)

![image-20220328192229431](image-20220328192229431.png)

![image-20220328192239104](image-20220328192239104.png)

### 量子逻辑门

![image-20220328193413998](image-20220328193413998.png)

而可逆逻辑门，是指可逆的，通过输出可以推测输入

![image-20220328193547396](image-20220328193547396.png)

![image-20220328193724842](image-20220328193724842.png)

![image-20220328193903115](image-20220328193903115.png)

![image-20220328195059852](image-20220328195059852.png)

![image-20220328201105054](image-20220328201105054.png)

### 简单量子算法

查看PPT 



### 量子密码协议



## 量子计算模型

### 量子逻辑线路

#### 经典逻辑门和可逆逻辑门

有一些基本的逻辑门，而在量子中，也存在一定的基本逻辑门： 

![image-20220402182437903](image-20220402182437903.png)

最经典的就是受控非门（CNOT）

![image-20220402182526630](image-20220402182526630.png)

![image-20220402182826024](image-20220402182826024.png)

而对于单 qubit 操作而言，主要有X,Y,Z和 H 门等

![image-20220402183116009](image-20220402183116009.png)

![image-20220402183123537](image-20220402183123537.png)

那么，关于x,y,z轴旋转算子分别定义如下：

![image-20220402183200416](image-20220402183200416.png)

那么任意一个单量子比特的酉变换，都可以分解为： 

![image-20220402184202903](image-20220402184202903.png)

![image-20220402184552354](image-20220402184552354.png)

#### 受控运算

![image-20220402194004684](image-20220402194004684.png)

![image-20220402194142393](image-20220402194142393.png)

#### 量子线路的测量问题

隐含测量问题： 

![image-20220402202029294](image-20220402202029294.png)

![image-20220402202742346](image-20220402202742346.png)

纠缠态（贝尔态）的制备

![image-20220402202101123](image-20220402202101123.png)

##### 通用运算的有效离散集合

![image-20220402203618253](image-20220402203618253.png)

**两级酉门**

![image-20220402205212829](image-20220402205212829.png)

## 纠错码与容错量子计算

### 编码理论基本概念

#### 编译码概念

编码过程是 m 位二进制数 到 n 位 二进制数的转化

![image-20220411183742528](upload/image-20220411183742528.png)

![image-20220411184031425](upload/image-20220411184031425.png)



![image-20220411183954001](upload/image-20220411183954001.png)

![image-20220411184006085](upload/image-20220411184006085.png)

标准的生成矩阵

![image-20220411184348247](upload/image-20220411184348247.png)

通过编码可以有效实现纠错内容

其具体纠错过程是：通过生成矩阵G ，可以得到校验矩阵H， 其满足如下表达式： 

$HW^T = 0$, 其中 $W = AG$, 那么如果存在出错，即： $HR^T \neq 0$，那么R 就不是码字，故假设有： $R = W + E$ ，所以： 

$HR^T = HE^T$，根据设定，可以取得E ，那么就可以求得 $W$.

#### hamming 码

从校验矩阵来构造hamming 码，可以得到hamming 码

![image-20220411190536890](upload/image-20220411190536890.png)

hamming 码是一个完全码： 

![image-20220411190610989](upload/image-20220411190610989.png)

### 量子纠错码

量子码所面临的问题在于： 错误类型不同，除了比特反转之外，还有相位反转。 并且纠错过程不能直接对数据态进行测量。 

![image-20220411194312529](upload/image-20220411194312529.png)

![image-20220411194259149](upload/image-20220411194259149.png)

通过特定的有效编码来实现其具体的检测过程。

![image-20220411194606603](upload/image-20220411194606603.png)



第二种思路是直接用量子电路修正错误，不需要判定其原来结果： 

![image-20220411194730354](upload/image-20220411194730354.png)

上面两个系统而言，其具体而言，是解决了所给出的第二个问题，而第一个问题是纠正相位错误，其解决方式如下： 

实际上相位反转是共轭基上的比特反转，所以其解决方式是较为简单的，实际上是将相位错误变为比特错误，然后使用上面的比特错误解决方式来解决相位反转的错误。

![image-20220411195229359](upload/image-20220411195229359.png)

#### Shor 码

![image-20220411195309596](upload/image-20220411195309596.png)

其编码方式就是通过给定编码的扩展，其具体编码电路如下：

![image-20220411195419401](upload/image-20220411195419401.png)

可以看到，实际上使用了9个量子位来实现一个量子位的纠错。 

#### CSS 量子纠错码

![image-20220411200038702](upload/image-20220411200038702.png)

![image-20220411200529925](upload/image-20220411200529925.png)

可以看到，通过求和的结果，可以描述出 $y$ 的内容。

具体的 CSS 码的纠错过程如下：

![image-20220411202039424](upload/image-20220411202039424.png)

![image-20220411202313246](upload/image-20220411202313246.png)

得到最终的一个CSS 码 纠错实例为： 

![image-20220411203132809](upload/image-20220411203132809.png)

其得到的结果为：

![image-20220411203437674](upload/image-20220411203437674.png)

![image-20220411203445829](upload/image-20220411203445829.png)

通过 物理位 上的 逐位变换 变成了 逻辑位 上的阿达玛 变换。 

#### steane 就是上述 CSS 编码的具体实例

![image-20220411203821036](upload/image-20220411203821036.png)



## 量子算法

### Shor 算法

#### 量子Fourier变换 (QFT)

对标经典离散Fourier 变换，在量子清醒下也可以得到具体的定义： 

![image-20220418181125690](upload/image-20220418181125690.png)

![image-20220418181329233](upload/image-20220418181329233.png)

因为整体的量子状态，可以分解为多个量子状态之和。上面的内容将量子和经典结合起来

要探究两个内容，第一个是说明QFT 的酉性： 

![image-20220418183819618](upload/image-20220418183819618.png)

![image-20220418184217287](upload/image-20220418184217287.png)

通过这一表述，可以说明，实际上就是一个对N个内容的操作，所以得到最终的电路为：

![image-20220418184249255](upload/image-20220418184249255.png)

![image-20220418184418161](upload/image-20220418184418161.png)

#### 相位估计

这是量子傅里叶变换的一个应用， 实现相位的估计。 

![image-20220418185051264](upload/image-20220418185051264.png)

具体第一阶段的运行图，按照讲义所示，并说明有：

![image-20220418185416551](upload/image-20220418185416551.png)

![image-20220418185729318](upload/image-20220418185729318.png)

整体的估计精度应该表述为：

![image-20220418190436289](upload/image-20220418190436289.png)

整体而言，有：

![image-20220418190551279](upload/image-20220418190551279.png)

#### 离散对数量子算法举例

经典秘钥的操作：

![image-20220418192959260](upload/image-20220418192959260.png)

实际上，这个协议毫无安全性可言。 

对于离散对数问题，有：

![image-20220418193634493](upload/image-20220418193634493.png)

![image-20220418193915077](upload/image-20220418193915077.png)



#### 求阶

求阶需要求的内容：

![image-20220418195636281](upload/image-20220418195636281.png)

利用(1)(2)(3)式，容易证明上面的内容，那么具体求阶计算过程为：

![image-20220418200258740](upload/image-20220418200258740.png)



#### 因子分解

因子分解的具体问题为：

![image-20220418192410472](upload/image-20220418192410472.png)

其具体的例子为：

![image-20220418200825269](upload/image-20220418200825269.png)

### Grover 量子搜索算法

无序数的快速搜索算法

#### $U_a$ 变换

![image-20220418203146794](upload/image-20220418203146794.png)

![image-20220418203434965](upload/image-20220418203434965.png)

![image-20220418203503927](upload/image-20220418203503927.png)

#### $U_s$变换

![image-20220418203630868](upload/image-20220418203630868.png)

#### Grover 迭代

![image-20220418203653289](upload/image-20220418203653289.png)



#### 从N 中到1 问题

迭代 多次使得最终的结果不断接近于以概率1 得到黑盒的 a 

#### 多搜索目标问题

#### 关于“量子摇晃”
