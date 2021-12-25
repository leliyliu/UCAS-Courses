# VLSI 测试与可测试性分析 

[toc]

## 第一章 VLSI 测试技术导论

### 良率和拒绝率

![image-20211209173847047](image-20211209173847047.png)

对于良率和拒绝率的计算方法，并且，在实际过程中，还可以用错误覆盖率来串联两者

![image-20211209173943493](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211209173943493.png)

### 故障模型

#### 可能的故障类型的计算： 

![image-20211209174125600](image-20211209174125600.png)在其中，还有一个重要的概念，也就是等价错误： 

等价错误： 对于所有的input patterns，不同的single fault 体现出现来的结果是相同的。

fault collapsing（取消错误的混淆）： 1. 消除等价错误，就可以定位到实际的错误 2. 减少错误的个数

#### Stuck-at Faults

也就是某一个或者多个位置卡在了0 或者 1 上，固定不变。 有两种不同的类型（SA0 和 SA1），可以根据此来生成真值表并进行处理

## 第二章 可测试性设计

### 可测试性设计技术

其中包括了两种方式，一种是基于拓扑的可测试性设计，另一种是基于仿真的可测试性设计。

首先的重点概念是： 可测试性的分析主要是计算可控制性和可观测性。其中 可控性反映了将信号线从初级输入端(primary input)设置为所需逻辑值的难度，而可观测性(observability)反映了将信号线的逻辑值传播到初级输出端(primary output) 的难度。 

#### 基于拓扑的可测试性设计

##### SCOAP

SCOAP 包括了两个重要概念： 

1. 可控制性： 反映了从输入开始，要设置一个值为固定值的难度
2. 可观测性： 反映了从逻辑值推到最终的输出结果的难度

因此需要计算这样六个内容： 

![image-20211209175758913](image-20211209175758913.png)

可控制性的值是从1到无穷，而可观测性的值是从0到无穷。注意S是针对于时序逻辑，而C 是针对于组合逻辑的。一般来说，会考的还是组合逻辑居多。

对于所有的输入，其CC0 和 CC1 都设置为1 ，而SC0 和SC1 都设置为0， 而对所有的输出，其CO 和 SO 值都设置为0 		

对于SCOPE 传播中的计算，有如下的规则 （记得打印规则），其中注意stem 的结构： 

![image-20211209181306270](image-20211209181306270.png)

![image-20211209181335768](image-20211209181335768.png)

注意例题中多路的问题 

对时序逻辑有一定的计算规则，规则比较复杂，这一部分的计算不是很清楚！**

###### levelization algorithms

![image-20211209183009476](image-20211209183009476.png)

可以利用此来进行计算，是比较重要的内容！！！ （也就是分级计算） 

##### 基于概率的可测试性分析

利用概率来进行相应的表示，主要是计算随机可测试性。 

![image-20211212095705147](image-20211212095705147.png)

其具体计算规则为： 

![image-20211212095748909](image-20211212095748909.png)

![image-20211212095828105](image-20211212095828105.png)

#### Test point insertion

这是提升DFT （可测性性设计） 中的ad hoc 方法中的一种。  

![image-20211214100849085](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211214100849085.png)

因此测试点插入就是一种经常使用的Ad hoc DFT 方法。可以用之前的方法来计算不同点的observationablity。 

![image-20211214101340391](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211214101340391.png)

当SE 为 0 的时候，（如OP2 中所示），那么这个low-observability 的值就会进入到D 触发器当中， 而当SE 为 1 的时候，那么就会进行移位操作，那么这些节点就会逐步被观测到。 

而对于低控制性的节点，其具体方式是类似的，只不过变成了TM 来进行信号的控制。如下图所示： 

![image-20211214102842541](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211214102842541.png)

#### Structure Approach

三种不同的模式： normal mode, shift mode 和 capture mode。 

一个scan 设计包括了两个部分： data input 和 scan input， 并且，在normal 和 capture mode 下， data input 被用来更新output， 而在shift mode 下， scan input 被用来更新output。 

##### Muxed-D SCAN Cell 

这个scan cell 包括了一个D 触发器和一个多路复用器

![image-20211212112917013](image-20211212112917013.png)

