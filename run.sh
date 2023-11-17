#!/bin/bash
python main.py > pylog.txt
timeout 5s java -jar Mars_CO_v0.4.1.jar code.asm db nc mc CompactLargeText coL1 ig > log.txt
java -jar Mars_CO_v0.4.1.jar code.asm db mc CompactDataAtZero a dump .text HexText code.txt  # code.txt会下载到run.sh所在目录下
python runISE.py
python compare.py