<div class="cover" style="page-break-after:always;font-family:方正公文仿宋;width:100%;height:100%;border:none;margin: 0 auto;text-align:center;">    <div style="width:60%;margin: 0 auto;height:0;padding-bottom:10%;">        </br>        <img src="upload/ucas-logo.png" alt="校名" style="width:100%;"/>    </div>    </br></br></br></br></br>    <div style="width:60%;margin: 0 auto;height:0;padding-bottom:40%;">        <img src="upload/ict-logo.jpg" alt="校徽" style="width:100%;"/>    </div>    </br></br></br></br></br></br></br></br>    <span style="font-family:华文黑体Bold;text-align:center;font-size:20pt;margin: 10pt auto;line-height:30pt;">《高级计算机体系结构 课程实验报告》</span>    </br>    </br>    <table style="border:none;text-align:center;width:72%;font-family:仿宋;font-size:14px; margin: 0 auto;">    <tbody style="font-family:方正公文仿宋;font-size:12pt;">       <tr style="font-weight:normal;">             <td style="width:20%;text-align:right;">授课教师</td>            <td style="width:2%">：</td>             <td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">沈海华 </td>     </tr>        <tr style="font-weight:normal;">             <td style="width:20%;text-align:right;">姓　　名</td>            <td style="width:2%">：</td>             <td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> 刘炼</td>     </tr>        <tr style="font-weight:normal;">             <td style="width:20%;text-align:right;">学　　号</td>            <td style="width:2%">：</td>             <td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> 202128013229021 </td>     </tr>        <tr style="font-weight:normal;">                  <tr style="font-weight:normal;">             <td style="width:20%;text-align:right;">日　　期</td>            <td style="width:2%">：</td>             <td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">完成日期</td>     </tr>    </tbody>                  </table></div>



#  高级计算机系统结构 课程实验报告

<center><div style='height:2mm;'></div><div style="font-family:华文楷体;font-size:14pt;">刘炼，202128013229021 </div></center>
<center><span style="font-family:华文楷体;font-size:9pt;line-height:9mm">中国科学院大学 计算机学院  </span>
</center>
## Build iFlow & Run Example 

```bash 
git clone https://github.com/PCNL-EDA/iFlow.git   
cd iFlow
./build_iflow.sh  # 在 build_iflow 中，存在很多 sudo 权限的内容，实际上应该删去改内容

```

> 整个项目目录如下所示： 
>
> ![image-20220411225846196](upload/image-20220411225846196.png)
>
> 

### 顶层与配置脚本

#### run_flow.py 

运行`./run_flow.py -h ` ，可以得到如下的说明：

![image-20220411230539846](upload/image-20220411230539846.png)

可以看到，通过选择不同的参数，可以设置不同的RTL 设计 （-d design) , 后端设计的不同步骤 （-s step) 等内容。 

#### configuration

在`iFlow/scripts/cfg` 文件夹中，包含了四个脚本文件： `data_def.py`, `flow_cfg.py`, `foundry_cfg.py` 和 `tools_cfg.py`，分别用来控制数据的定义， 流程配置，工艺库配置以及工具版本的配置。 

![image-20220411232837012](upload/image-20220411232837012.png)

在`data_def.py`中，如上图所示，蓝框标识了后端的不同步骤，并且设置了每个步骤所使用的工具，可以更改这些工具内容。而在`flow_cfg.py`中，设置了默认的参数，因此可以不用设置工艺相关的参数而直接运行命令，同样能够得到结果。

例如运行命令：

```bash 
./run_flow.py -d aes_cipher_top -s synth
```

实际上对aes_cipher_top 设置了默认的参数为： `sky130`, `HS`  和 `TYP`。 

而对于文件`floundry_cfg.py`，其中定义了不同工艺节点的库文件路径，如果要加入新的工艺，则需要将其添加到这个文件中，截取<font color=red>sky130</font>的工艺库路径的部分展示如下： 

![image-20220413153959584](upload\image-20220413153959584.png)

而文件`tools_cfg.py`用于配置每一步要用哪种开源EDA 工具及其对应的版本号。 

### iFlow 流程介绍

#### 综合

综合的目的是将RTL代码转化为网表，在对应的`.tcl`文件中，需要配置相应的参数来实现，需要配置的内容包括：

+ 综合需要读入的库文件，例如blackbox 的 verilog 文件 和 map 文件
+ 特定的cell，包括tie cell 和 buffer 
+ 综合所需要的RTL 代码路径

在配置好相应的内容之后，运行单步综合命令如下：

```bash
./run_flow.py -d gcd -s synth 
```

可以看到，在`report`文件夹下得到了`gcd`综合相关的文件夹，其中包含了`synth_check.txt` 和 `synth_stat.txt` 文件

![image-20220413155623594](upload\image-20220413155623594.png)

