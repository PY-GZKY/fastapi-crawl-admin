# -*- coding: utf-8 -*
# @Time : 2020/12/25 14:49


from motor.motor_asyncio import AsyncIOMotorClient

from app.api.db.mongoCurd import do_find


import jieba
from collections import Counter
import json
import matplotlib.pyplot as plt
import pandas as pd

def readContent(df,clo="漏单问题"):
    contents = ","
    for i in range(len(df)):
        l_con = str(df[clo][i])
        contents += l_con
    return contents


def mostCommon(contents):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = 'sans-serif'
    words = [x for x in jieba.cut(contents) if len(x) >= 2]
    # print(words, "=============")
    c = Counter(words).most_common(80)  # 取若干组
    return [{"name":cc[0],"value":cc[1]} for cc in c ]

def returnWord(file):
    f = pd.ExcelFile(file)
    print(f.sheet_names)  # 获取工作表名称
    allContent = ","
    for i in f.sheet_names:
        df = pd.read_excel(file, sheet_name=i)
        allContent += readContent(df)
    # 返回所有子表汇总后的分词
    return mostCommon(allContent)



async def mongoWord(db):
    rows = await do_find(db, databaseName="TM",collection="goods_comment")
    allContent = ","
    for i in rows:
        allContent += i.get("评论内容")
    # 返回所有子表汇总后的分词
    # print(mostCommon(allContent))
    return mostCommon(allContent)

