#  Can Can Word auto-Tester
## 环境
Python 3.7

Anaconda 23.1.0
> 但是应该是有个Python就行，版本不重要，我就用了os/random/argparse三个库

## 参数设置
`--test_size`：单`.asm`文件内希望生成的指令数，默认为500条

`--init`：是否对所有寄存器进行初始化，默认为否

`--bound`：是否对执行边界值测试，默认为否

`--Project`: 针对P5/P6进行测试，默认为6，如果希望生成P5数据则设置 `--Project 5`

# 准备
在顶层模块中写好对MIPS的tb文件，并命名为tb.v

在工程文件夹中加入文件mips.tcl文件，写入
```
run 20000ns;
exit
```

文件层次结构:
```
--dir
----mips.v
----mips.tcl
----mips.prj
----CO_tester_P5
------run.sh
------...
----ALU.v
----...
```

修改下列文件中所有绝对路径
```
compare.py
runISE.py
run.sh
```
# 运行
命令行`run.sh`即可，你将在`compare.txt`内看到本次运行结果

# 获取 & 声明
在github仓库https://github.com/CharlesSebastian1/BUAA_CO_tester_P5

基于Toby学长的Mars进行的模拟，Mars.jar文件已在当前repo中