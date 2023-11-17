#!/bin/bash
python main.py > pylog.txt
timeout 5s java -jar Mars_CO_v0.4.1.jar code.asm db nc mc CompactLargeText coL1 ig > log.txt
java -jar Mars_CO_v0.4.1.jar code.asm db mc CompactDataAtZero a dump .text HexText code.txt  # code.txt会下载到run.sh同级目录下, 你可以将其修改路径至cpu目录下
# python runISE.py
# python compare.py