#!/bin/bash
python main.py > pylog.txt
timeout 5s java -jar Mars_CO_v0.4.1.jar code.asm db nc mc CompactLargeText coL1 ig > log.txt
java -jar Mars_CO_v0.4.1.jar code.asm db mc CompactDataAtZero a dump .text HexText D:\\CO\\CO_P6\\code.txt  # code.txt会生成至你搭建的cpu工程目录下
# python runISE.py # 如果你希望使用以下功能，需要将code.txt修改至cpu工程目录的绝对路径
# python compare.py