# -*- coding: utf-8 -*
# @Time : 2020/12/22 15:58


from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from app.api.db.mongoDB import get_database


import pandas as pd
import numpy as np
from io import BytesIO


class ExcelTools:
    def __init__(self, columns_map=None, order=None):
        '''
        :param columns_map: 列名映射 => {"name":"姓名"，"score":"成绩","sex":"性别"}
        :param columns_map: 列排序列表 => ["name","sex","score"]
        '''
        self.columns_map = columns_map
        self.order = order

    def get_excel_header(self,excel):
        df = pd.read_excel(excel, skiprows=None)
        print(df.columns)
        return df.columns

    # 表格转字典
    def excel_to_dict(self,excel,skiprows=1):
        '''
        Excel转Python dict
        :param excel: bytes
        :return:
        '''
        if not excel:
            return []
        df = pd.read_excel(excel, skiprows=None)
        df = df.replace(np.nan, '', regex=True)
        # 去除所有列数据中的空格
        stripstr = lambda x: x.strip() if isinstance(x, np.unicode) else x
        df = df.applymap(stripstr)
        # 列名映射
        if self.columns_map:
            columns_map = dict(zip(self.columns_map.values(), self.columns_map.keys()))
            df = df.rename(columns=columns_map)
        result = df.to_dict(orient='records')
        return result

    # 字典转表格
    def dict_to_excel(self, datas):
        """
        :param datas: 数据集 => [{"name":"张三","score":90，"sex":"男"}]
        :return:
        """
        # 初始化IO
        output = BytesIO()

        # 将字典列表转换为DataFrame
        pf = pd.DataFrame(datas)

        # 按字段排序
        if self.order:
            pf = pf[self.order]

        # 将列名替换为中文
        if self.columns_map:
            pf.rename(columns=self.columns_map, inplace=True)

        # 指定生成的Excel表格名称
        writer = pd.ExcelWriter(output, engine='xlsxwriter')

        # 替换空单元格
        pf.fillna(' ', inplace=True)

        # 输出
        pf.to_excel(writer, encoding='utf-8', sheet_name='sheet1', index=False)

        # 格式化Excel
        workbook = writer.book
        worksheet = writer.sheets['sheet1']
        format = workbook.add_format({'text_wrap': True})

        # 设置列宽
        for i, col in enumerate(pf.columns):
            # find and set length of column
            column_len = pf[col].astype(str).str.len().max()
            column_len = max(column_len, len(col)) + 2

            # set column length
            worksheet.set_column(i, i, column_len)

        # 保存到IO
        writer.close()
        output.seek(0)

        return output


if __name__ == '__main__':
    pass