这个内容实际上使用了一个使能信号SE来选择data input 或者 scan input 。 SE 设置为0，则是normal 或者capture 模式。 SE 实际上是控制shift mode 和其余两个的划分，而TM 信号则是test mode 信号，是将normal mode 和其它两个模式分开。 

#### 扫描测试

对于扫描测试而言，主要有三种不同的测试方式，包括了full-scan，partial scan 和random-scan 

##### full-scan 扫描测试

![image-20211212115359978](image-20211212115359978.png)

所以实际上Mux-D full scan 也是能够很好被理解的，如下图所示： 

![image-20211212115913351](image-20211212115913351.png)

改为full-scan 的 测试结果，为： 

![image-20211212115949655](image-20211212115949655.png)

其中，不同的符号的不同概念为： 

![image-20211212120105401](image-20211212120105401.png)

其中关于扫描时间的计算为： 

![image-20211215144602313](upload\image-20211215144602313.png)

参考课本的61页

对于不同的mode，其TM 和 SE 的信号应该是： （实际上，SE 是用来控制 controlability 的， 而TM 是用来控制 observability 的） 

![image-20211212223525043](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211212223525043.png)

ATPG 自动测试图样生成 

### 扫描规则检验

一些重要的扫描设计规则如下： （为了实现扫描设计，所给出的扫描设计应该满足一系列的规则。)

![image-20211212224035642](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211212224035642.png)

#### Tri-State Buses

其原电路如下：

![image-20211221102141986](upload\image-20211221102141986.png)

根据描述，在这种三态电路中，两个bus 会造成不同的值，对于总线产生竞争。 

![image-20211212224227150](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211212224227150.png)

之后的modified circuit 为： 

![image-20211212224254375](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211212224254375.png)

#### Bi-Directional I/O Ports 

在移位操作期间，双向端口可能会造成冲突

![image-20211221104038687](upload\image-20211221104038687.png)

![image-20211221104048837](upload\image-20211221104048837.png)

加入相应的控制信号来保证对应的输入输出的控制

#### Gated Clocks 

时控门能够很好的减少功耗开销，但是其阻碍了一些触发器直接被primary inputs 控制 

![image-20211221111610279](upload\image-20211221111610279.png)

通过取消掉特定的门控逻辑，来实现相应的优化

![image-20211221113619276](upload\image-20211221113619276.png)

#### Conbinational Feedback Loops

组合电路的反馈循环， 由于在测试期间不能控制或确定存储在循环中的值，这可能会导致测试生成复杂性的增加或故障覆盖的损失。

![image-20211221164244096](upload\image-20211221164244096.png)

因此可以考虑如下的修改方式

![image-20211221182442522](upload\image-20211221182442522.png)

#### Asynchronous Set/Reset Signals 

异步set/reset 信号： 非直接由一次输入控制的扫描单元的异步设置/复位信号会阻止扫描链正确地移动数据。 

![image-20211221184446312](upload\image-20211221184446312.png)

因此需要对其进行修改，要保持其的inactivate 在shift operation 期间 

![image-20211221184626313](upload\image-20211221184626313.png)

#### Enhanced Scan

![image-20211212224608219](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211212224608219.png)

## 第三章 逻辑模拟

在逻辑符号中，一些重要的点包括了 0,1,u 和 Z, 其中，0和1就是简单的布尔值，而u 表示不知道（不知道是0还是1），而Z 表示一个高阻态。

### 逻辑模拟

#### truth table based gate evaluation

这种方式实际上是很简单的，也就是列出真值表，然后进行评估即可。 

（这里的input scanning 有点没太看懂） 

#### parallel gate evaluation 

利用计算机中内在的并发性来探索可能的并发操作。 

![image-20211212230802277](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211212230802277.png)

#### compiled code simulation 

这种模拟的思路，就是将逻辑网络转变为一系列机器指令，对于门函数和互连进行建模。 其基本的生成流如下： 

![image-20211213102808771](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213102808771.png)

#### event-driven simulation 

事件驱动的模拟，其中事件代表的是，信号值的改变。因此事件驱动的模拟器，监视了事件的发生，来决定哪些门需要进行评估。

上述两种方法的比较： 

![image-20211213110355363](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213110355363.png)

### 带时延的逻辑模拟

#### transport delay 

