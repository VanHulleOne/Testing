# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:52:03 2016

@author: lvanhulle
"""

import os
import openpyxl
import re

path = 'C:\\Users\\lvanhulle\\Desktop\\G-Codes Carsten Koch'

row = 2
NAME = 'A'
P_NUM = 'B'
SR = 'C'
LAY_H = 'D'

SR_INT = 0
LAY_INT = 4

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
sheet['A1'] = 'File Name'
sheet['B1'] = 'Part Number'
sheet['C1'] = 'Solidity Ratio'
sheet['D1'] = 'Layer Height'

paramRegex = re.compile(r'(\[|\()(.*)(\]|\))')
numRegex = re.compile(r'(\d)+(\.)*(\d*)')

for folderName, subfolders, filenames in os.walk(path):
    for filename in filenames:
        print('File: ', filename)
        sheet[NAME + str(row)] = filename
        with open(path+'\\'+filename, 'r') as f, open('C:\\Users\\lvanhulle\\Desktop\\G-Code\\'+filename, 'w') as out:
            lines = f.readlines()
            line_iter = iter(lines)
            for line in line_iter:
                out.write(line)
                if 'Part number' in line:
                    num = line[-2]
#                    print('Part Number: ', num)
                    sheet[P_NUM + str(row)] = int(num)
                    
                    line = next(line_iter)
#                    print(line)
                    found = paramRegex.search(line)
                    paramList = found.group(2).split(', ')
                    try:
                        sheet[SR + str(row)] = float(paramList[SR_INT])
                        sheet[LAY_H + str(row)] = float(paramList[LAY_INT])
                        out.write(';Parameters: (' + 
                                    'Solidity Ratio='+paramList[SR_INT] + ', ' +
                                    'Print Speed=' + paramList[1] + ', ' +
                                    'ShiftX=' + paramList[2] + ', ' + 
                                    'ShiftY=' + paramList[3] + ', ' + 
                                    'LayerHeight=' + paramList[4] + ', ' +
                                    'NumLayers=' + paramList[5] + ')\n')
                    except Exception:
                        sheet[SR + str(row)] = float(numRegex.search(paramList[SR_INT]).group())
                        sheet[LAY_H + str(row)] = 3.2/float(numRegex.search(paramList[LAY_INT]).group())
                        out.write(line)
                    
                    row += 1
                 
wb.save('Gcode Reference2.xlsx')
