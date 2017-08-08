# -*- coding: utf-8 -*-
import os
path = "test.txt"
subfolder = ["Accounting","Audit","China Consulting","Com Sec","HPO","Tax Advisory"]
content = open(path,"r").readlines()
for line in content: 
    line = line.strip()     # trim away \n 
    line = line.replace("-","")
    print(line)
    for item in subfolder:
        os.makedirs("V:/"+line+"/"+item)
    print(line + "created!")
