# -*- coding:utf-8 -*-
import myParser
import os

config=myParser.prjPath_parser()
projectPath=config["prjPath"]    # 你创建的cpu的工程路径，已自动识别
xilinxPath = "/opt/Xilinx/14.7/ISE_DS/ISE/"  # 你的下载的ISE的路径

os.chdir(projectPath)
os.environ['XILINX'] = xilinxPath  # 设置环境变量
os.system(xilinxPath + "bin/lin64/fuse -nodebug -prj mips_txt_stx_beh.prj -o mips mips_txt > mips.log")  # 编译
os.system("./mips -nolog -tclbatch mips.tcl > res.txt")  # 运行
