# -*- coding: utf-8 -*
# @Time : 2020/11/10 15:00
import json
import time
import uuid
import zipfile
from typing import Optional, Union, Any

from fastapi import APIRouter, Depends, UploadFile, File
from fastapi_cache import JsonCoder
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response

from app.api.api_v1.core.tools.deployServer import SSHConnection
from app.api.api_v1.core.tools.getHostInfo import HostInfo
from app.api.api_v1.core.tools.testHost import TestConnect
from app.api.common import deps
from app.api.db.session import get_db
from app.api.logger import logger
from app.api.models.hosts import Hosts
from app.api.utils import responseCode
from app.api.utils.responseCode import resp_400, resp_200
from app.config import settings
from app.security.security import AES_Decrypt, AES_Encrypt

router = APIRouter()


async def get_host_list(*, request: Request,
                        db: Session = Depends(get_db),
                        status: str = None,
                        # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                        ):
    hostList = db.query(Hosts).filter(Hosts.host_status == status).all() if status else db.query(Hosts).all()
    resultList = [{
        'id': host.id,
        'hostName': host.host_name,
        'hostStatus': host.host_status,
        'ip': host.ip,
        'port': host.port,
        'username': host.username,
        'hostType': host.host_type,
        'isVerify': host.is_verify,
        'desc': host.desc,
        'uuid': host.uuid,
        'updateTime': str(host.update_time)
    } for host in hostList]
    return resp_200(data=resultList)


def default_key_builder(
        func,
        namespace: Optional[str] = "100875",
        request: Optional[Request] = None,
        response: Optional[Response] = None,
        args: Optional[tuple] = None,
        kwargs: Optional[dict] = None,
):
    return f"{settings.REDIS_CACHE_KEY}{settings.HOST_DETAIL_KEY}{namespace}"


async def host_detail(
        *, request: Request,
        db: Session = Depends(get_db),
        uuid,
        token_data: Union[str, Any] = Depends(deps.check_jwt_token)
):
    hostInfo = db.query(Hosts).filter(Hosts.uuid == uuid).first()

    # ??????????????????
    @cache(namespace=hostInfo.uuid, expire=settings.HOST_CACHE_EXPIRE, coder=JsonCoder, key_builder=default_key_builder)
    async def get_host_detail(hostInfo):
        # hostInfo = db.query(Hosts).filter(Hosts.id == hostId).first()

        # ?????? redis??????
        cacheHostInfo = await request.app.state.redis.get(
            f"{settings.REDIS_CACHE_KEY}{settings.HOST_DETAIL_KEY}{uuid}")
        # print(cacheHostInfo)
        # ????????????
        if cacheHostInfo:
            logger.debug("????????????")
            cacheHostInfo = json.loads(cacheHostInfo)
            return cacheHostInfo
        else:
            data = {
                'id': hostInfo.id,
                'hostName': hostInfo.host_name,
                # 'hostStatus': hostInfo.host_status,
                'ip': hostInfo.ip,
                'port': hostInfo.port,
                # 'username': hostInfo.username,
                # 'hostType': hostInfo.host_type,
                'isVerify': hostInfo.is_verify,
                'desc': hostInfo.desc,
                'updateTime': str(hostInfo.update_time)
            }
            sysInfo = HostInfo().info_(host=hostInfo.ip, port=hostInfo.port, username=hostInfo.username,
                                       password=AES_Decrypt(hostInfo.password))
            logger.debug(sysInfo)
            sysInfo.update(data)
            print(sysInfo)
            return dict(code=200, message="Success", hostInfo=sysInfo)

    return await get_host_detail(hostInfo)


# ????????????
async def create_host(*, request: Request,
                      dictParams: dict,
                      db: Session = Depends(get_db)
                      ):
    # print(dictParams)
    # try:
    createHost = Hosts(
        host_name=dictParams.get("hostName"),
        ip=dictParams.get("ip"),
        port=dictParams.get("port"),
        username=dictParams.get("username"),
        password=AES_Encrypt(dictParams.get("password")),
        host_type=dictParams.get("type", "????????????"),
        uuid=dictParams.get("uuid", str(uuid.uuid4())),
        desc=dictParams.get("desc"),
    )
    db.add(createHost)
    db.commit()
    return resp_200(message='????????????')
    # except:
    #     db.rollback()
    #     return resp_400(message='????????????')


# ????????????


def edit_host(*, request: Request,
              dictParams: dict,
              db: Session = Depends(get_db),
              # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
              ):
    hostInfo = db.query(Hosts).filter(Hosts.id == dictParams.get("id")).first()
    # try:
    hostInfo.host_name = dictParams.get("hostName"),
    hostInfo.ip = dictParams.get("ip"),
    hostInfo.port = dictParams.get("port"),
    hostInfo.username = dictParams.get("username"),
    hostInfo.password = AES_Encrypt(dictParams.get("password")) if dictParams.get("password") else hostInfo.password,
    hostInfo.host_type = dictParams.get("hostType", "????????????"),
    hostInfo.host_status = dictParams.get("hostStatus", "??????"),
    # hostInfo.uuid=dictParams.get("uuid",uuid.uuid4()),
    hostInfo.desc = dictParams.get("desc"),
    hostInfo.update_time = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime())
    db.commit()
    return resp_200(message='????????????')
    # except:
    #     db.rollback()
    #     return resp_400(message='ID?????????')


