# -*- coding: utf-8 -*
# @Time : 2020/12/22 16:01
import os.path
import uuid
import zipfile
from typing import Union, Any

from starlette.responses import Response

from app.api.apiV1.router.file.wordTool import returnWord, mongoWord
from app.api.common import deps
from app.api.db.mongoCurd import do_find, do_insert, do_find_select_time
from app.api.utils.responseCode import resp_200, resp_400

from motor.motor_asyncio import AsyncIOMotorClient
from app.api.apiV1.router.file.excelTool import ExcelTools
from app.api.db.mongoDB import get_database
import mimetypes
from datetime import datetime
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import StreamingResponse

from app.config import settings

router = APIRouter()


async def excelExport(
        response: Response,
        dataParams: dict,
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
        db: AsyncIOMotorClient = Depends(get_database),

):
    timeRange = dataParams.get("timeRange")
    # rows = await do_find(db)
    rows = await do_find_select_time(db, startTime=timeRange[0], endTime=timeRange[1])
    try:
        excel_tools = ExcelTools()
        excel = excel_tools.dict_to_excel(rows)
        file_name = 'devices' + '-' + datetime.now().strftime("%Y%m%d_%H%M%S") + '.xls'
        mime = mimetypes.guess_type(file_name)[0]
        print(f"文件名: {file_name}, 文件类型: {mime}")
        # response.headers["Access-Control-Expose-Headers"] = "Content-Disposition"
        return StreamingResponse(content=excel,
                                 media_type=mime,
                                 headers={'Access-Control-Expose-Headers': 'Content-Disposition',
                                          'Content-Disposition': file_name})
    except:
        return resp_400(data="导出数据为空", message="ERROR")


# 进行导入文件格式限制
async def excelImport(
        file: UploadFile = File(..., description="使用form表单上传文件"),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token),
        db: AsyncIOMotorClient = Depends(get_database)):
    if file:
        excel_tool = ExcelTools()
        filename = file.filename
        ext = filename.split('.')[-1].replace('"', '')

        # 限定文件格,只对excel表格后缀做处理
        if ext not in ['xls', 'xlsx']:
            return resp_400(data="不可解析的文件")
        parsed_dict = excel_tool.excel_to_dict(file.file)
        await do_insert(db, parsed_dict)
        return resp_200(message="文件上传成功", data={
            "fileName": filename,
            "type": "import"
        },
                        )

    return resp_400(data="请选择上传文件")


# MongoDB数据转换为词云
async def mongoToWord(
        db: AsyncIOMotorClient = Depends(get_database),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token), ):
    wordList = await mongoWord(db)
    return resp_200(message="文件上传成功", data=wordList)


# 导入文件转换为词云
async def excelToWord(
        file: UploadFile = File(..., description="使用form表单上传文件"),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token), ):
    if file:
        excel_tool = ExcelTools()
        filename = file.filename
        ext = filename.split('.')[-1].replace('"', '')

        # 限定文件格,只对excel表格后缀做处理
        if ext not in ['xls', 'xlsx']:
            return resp_400(data="不可解析的文件")
        wordList = returnWord(file.file)
        print(wordList)

        return resp_200(message="文件上传成功", data=wordList)

    return resp_400(data="请选择上传文件")


def get_zip_file(zip_file, folder_abs):
    zip_file = zipfile.ZipFile(zip_file)
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件
    for f in zip_list:
        zip_file.extract(f, folder_abs)  # 循环解压文件到指定目录
    zip_file.close()  # 关闭文件，必须有，释放内存


# 上传zip任务包到指定目录
async def uploadZip(
        file: UploadFile = File(..., description="使用form表单上传文件"),
        # token_data: Union[str, Any] = Depends(deps.check_jwt_token),
):
    if file:
        filename = file.filename
        print(filename)
        name, ext = filename.split('.')
        # print(name,ext)

        # 限定文件格,只对zip后缀做处理
        if ext not in ['zip']:
            return resp_400(data="不可解析的文件")

        content = await file.read()
        randomUuid = str(uuid.uuid4())
        with open(f"{settings.LOCAL_DIR}/{randomUuid}.zip", "wb") as f:
            f.write(content)

        # get_zip_file(f"./task/{filename}","./task/") # 解压一下

        return resp_200(message="文件上传成功", data={
            "uuid": randomUuid,
            "type": "import"
        }
                        )

    # return resp_400(data="请选择上传文件")


router.add_api_route(methods=['PUT', 'POST'], path="/import", endpoint=excelImport, summary="导入excel")
router.add_api_route(methods=['GET', 'POST'], path="/export", endpoint=excelExport, summary="导出excel")
router.add_api_route(methods=['POST'], path="/importWord", endpoint=excelToWord, summary="excel转词云")
router.add_api_route(methods=['POST'], path="/importMongo", endpoint=mongoToWord, summary="mongodb转词云")
router.add_api_route(methods=['POST'], path="/uploadZip", endpoint=uploadZip, summary="上传zip任务")
