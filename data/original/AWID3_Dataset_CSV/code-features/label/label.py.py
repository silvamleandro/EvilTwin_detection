#!/bin/bash
import pandas as pd
from termcolor import cprint
import os
import subprocess
from pathlib import Path

#pip3 install pandas
#pip3 install termcolor
#python 3.8.10

fileNames = subprocess.Popen(['ls | grep "split_"'], stdout=subprocess.PIPE, shell=True)
fileNames = [x.decode('ISO-8859-1').strip() for x in fileNames.stdout.readlines()]

count = len(fileNames)
for fileName in range(count):
    cprint("Progress: "+str(fileName)+"/"+str(count), "green")
    
    my_file = Path("/home/Desktop/labeling/"+fileNames[fileName])
    if my_file.exists():
        continue
        
        # Read data from CSV file into pandas dataframe
    data = pd.read_csv(fileNames[fileName], sep=',', error_bad_lines=False, encoding='ISO-8859-1', low_memory=False)

    data['Label'] = "Normal"    
    name = "Website_spoofing_" + str(fileName) + ".csv"
    data.to_csv(name, index=False)
    os.system("rm -rf "+fileNames[fileName])
        