#### 布局

在iFlow中，布局包括了六个小步骤，分别是`flloorplan`, `tapcell`,`PDN`,`gplace`,`resize`和 `dplace`。 

##### floorplan 

根据gcd中`floorplan`的脚本，配置其中的“DIE_AREA" 和 "CORE_AREA"参数，具体如下图所示：

![image-20220413161544560](upload\image-20220413161544560.png)

配置的track 对应参数为：

![image-20220413161755378](upload\image-20220413161755378.png)

最终执行单步`floorplan`的命令如下：

```bash 
./run_flow.py -d gcd -s floorplan -p synth
```

得到 其 check 如下：

![image-20220413162803964](upload\image-20220413162803964.png)

##### tapcell

在 floorplan 初始化之后，需要在 core area 范围内插入 tapcell，tapcell 的作用是为所有标准单元的 N 阱和衬底提供偏置电源，在 core area 范围内每间隔一段距离则需要摆放一个 tapcell，在 tapcell 这一步还需要插入 endcap，主要是为了插在边界处或 sram 及 ip 周围消除不对称性。其基本配置可以参考配置文件： 

![image-20220413162959961](upload\image-20220413162959961.png)

执行对应的`tapcell`命令如下：

```bash 
./run_flow.py -d gcd -s tapcell -p floorplan
```

得到了最终的tapcell 结果

##### PDN

在布局中，除了面积规划及标准单元的摆放之外，还有相当重要的一步为power plan，又称为 PDN，这一步主要是构建为整个芯片供电的电源网络，一个芯片的电源网络质量直接影响整个芯片的性能。其脚本是比较简单的，具体为：

```bash
pdngen $PDN_CFG_FILE --verbose
```

执行对应的`PDN`命令如下：

```bash 
./run_flow.py -d gcd -s pdn -p tapcell
```

其具体对应的配置实例如下图所示： 

![image-20220413164001174](upload\image-20220413164001174.png)

##### gplace

在完成电源网络的构建后，接下来需要将标准单元摆放到 core area 范围中，这一步即为 gplace，又称为 global place。在gplace阶段，需要配置线RC参数的抽取层以评估延时，而另一个参数用于设置摆放标准单元时的密度。 具体的运行gplace的命令如下图所示： 

![image-20220413164238667](upload\image-20220413164238667.png)

其中默认overflow 为 0.1 ，执行单步`gplace`命令为：

```bash 
./run_flow.py -d gcd -s gplace -p pdn
```

可以观察到其最终的overflow 会小于0.1 ,迭代超过了 360 轮

![image-20220413164349233](upload\image-20220413164349233.png)

##### resize

resize 这一步骤主要是在 dplace 前，进行一部分标准单元的更换及插入，其中包括将逻辑 0 和逻辑 1 的驱动端加上 Tie cell 和在需要 fix fanout 的驱动端加上buffer。这一步骤需要配置的参数如下图所示： 

![image-20220413164520277](upload\image-20220413164520277.png)

包括了最大扇出和固定的tie cell 和 buffer 类型。在这一流程中，主要进行fanout 的 修复，降低fanout 以增加各级的驱动能力。执行单步`resize`命令如下：

```bash 
./run_flow.py -d gcd -s resize -p gplace
```

会在report 中保存 resize 前后的差别

![image-20220413164822699](upload\image-20220413164822699.png)

##### dplance

dplace 是布局中的最后一步，主要是对gplace阶段已经摆放的标准单元进行合法化，消除标准单元之间的重叠，将标准单元对齐到core area 范围的Row 上，从而确保电源网络能为标准单元供电。

执行单步`dplace`命令如下：

```bash 
./run_flow.py -d gcd -s dplace -p resize
```

可以得到最终的布局阶段的分析：

![image-20220413165034545](upload\image-20220413165034545.png)

#### CTS

CTS 的全称为 Clock Tree Synthesis，时钟树综合，这是后端物理设计的一个关键步骤，EDA 工具会根据时序约束文件，创建真实的时钟，并构建时钟树，目的是通过插入 buffer 或 inverter 的方法使得同一时钟域到各个寄存器时钟端的延迟尽可能保持一致，即时钟 skew 尽可能小。

首先需要设置用于构建时钟树的buffer 的 cell 类型，其在配置文件中表示为：

![image-20220413165318525](upload\image-20220413165318525.png)

执行单步`CTS`命令如下：

```bash 
./run_flow.py -d gcd -s cts -p dplace
```

得到其分析为：

![image-20220413170008404](upload\image-20220413170008404.png)

可以看到，与 CTS 步骤之前相比，整体的分析有了很大的不同。

#### filler

