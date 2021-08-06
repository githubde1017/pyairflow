#!/usr/bin/env python
# coding: utf-8

import os, sys
import pandas as pd
from glob import glob
print("Please enter username:")
username = input("")
folderpath = "/Users/" + username + "/Documents/00_stock/*.htm"
result = glob(folderpath)
Tlist = []
n = 0
for f in result:
    f = os.path.basename(f)
#    print(f)
    table0 = pd.read_html("/Users/" + username + "/Documents/00_stock/" + f, encoding="big5")[3]
    table = table0.drop(table0.columns[[1]],axis=0)
#    table = table.drop(table.columns[9:296],axis=1)
    n = n + 1
    Tlist.append(table)
print(Tlist)

#print("==============")
#print("資料筆數",n,"筆")


import pandas as pd
import glob
username = input("")
path = r'/Users/' + username + '/Documents/00_stock' # use your path
all_files = glob.glob(path + "/*.htm")

li = []

for filename in all_files:
    df = pd.read_html(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)


import pandas as pd

# 將列表轉為df
table_df = pd.DataFrame(Tlist[1:],columns=Tlist[0])

# 儲存excel
table_df.to_excel('test.xlsx')

table_df