在信号通过门级电路时，会有一定的延迟，因此需要进行考虑，并且，对于rise 和 fall 可能有不同的延时，有时候也会有min-max delay，表示了一个区域。可以用如下进行表示： 

![image-20211213101254530](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213101254530.png)

#### Inertial Delay 

指的是输入脉冲变化需要持续的时间，在这种情况下，输出才会给出反馈。 注意这种延时一般用$d_l$来表示，而传输延时通常用$d_N$来表示。

![image-20211213101641678](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213101641678.png)

除此之外，还有线延迟，也就是传播延时（和传输延时不同，传输延时是由门电路引起的，而不是由线引起的） 

### 故障模拟

对于故障模拟的概念，应该为： 

当给定一个电路，一组测试图样和一个故障模型；决定了故障输出，不可检测的故障和故障覆盖率。

#### Serial Fault Simulation 

这种故障模拟方法是很简单的，也就是先执行无故障的逻辑模拟，在原始的电路上；然后对于每个故障，进行故障注入，并且进行逻辑模拟

![image-20211213123041259](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213123041259.png)

具体架构如上图，这种方法的优点是： 很容易实现，并且能够处理很多不同的故障模型，但是也很慢。 

##### Fault draopping 

为了减少不必要的仿真，可以停止对于一些已检测到的故障的模拟。例如（这样也可以减少模拟的时间）

![image-20211213143811550](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213143811550.png)

#### parallel fault simulation 

这个并行的思路实际上也就很简单，就是使用多bit 的数据来进行模拟，也就是利用bitwise 的 逻辑操作来并行模拟故障和无故障电路。 具体可以如下图所示

![image-20211213143619631](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213143619631.png)

这种方法的有点是： 当模拟序列开始的时候，每个模式都测试到了大量的故障（快）， 但缺点在于，只能应用于单元或者零延时的模型当中，并且除非所有的$w-1$个故障被检测出来，否则，不能drop 掉。 （这里有点没太看明白） 

#### parallel pattern fault simulation （PPSFP） 

也就是对于pattern 进行并行，但每次只针对于一个fault 来进行检测。 

![image-20211213144749327](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213144749327.png)

例子如上图所示。其优点是： 当故障被检测到之后，就会被抛弃，并且最适合那些fault dropping 率低的故障检测，但是不适合时序电路。 

## 第四章 测试生成

ATPG 自动测试向量生成

ATPG 的概念： 生成一组输入向量，使得其能够将无故障的电路和有故障的电路区分开。 一些典型的故障包括了： stuck-at fault， bridging fault， transition fault 和 path-delay fault。 

### Probablity of Fault Detection 

给定一个包含n 个输入的电路，假设$T_f$表示了能够检测故障$f$的向量集合，那么概率应该为$d_f = \frac{T_f}{2^n}$，进一步扩展有： 

![image-20211213151404818](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213151404818.png)

注意这里随机向量能够检测故障的概率。 

### 布尔差分

对于一个给定的电路而言，实际上一个输出可以表示成一个函数。假设无故障电路表示为$f$，而在某处有故障的电路表示为$f'$，那么应该有$f \ XOR \ f' = 1$，对于至少一个向量（测试向量）成立，也就是需要找到的向量（也就是测试生成的目标） 

对于差分的定义如下： 

![image-20211213152430182](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213152430182.png)

那么一个具体的求解例子如下： 

![image-20211213152757279](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213152757279.png)

也就是检测某个为SA0 或者 SA1 的时候，只需要设该为另一个，并利用布尔差分，使得最终的值为1，就可以求得测试向量。 

这里再加上一个对于中间节点的操作，也就是进行替换

![image-20211213153054889](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213153054889.png)

### 决定性的ATPG 

其中包含了两个主要的目标： 激励目标故障 和 传播相应的故障的效果到输出端。 

### 5-value algebra for Comb. Circuits 

之前我们使用的是四个值来进行表示，或者 使用两种不同的电路（无故障和有故障电路） 来解决ATPG 问题，这里考虑使用一个电路，将信号表示为： 

![image-20211213165853098](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213165853098.png)

其具体的布尔操作为： 

![image-20211213165958525](D:\leliy\github_project\UCAS-Courses\VLSI\reviews\image-20211213165958525.png)

### D 算法（D - Frontier 和 J-Frontier）