# ????????????
async def delete_host(*, request: Request,
                      dictParams: dict,
                      db: Session = Depends(get_db),
                      # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                      ):
    try:
        db.query(Hosts).filter(Hosts.id == dictParams.get(
            "hostId")).delete(synchronize_session=False)
        db.commit()
        return resp_200(message='????????????')
    except:
        db.rollback()
        return resp_400(message='????????????')


# ????????????
async def test_host(*, request: Request,
                    dictParams: dict,
                    db: Session = Depends(get_db),
                    # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                    ):
    # try:
    hostInfo = db.query(Hosts).filter(
        Hosts.id == dictParams.get("hostId")).first()
    print(hostInfo.ip, hostInfo.username)
    testClass = TestConnect(
        host=hostInfo.ip,
        port=hostInfo.port,
        username=hostInfo.username,
        password=AES_Decrypt(hostInfo.password),
    )  # ???????????? 22

    testResult = testClass.run()
    if testResult:
        # ?????????????????????????????????
        hostInfo.host_status = 1
        db.commit()
    else:
        # ?????????????????????????????????
        hostInfo.host_status = -1
        db.commit()

    print(testResult)
    return resp_200(data=dict(ip=hostInfo.ip, hostName=hostInfo.host_name, uname=testResult),
                    message='????????????') if testResult else resp_400(message='????????????', data="????????????????????????")
    # except:
    #     db.rollback()
    #     return resp_400()


def recombination_deploy_task(hosts: list, db: Session = Depends(get_db)):
    newHosts = []
    for host in hosts:
        hostDict = {}
        hostInfo = db.query(Hosts).filter(Hosts.ip == host).first()
        hostDict.update({
            'host': hostInfo.ip,
            'port': hostInfo.port,
            'username': hostInfo.username,
            'password': AES_Decrypt(hostInfo.password),  # password ??????
        })
        # print(hostDict)
        newHosts.append(hostDict)
    return newHosts


def deploys(
        *, request: Request,
        dictParam: dict,
        db: Session = Depends(get_db),
        token_data: Union[str, Any] = Depends(deps.check_jwt_token)
):
    # try:
    print(f"????????????????????????: {dictParam.get('hosts')}")
    print(f"??????????????????ID: {dictParam.get('cmd')}")

    newHosts = recombination_deploy_task(hosts=dictParam.get('hosts'), db=db)
    SSHConnection(command=dictParam.get('cmd')).bulk_deploy(hosts=newHosts)

    # ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
    # db.commit()  # ????????????????????????
    return resp_200(data={}, message='????????????')


# ssh????????????
def change_rsa_verify(*, request: Request,
                      dictParams: dict,
                      db: Session = Depends(get_db),
                      # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                      ):
    try:
        hostInfo = db.query(Hosts).filter(
            Hosts.id == dictParams.get("hostId")).first()
        hostInfo.is_verify = False if hostInfo.is_verify else True
        hostInfo.update_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())
        db.commit()
        return resp_200(message='????????????')
    except:
        db.rollback()
        return resp_400()


"""?????? RSA PRIVATE KEY ???????????????,?????????????????? """


def get_rsa_private_key(*, request: Request,
                        dictParams: dict,
                        db: Session = Depends(get_db),
                        token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                        ):
    print(dictParams)
    try:
        hostInfo = db.query(Hosts).filter(Hosts.id == dictParams.get("hostId")).first()
        db.commit()
    except:
        db.rollback()
        return resp_400()


"""
????????????????????????????????????????????????
?????????????????????????????????(???????????????????????????????????????)???????????????????????????????????????
"""


def get_zip_file(zip_file, folder_abs):
    zip_file = zipfile.ZipFile(zip_file)
    zip_list = zip_file.namelist()  # ??????????????????????????????
    for f in zip_list:
        zip_file.extract(f, folder_abs)  # ?????????????????????????????????
    zip_file.close()  # ???????????????????????????????????????


async def upload(
        # token_data: Union[str, Any] = Depends(deps.check_jwt_token),
        file: UploadFile = File(...)
):
    logger.info(f"????????????:{file.filename}")
    save_dir = f"{settings.BASE_DIR}/app/assets/spiderZip"
    try:
        content = await file.read()
        with open(f'{save_dir}/{file.filename}', 'wb') as f:
            f.write(content)
        get_zip_file(f'{save_dir}/{file.filename}', f'{save_dir}')  # ????????????
        return responseCode.resp_200(data={"file": file.filename, "content_type": file.content_type})

    finally:
        file.file.close()


# def exceutCmd(*, request: Request,
#               file: UploadFile = File(...)
#               # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
#               ):
#     # result = gogogo(file)
#     print(file.filename)
#     return resp_200()


# ------------------------------- ???????????? --------------------------------
# ?????? ??? ???????????????????????????????????????
router.add_api_route(methods=['GET'], path="s",
                     endpoint=get_host_list, summary="??????????????????")
router.add_api_route(methods=['POST'], path="/create",
                     endpoint=create_host, summary="????????????")
router.add_api_route(methods=['PUT'], path="/edit",
                     endpoint=edit_host, summary="????????????")
router.add_api_route(methods=['DELETE'], path="/delete",
                     endpoint=delete_host, summary="????????????")
router.add_api_route(methods=['POST'], path="/test",
                     endpoint=test_host, summary="??????????????????")
router.add_api_route(methods=['GET'], path="/detail",
                     endpoint=host_detail, summary="????????????")

router.add_api_route(methods=['PUT'], path="/deploys",
                     endpoint=deploys, summary="????????????(??????????????????)")

router.add_api_route(methods=['PUT'], path="/uploadZip",
                     endpoint=upload, summary="?????????????????????")
router.add_api_route(methods=['POST'], path="/get_rsa_private_key",
                     endpoint=get_rsa_private_key, summary="??????ssh??????")
router.add_api_route(methods=['POST'], path="/change_rsa_verify",
                     endpoint=change_rsa_verify, summary="rsa????????????")