在构建时钟树，并完成 timing 的修复之后，所有的标准单元已经确认并固定，后续的操作不会改变网表，这时，我们需要在整个 core area 范围内填满 fillercell，主要作用是为了填充标准单元之间的空隙，将整个扩散层连接起来，以满足 DRC（Design Rule Check）要求，以构成 power rail，使电源和地线保持连接。需要设置filler cell 的类型，具体如图所示： 

![image-20220413170237421](upload\image-20220413170237421.png)

执行单步`filler`命令如下：

```bash 
./run_flow.py -d gcd -s filler -p cts
```

生成得到了.def 文件。 

#### 布线

在iFlow 中，布线一共分为两步流程，分别是 groute 和 droute，groute 生成一个引导布线文件 guide，droute 读入 guide 完成实际的布线。

##### groute

groute 又称为 global route，这一步骤会做好布线资源分配，生成布线引导文件“route.guide”。groute 主要设置的参数为各金属层在库里面的对应名字，用于确定布线所用层。 

在开始groute前，如果有用到SRAM 等marco，需要给marco 加上routing package，具体如下所示（由于这里使用的是gcd，暂时用不上，所以注释掉，在后续内容中，可能会使用到routing package）：

![image-20220413171034960](upload\image-20220413171034960.png)

执行单步`groute`命令如下：

```bash 
./run_flow.py -d gcd -s groute -p filler
```

可以生成相应的.guide 文件

##### droute

droute 流程是将 groute 输出的 route.guide 文件读入，并根据 guide 文件的描述去形成实际布线的过程，又称为 detail place。其主要是依赖于生成的route.guide 文件，没有额外的参数需要设置：

![image-20220413171442879](upload\image-20220413171442879.png)

执行单步`droute`命令如下：

```bash
./run_flow.py -d gcd -s droute -p groute
```

#### 版图

droute 完成后输出的是 def 文件，而不是 gds 文件，需要得到用于 foundry生产的 gds 文件还需要一个 merge 的流程，在 iFlow 中，这一流程命名为“layout”。其中的layout 是将所得到的def 文件和标准单元中的黑盒进行合并，得到最终的gds 文件。 

merge 过程的具体命令在顶层脚本“run_flow.py”中实现，如图 29 所示，merge 需要读入的文件包括 droute 输出的 def，还有标准单元、IO cell、marco 的gds 文件，以及工艺的 layer map 文件 klayout.lyt 和 klayout.lyp，最终输出 gds 版图。

![image-20220413172354558](upload\image-20220413172354558.png)

执行单步`layout  (merge)`命令如下：

```bash
./run_flow.py -d gcd -s layout -p droute
```

使用klayout 工具，查看gds 版图如下（所有中间生成结果和最终的gds文件均在 result 文件夹下。

![image-20220413173110625](upload\image-20220413173110625.png)

## 更换设计

在前面的执行示例中，我们使用了gcd 来作为基本设计单元，其实际上是一个非常小的设计，只有百门级别的芯片。 下面将介绍几个别的设计，进行更换。 

### uart 设计



#### 拷贝rtl 代码并修改flow 定义

首先需要将uart 的 rtl 拷贝到 `iFlow/rtl`中，而后需要修改默认flow 参数，这里的默认foundry 为 "asap7"，可以修改为"sky130"，具体如图所示：

#### 设定rtl 代码脚本

首先将 gcd 设计脚本作为uart设计的脚本，并修改相应的参数，具体而言，首先修改综合脚本，将输入的verilog 代码改为 uart 设计的rtl 代码，如下图所示：

![image-20220413183050905](upload\image-20220413183050905.png)

这里由于uart 设计的规模和gcd 设计非常接近，在使用sky130 工艺的情况下，我们可以沿用gcd 设计的floorplan 设置，也可以适当调节为如下：

![image-20220413183112937](upload\image-20220413183112937.png)

最后执行`uart`的命令：

```bash
./run_flow.py -d uart -s \ synth,floorplan,tapcell,pdn,gplace,resize,dplace,cts,filler,groute,droute,layout -f sky130 -t HS -c TYP -v V1 -l V1
```

得到最终的版图为： 

![image-20220413183652665](upload\image-20220413183652665.png)

### aes_cipher_top 设计

aes_cipher_top 是一个加密算法的小模块，相对于前面两个设计，aes_cipher_top 的规模要大很多，是一个万门级的设计。与 uart 设计一样，首先要修改综合脚本中的 Verilog 代码路径，然后调整 floorplan，增大芯片的面积，其面积设置为： 

![image-20220413183802564](upload\image-20220413183802564.png)

这里的操作是与之前uart 中的执行相同的，而后运行相应的命令生成`aes_cipher_top`的版图：

![image-20220413193907416](upload\image-20220413193907416.png)

```bash

```

### picorv32 设计更换

picorv32 是一个实现 RISC-V RV32IMC 指令集的 CPU 内核，其代码源地址为：https://github.com/YosysHQ/picorv32 ，下面将展示如何