如果使用Naive ATPG 算法，时间复杂度是非常高的，需要过长的时间才能找到真正正确的input vector，因此考虑能否使用某种方式来减少整个的搜索空间。 这里需要简单了解一般的ATPG 方法，也就是直接从错误位置开始进行激励。 

D 算法能够解决任意的组合电路，其思路就是始终保持一个非空的D-frontier 并且试着传播至少一个故障影响到一个primary output 当中。 

其中： D-frontier 是门的输出都固定为x，并且有至少一个门的输入为D 或者D-bar  ，而J-frontier 是输出被给定，但是具体的输入的值，都没有给定（都是x）。

给出D-frontier 和 J-frontier 的具体实例： 

![image-20211215094902596](https://gitee.com/leliyliu/blog-image/raw/master/img%20/image-20211215094902596.png)

![image-20211215094938320](https://gitee.com/leliyliu/blog-image/raw/master/img%20/image-20211215094938320.png)

##### D算法的具体过程

![image-20211215095705682](https://gitee.com/leliyliu/blog-image/raw/master/img%20/image-20211215095705682.png)

![image-20211215095720224](upload\image-20211215095720224.png)

这里的D算法基本看明白了，但是还不太理解D-bar 和 0 之间的关系的内容。

### Static/Dynamic logic implications 

逻辑蕴含是指能够捕获在电路中分配逻辑值对于其他门的值的影响，能够帮助ATPG 进行更好的决策，并且避免冲突，来减少backtrack 的次数。 

静态逻辑蕴含，包含了： 直接蕴含，简介蕴含，以及Extended Backward 蕴含，一个实例如下，需要注意这里直接和间接的区别，直接的是能够单个信号直接影响到的，而间接的则是需要从多路来进行分析得到的。

![image-20211215104213254](upload\image-20211215104213254.png)

动态逻辑蕴含和静态逻辑蕴含是相似的，不同之处在于有一些信号已经被赋值了（这个已经赋值是指非需要探索的蕴含的赋值）。

![image-20211215104628571](https://gitee.com/leliyliu/blog-image/raw/master/img%20/image-20211215104628571.png)

### Untestable Fault(冗余故障-不可检测故障) 识别

冗余故障就是那些不能够被激励，或者不能够传播信号（或两者同时满足的），能够有效识别出这些故障，就可以避免使用ATPG 去寻找。 

![image-20211215105006037](https://gitee.com/leliyliu/blog-image/raw/master/img%20/image-20211215105006037.png)

利用上述描述，就可以得到FIRE 算法，其例子如下：

![image-20211215105624078](upload\image-20211215105624078.png)

![image-20211215105642428](upload\image-20211215105642428.png)

![image-20211215105655787](upload\image-20211215105655787.png)

![image-20211215105731211](upload\image-20211215105731211.png)

除此之外，还包括multi-line conflicts

![image-20211215105952230](upload\image-20211215105952230.png)

### Number of Paths in a Circuit 

计算逻辑通路数的方法是： 

构造通路图，对从source 到任一节点的通路数计数，用所有前驱节点的通路数之和得到当前节点的通路数，直到计算到sink 节点，得到总的物理通路数，而逻辑通路（通路时延故障）数是物理通路数的两倍。 

![image-20211220114352373](upload\image-20211220114352373.png)

## 第五章 逻辑自测试

BIST(built-in self-test) 自测试，由于传统的测试方法很贵，并且不具有很高的故障覆盖率。 整体的BIST 架构包括

![image-20211215194824170](upload\image-20211215194824170.png)

### X-bounding Methods 

X-bounding 方法是为了block 或者 fixed 电路中（BIST-ready 或者 CUT）的unknown 的值。 一些经典的模式如下图所示： 

![image-20211215195635109](upload\image-20211215195635109.png)

可以看到，有0-control， 1-control 以及选择一个PI 等操作。 

这种方法的问题在于：1. 提高了电路设计的面积 2. 影响了时序

### Standard LFSR & Modular LFSR 

LFSR(linear feedback shift register)，线性反馈移位寄存器。 

一个标准的LFSR 如下： 包含了n 个D触发器，和一组选定的异或门（XOR） 

![image-20211216101023728](upload\image-20211216101023728.png)

一个Modular LFSR（模块化）是指：每个异或门都放置在两个相邻的D触发器中间

![image-20211216101541768](upload\image-20211216101541768.png)

可以用函数来表示相应的LFSR 内容，如下图所示：

![image-20211216103156036](upload\image-20211216103156036.png)

$f(x) = 1 + h_1x + h_2x^2 + ... + x^n$

并且有，如果T 是一个能够数能够使得$f(x)$整除$1+x^T$,那么这个T 就被称为是LFSR 的周期。实际上这个周期就代表了LFSR 的长度内容

可以用$S_i(x)$来表示进行了在$i$次移位后的内容。

### Pseudo-Random Testing 

伪随机测试向量生成，减少了测试的时长但是牺牲了错误覆盖率，问题在于很难决定要求的测试长度和故障覆盖率。

所谓的maximum-length LFSR 就是指 上述的 T = $2^n-1$

#### weighted LFSR 

也就是对信号进行加权，这里给出一个实例如下： 

如何设置LFSR 的权重也是一个很重要的点 

![image-20211216204425603](upload\image-20211216204425603.png)

### Output Response Analysis 

在之前的学习部分，我们对于输出响应是将其与无故障电路进行异或（也就是进行不同电路输出信号之间的比较） ；而这里需要有效有一种输出响应分析技术，来将输出响应表述为一个特定的signature，并且进行比较。 

这里给出三种不同的输出响应比较技术： 

#### ones count testing 

假设CUT 有一个输出，并且这个输出包含了L - bits，整体的无故障的输出为：

![image-20211217093111893](upload\image-20211217093111893.png)

而ones count testing 需要一个计数器来计算bit流中的数目，而混叠概率(masking probability) 是：

![image-20211217093740338](upload\image-20211217093740338.png)

其电路结构为：

![image-20211217093840716](upload\image-20211217093840716.png)

#### transition count testing 

和ones count testing 是类似的，不过记录的是0-1 和 1-0 的转变的个数，其概率为：（还有一个需要假设的点，就是最开始中D触发器的值） 

![image-20211217095050957](upload\image-20211217095050957.png)

代表电路为： 

![image-20211217095106037](upload\image-20211217095106037.png)

#### signature analysis

这是最常用的分析技术，包括了serial 和 parallel 分析。 其中的循环冗余校对（cyclic redundancy checking (CRC) ）

##### serial  

![image-20211217101454698](upload\image-20211217101454698.png)

也就是顺序输入M ，然后根据r 的状态来进行比较。 

一个基本的example 如下：（SISR 是指 single-input signature register） 对应的混叠概率的计算

![image-20211217101519978](upload\image-20211217101519978.png)

##### parallel 

而对于并行内容，其结构如下：

![image-20211217102140874](upload\image-20211217102140874.png)

![image-20211217102250972](upload\image-20211217102250972.png)

### Logic BIST Architecture: STUMPS, BILBO 

整体而言，有四种不同的逻辑自测试架构：

+ no special structure to the CUT 
+ make use of scan chains in the CUT （利用扫描链）
+ configure the scan chains for test pattern generation and output response analysis  （测试向量生成和输出响应分析的扫描链） 
+ use concurrent checking circuitry of the design （并发电路检测） 

这里主要给出两种比较经典的： 

#### STUMPS (type - 2) 

self-testing using MISR and Parallel SRSG。这种架构包含了一个PRPG(并行的 SRSG) 和 一个MISR。扫描链将从PRPG中被并行加载， STUMPS 是一个现在都还在被使用的商用架构。 

架构表示为： 

![image-20211217105211874](upload\image-20211217105211874.png)

#### BILBO - type-3

Built-In Logic Block Observer 这种架构适用于可以将电路划分成一些独立模块的电路，每个模块都有自己的输入输出。

![image-20211217105428230](upload\image-20211217105428230.png)

## 第六章 测试压缩

需要压缩的原因在于： 测试数据量过大，测试时间过长以及芯片和测试通道的限制 ，而其整体的架构为： 

![image-20211217105720628](upload\image-20211217105720628.png)

### 测试激励压缩

首先要明确的是，当压缩x位时，可以不影响故障覆盖率（这个x 的求解等内容如何得到） ，这些X 为是可以不用设定的，比如下面的例子中： 

![image-20211217114916897](upload\image-20211217114916897.png)

#### 不同编码方式

##### 游程编码

游程编码方式：可以直接表述为，连续的多少个xxx ；一个具体例子如下： 

![image-20211217112830981](upload\image-20211217112830981.png)

但实际上游程编码不一定有效，不一定能压缩。这里的编码还有所不同，只需要标明所有的0 的个数（但这里用3位来表示0 中间的个数）  

![image-20211217115007107](upload\image-20211217115007107.png)

##### 字典编码

也就是通过查字典的方式来找对应的压缩测试

![image-20211217144952661](upload\image-20211217144952661.png)

##### 哈夫曼编码 

哈夫曼编码需要根据特定的频率来进行编码：也就是下图中的frequency 

![image-20211217145216040](upload\image-20211217145216040.png)

##### 选择性编码（线性） 

利用线性寄存器实现编解码操作，其基本架构为： 

![image-20211217150231515](upload\image-20211217150231515.png)

![image-20211217150243756](upload\image-20211217150243756.png)

#### 广播扫描设计： lllinois 扫描结构

传统的广播扫描设计，也就是直接强制ATPG 为广播扫描产生测试向量，这样显然会在一些测试上比较麻烦，毕竟不同的CUT 需要的测试向量不同，可能会无法检测到一些特定的故障。 

因此提出了lllinois 扫描结构， 包含了广播模式和串行扫描模式。 在广播模式中，一个扫描链被划分成多个子扫描链（分段），相同的向量被移位到了多个段中，然后通过一个MISR 来进行得到最终的响应数据。 而串行扫描模式，被用来那些所有的测试向量都能使用的场景。其缺陷是，在串行扫描阶段不会有压缩。  

![image-20211217151124753](upload\image-20211217151124753.png)

### 测试响应压缩

响应压缩和激励压缩是不同的，为了保证故障覆盖率，激励压缩应该是无损的，而相应是特征比较，则采用有损压缩，也可以保证故障覆盖率。

所以响应压缩本质上是有损压缩技术，可能会造成故障的混淆。 

整体的压缩技术包括：空间压缩技术，时间压缩技术以及时间和空间相结合的响应压缩技术。

#### 空间压缩技术

![image-20211217160018502](upload\image-20211217160018502.png)

整体的过程类似于一个矩阵乘的技术， 可保证2个错误位时无误判，保证任意奇数个错误位时无误判

#### 时间压缩

由时序电路构成，MISR  是一个典型的时间压缩电路

![image-20211217164911774](upload\image-20211217164911774.png)

#### 响应中的X 位

响应中有时候会存在 X位，而对其的处理包含了两种，分别是主动处理和容忍

![image-20211217171808253](upload\image-20211217171808253.png)

## 第七章 故障诊断

### Quality Metrics of Diagnosis 

#### success rate 

是指在物理故障分析中至少找到一个故障的比例。

#### diagnostic resolution 

工具报告的故障候选总数

#### first-hit index 

报告所有可能的排名列表， 更高的index 表示有更大可能是个故障

#### top-10 index 

多个故障， 前10个可能的故障

![image-20211218171429508](upload\image-20211218171429508.png)

### Combinational Logic Diagnosis 

在组合逻辑诊断中，我们假设故障你能够在组合逻辑中得到识别。 

#### Cause-Effect Analysis

 开始将故障的原因限定为特定的类型， 通过故障模拟来建立故障字典，然后使用查表操作来分析相应的故障效果，因此也就被叫做fault-dictionary based paradigm。 

![image-20211219092850781](upload\image-20211219092850781.png)

并且还可以进一步对问题内容进行简化的操作。（整合不同的输出内容来进行优化）

#### Effect-Cause Analysis 

这种方法是直接去检测出相应的故障，然后利用这些故障去推导可能出现故障的原因。

![image-20211219100407497](upload\image-20211219100407497.png)

可以看到，有一些耦合部分的内容。 然后可以进行一些结构化的剪枝，剪掉一些无关的部分

#### Chip-Level Strategy 

之前的方法都是block level ，并且主要解决一个故障的。 而chip-level 需要检测一个大的chip 的多个故障。 

![image-20211219100649547](upload\image-20211219100649547.png)

如上图所示，可以将故障分成独立的，和非独立的故障（IF 和 DF）

一种方法就是如上所示直接进行划分，可以通过将输出划分为组来进行。

另一种策略是两阶段的策略，通过识别出每个阶段独立的断层。第一个阶段，一个概念被称为prime candidate， 在不执行分区的情况下，每个独立的故障会被识别出来，在第二个阶段，这些造成的错误输出by prime candidates 会被首先消除，然后dependency-graph-based 的划分会变得更加有效。 

### Scan Chain Diagnosis 

扫描链中常有的故障类型包括： 

![image-20211219101551936](upload\image-20211219101551936.png)

![image-20211219102108424](upload\image-20211219102108424.png)

## 第八章 内存测试

这一章节主要是说内存测试与自测试，包括内存故障模型和测试算法，内存故障仿真和测试算法生成。

### Memory fault models 

典型的故障模型有： 

![image-20211217173520713](upload\image-20211217173520713.png)

根据书中的描述，主要是六种： SAF(stuck-at fault), SOF(stuck-open fault), TF(transition fault), DRF(data retention fault), CF(coupling faults), RDF(read distrub fault)，还有一个是AF (address-decoder fault)

![image-20211221090243879](upload\image-20211221090243879.png)

![image-20211221090300129](upload\image-20211221090300129.png)

![image-20211221091841520](upload\image-20211221091841520.png)

### Memory test algorithms 

这里的测试算法主要是 march test algorithm ；实际上可以将一个测试算法看成是一个有限序列的测试元素。 

一个march test包含了有限序列的march 元素，每个元素是一个有限序列的操作，被用到每个内存的每个cell 当中，操作包括r0,r1,w0,w1。并且每个march 元素可以用两种不同的address orders 来表示， ascending order 和 decending order. 因此一种表示方法就是：

![image-20211217212233845](upload\image-20211217212233845.png)

![image-20211217212438748](upload\image-20211217212438748.png)

![image-20211217212447560](upload\image-20211217212447560.png)

上述是一些经典的方式，用来检测出不同的错误。 

不同测试的故障覆盖率如下： 

![image-20211217213426325](upload\image-20211217213426325.png)

对于不同的覆盖率的计算，有一些定理： 

![image-20211221095347174](upload\image-20211221095347174.png)

也就是包含了$\Uparrow (rx, ..., wx') 和 \Downarrow (rx', ..., wx)$， 那么就能完全检测出AF 故障。 

### Testing Word-Oriented RAM 

将故障分为两类： single cell fault 和 faults involving two cells （也就是coupling faults），第二类的故障基于写操作的强度和coupling effect。

对于word-oriented 的RAM 的测试，需要设置logm+1 个标准background 来进行测试，来保证故障覆盖率。

### Typical RAM BIST Architecture 

![image-20211217213535277](upload\image-20211217213535277.png)

典型的RAM BIST 架构如上所示，也就是有相应的控制器，以及测试向量的生成和 最终的比较。

## 第九章 内存诊断

![image-20211218094641160](https://gitee.com/leliyliu/blog-image/raw/master/img%20/image-20211218094641160.png)

### Typical RAM BISR 架构

![image-20211217215127487](upload\image-20211217215127487.png)

整体的架构中包含了BIST， 冗余分析，可配置机制和额外的元素来进行可配置性补充。

其中的冗余结构包含了global 或 local 的 spare elements。 

### BIRA(built-in redundancy analysis)

在检测到对应的错误之后，需要对故障进行修复，一种主要的方式就是冗余。包括了online (ECC 汉明码扩展) 和 offline(spare rows, columns, blocks) 

关于一些内容的定义： 

faulty line 也就是对于在一个faulty cell 中至少有一行或一列。而一个不与其他cell 共享行和列的cell 被称为orthogonal faulty cell 。 

![image-20211218095703978](upload\image-20211218095703978.png)

因此一个不可挽回的条件（不可修复的条件） ： $F' > r+c$

RM 算法（repair-most）： 对于每个faulty line (错误个数为k) ， 当满足k>r 或者 k>c时，就是must-repair 的faulty line。 

#### Essential Spare Pivoting (ESP)

为了不需要利用一个bitmap 来保持高修复率（存储一个bitmap 开销大） ，ESP 算法的目标是有效并行分配冗余。 保持area overhead low 并且repair efficiency high。 

其思路就是任意一个故障行或者列中faulty cell 大于等于阈值，则修复。 也就是对每个故障行列 用一个计数器进行计数。 

拥有r+c 个寄存器，最开始都是空的。 当有row-address 或者 column-address match 的时候，就标注为pivot，然后会根据threshold 来进行冗余单元的安排： 

![image-20211218104352718](upload\image-20211218104352718.png)

### Repair rate 

一个高的repair rate 意味着一个高的良品率（在repair 之后） 在几乎相同的area overhead 当中。 

![image-20211218104657654](upload\image-20211218104657654.png)

可以看到，ESP 是一个不错的算法，和optimal 能达到近似的高。 

具体的repair rate 的定义为： 内存修复的数量与缺陷数量之间的比例。

## 第十章 边界扫描与SOC测试

### 1499.1 Boundary-Scan Architecture 

1499.1 标准 边界扫描实际上是一系列旨在解决广泛测试问题的测试方法:从芯片级到系统级，从逻辑核心到核心间的互连，从数字电路到模拟或混合模式电路，从普通数字设计到高速设计。

标准1149.1为数字集成电路和混合模拟/数字集成电路的数字部分定义了测试访问协议和边界扫描架构。如下图所示， 边界扫描是由于在原电路的每个I/O引脚上插入一个边界扫描单元，并将这些单元连接到一个称为边界扫描寄存器的移位寄存器中。 

![image-20211219103947279](upload\image-20211219103947279.png)

整体的边界扫描的结构为： 

![image-20211219104949653](upload\image-20211219104949653.png)

整体的架构包括了一个test access port （TAP） 控制器，一个TAP 单元，以及一个指令寄存器和多个测试数据寄存器。 

![image-20211219105301523](upload\image-20211219105301523.png)

### 1149.1 Instruction Set: EXTEST, BYPASS, SAMPLE, PRELOAD...

一些指令集包括了

![image-20211219105419408](upload\image-20211219105419408.png)

### A System Overview of IEEE 1500 Standard 

1500 是一个 embedded core test 标准（嵌入核标准） 

整体的架构如下所示： 

![image-20211219110013589](upload\image-20211219110013589.png)

### Comparison between 1499.1 and 1500 

两个标准之间的比较

![image-20211219103157259](upload\image-20211219103157259.png)

### IJTAG (IEEE 1687)

![image-20211219105934055](upload\image-20211219105934055.png)

## 第十一章 纳米电路测试技术

随着集成电路技术的发展，对于电路的测试变得更加困难了。

### Delay Testing 

 对于此，有两种主要的故障模型： path-delay 和 gate-delay faults

path-delay faults 表示 路径的传播延时超过了时钟间隔，而gate-delay 表示门级电路所带来的延时。 

对于不同路径的分类，可以包括：

![image-20211219161733625](upload\image-20211219161733625.png)

#### A cost-effective test strategy 

使用功能性的向量，功能向量能够快速应用并且找到一些延迟的缺陷，并且能够评估transition 故障覆盖率。并对未检测到的转换故障应用测试，然后对于long-path delay 故障进行测试。

![image-20211219162923902](upload\image-20211219162923902.png)

#### Variability of Path Delay: noise, process, thermal, power

![image-20211219163031100](upload\image-20211219163031100.png)

### Signal Integrity（信号完整性）

信号完整性测试既是一种设计问题，也是一个测试问题，如何有效保证信号的完整性？

#### Integrity Loss Model

excessive delay 表示性能降低，导致功能问题；ringing 导致功能问题； 而overshoot 有助于噪声，延迟，热载流子，时间依赖性的介电击穿和电迁移。 

#### Maximum Aggressor(MA) model 

这个模型假设在受害线路上传输的信号可能会受到附近其他线路(攻击者)的信号或转换的影响。传统的MA模型只考虑耦合电容

### FPGA Testing 

FPGA 就是有可编程的logic blocks( PLBs)，以及对应的routing network 和 I/O cells。 

对于PLB 板子的 BIST （自测试） 

![image-20211219164342303](upload\image-20211219164342303.png)

根据这样一种结构进行测试即可。