# -*- coding:utf-8 -*-
import os

projectPath = "D:\\CO\\CO_P5\\pipelineCPU"      # 你创建的cpu的工程路径
xilinxPath = "C:\\Xilinx\\14.7\\ISE_DS\\ISE\\"  # 你的下载的ISE的路径

os.chdir(projectPath)
os.environ['XILINX'] = xilinxPath  # 设置环境变量
os.system(xilinxPath + "bin/nt64/fuse -nodebug -prj mips.prj -o mips.exe tb > mips.log")  # 编译
os.system("mips.exe -nolog -tclbatch mips.tcl > res.txt")  # 运行