#### 下载rtl 代码 & 增加flow 

```bash 
git clone git@github.com:YosysHQ/picorv32.git # 拷贝数据到 rtl 文件夹下
#除了拷贝rtl 源代码之外，还需要加上.sdc 文件，否则会报错！！！
#拷贝.sdc 文件
cp -r aes_cipher_top/aes_cipher_top.sdc picorv32/
mv aes_cipher_top.sdc picorv32.sdc
```

查看`picorv32`的rtl 代码可知，其rtl 实现CPU 的代码为 `picrov32.v`文件，因此，需要在后续综合脚本中导入该文件。 在cfg 中的`flow_cfg.py`文件中，添加对应的flow 为： 

```python
picorv32 = Flow('picorv32', 'sky130', 'HS', 'TYP')
```

#### 脚本配置

首先将aes_cipher_top 的配置拷贝到picorv32中，指令如下：

```bash
cp -r aes_cipher_top/ picorv32
```

其中，对于综合脚本，需要修改rtl 源，如图所示

![image-20220413193443968](upload\image-20220413193443968.png)

将`aes_cipher_top`中的源文件修改为：

![image-20220413193524890](upload\image-20220413193524890.png)



观察综合之后的stas.txt 文件，可以发现，其结果如下图所示：

![image-20220413200531921](upload\image-20220413200531921.png)

相较于`aes_cipher_top`而言，picorv 所拥有的cell 更少，所以使用`aes_cipher_top` 中 floorplan 中所设置的DIE_AREA  和  CORE_AREA 是可行的。

#### 运行后端流程

执行如下指令以运行`iFlow`后端流程：

```bash
./run_flow.py -d picorv32 -s \
synth,floorplan,tapcell,pdn,gplace,resize,dplace,cts,filler,groute,droute,layout -f sky130 -t HS -c TYP -v V1 -l V
```

得到最终的版图文件为：

![image-20220413202842993](upload\image-20220413202842993.png)

## 更换工艺库

### nangate45

在iFlow 中的 nangate45  工艺库 是经过整理的，要想用nangate45 工艺库来设计后端，首先要将nangate45工艺库加到iFlow中，放在"iFlow/foundry" 目录下，然后进入"iFlow/scripts/cfg"目录，编辑"foundry_cfg.py"文件，配置好对应的lib,lef和gds 库的路径以及综合阶段需要禁掉的单元列表"don't use list"。 具体如下图所示： 

![image-20220413203127023](upload\image-20220413203127023.png)

并且需要在综合脚本中添加其tie cell 和 buffer 名称以及内容，具体如下图所示：

![image-20220413203253520](upload\image-20220413203253520.png)

以`aes_cipher_top`为例，其基于nangate45工艺跑对应的设计，其生成的版图如下所示：

```bash
./run_flow.py -d aes_cipher_top -s \
synth,floorplan,tapcell,pdn,gplace,resize,dplace,cts,filler,groute,droute,layout -f nangate45 -t HD -c TYP -v V1 -l V1
```

![image-20220413205453933](upload\image-20220413205453933.png)

### asap7

#### gcd for  asap7

在iFlow库中的asap7工艺库是经过整理的，asap7 是开源的7nm 工艺，因此我们需要吧floorplan 面积调得更小，以保证在一定的利用率下能够顺利布线，修改

floorplan 脚本，这里以gcd 为例，得到其结果为：

![image-20220413203902326](upload\image-20220413203902326.png)

并且设置gplace 参数为：

![image-20220413204136291](upload\image-20220413204136291.png)

运行如下指令： 

```bash
./run_flow.py -d gcd -s \
synth,floorplan,tapcell,pdn,gplace,resize,dplace,cts,filler,groute,droute,layout -f asap7 -t HS -c TYP -v V1 -l V1
```

得到最终的版图如下所示：

![image-20220414085340280](upload\image-20220414085340280.png)

#### uart for asap7

由于uart 中的单元和 gcd 是相似的，因此在设置floorplan 的时候，也需要考虑到具体的约束，因此DIE_AREA 和 CORE_AREA 分别设置为如下：

![image-20220413205758670](upload\image-20220413205758670.png)

在进行gplace 时，也需要修改具体的`PLACE_DENSITY`，修改为0.8，如下图所示，否则会不满足约束：

![image-20220413210252191](upload\image-20220413210252191.png)

运行如下指令对`uart`进行后端流程的处理：

```bash
./run_flow.py -d uart -s \
synth,floorplan,tapcell,pdn,gplace,resize,dplace,cts,filler,groute,droute,layout -f asap7 -t HS -c TYP -v V1 -l V1
```

得到`uart`在asap7 工艺库下的版图为： 

![image-20220420195928030](upload\image-20220420195928030.png)