# -*- coding: utf-8 -*
# @Time : 2020/11/10 15:00
import json
import uuid
from typing import Union, Any

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api.api_v1.core.spider_log.save_log import remove_task_log
from app.api.api_v1.core.spider_status.get_status import start_spider_status, end_spider_status
from app.api.api_v1.core.tools.deployTask import SSHConnection
from app.api.common import deps
from app.api.db.session import get_db
from app.api.logger import logger
from app.api.models.hosts import Hosts
from app.api.models.proTask import Project, TaskLog, Tasks
from app.api.utils.responseCode import resp_200, resp_400
from app.config.development_config import settings
from app.security.security import AES_Decrypt

router = APIRouter()


# 项目首页
async def project_list(*, request: Request, db: Session = Depends(get_db),
                       token_data: Union[str, Any] = Depends(deps.check_jwt_token)):
    # logger.info(f"用户{token_data.sub} 正在操作")
    logger.info(request.client.host)
    projectList = db.query(Project).all()
    data = [{
        'projectName': projectCore.project_name,
        'projectId': projectCore.project_id,
        'updateTime': str(projectCore.update_time),
        'projectDesc': projectCore.project_desc
    } for projectCore in projectList]
    return resp_200(data=data)


# 创建项目
def create_project(*, request: Request,
                   dictParam: dict,
                   db: Session = Depends(get_db)
                   ):
    try:
        createProject = Project(
            project_id=str(uuid.uuid4()),
            project_name=dictParam.get("projectName"),
            project_desc=dictParam.get("projectDesc")
        )
        db.add(createProject)
        db.commit()
        return resp_200(message='创建成功')
    except:
        db.rollback()
        return resp_400(message='创建失败')


# 删除项目
def delete_project(*, request: Request,
                   dictParam: dict,
                   db: Session = Depends(get_db)
                   ):
    try:
        # 先删除该项目下的所有任务(主键关联)
        db.query(Tasks).filter(Tasks.project_id == dictParam.get(
            "proId")).delete(synchronize_session=False)
        # 删除该项目
        db.query(Project).filter(Project.project_id == dictParam.get(
            "proId")).delete(synchronize_session=False)
        db.commit()
        return resp_200(message='删除成功')
    except:
        db.rollback()
        return resp_400(message='删除失败')


# 所有任务
def task_search_list(
        *, request: Request,
        project: str = Query(None, title="项目", description="项目"),
        status: str = Query(None, title="状态", description="状态"),
        db: Session = Depends(get_db)
):
    if all([project, status]):
        taskList = db.query(Tasks).filter(Tasks.project_id == project, Tasks.task_status == status).all()
    elif project:
        taskList = db.query(Tasks).filter(Tasks.project_id == project).all()
    elif status:
        taskList = db.query(Tasks).filter(Tasks.task_status == status).all()
    else:
        taskList = db.query(Tasks).all()
    resuleList = [{
        'projectId': task.project_id,
        'taskId': task.task_id,
        'taskName': task.task_name,
        'taskDesc': task.task_desc,
        'taskLevel': task.task_level,
        'taskStatus': task.task_status,
        'lastRunStatus': task.last_run_status,
        'taskPath': task.local_path,
        'lastRunTime': str(task.last_run_time),
        'createTime': str(task.create_time),
    } for task in taskList]
    return resp_200(data=resuleList)


# 项目下任务列表
def task_list(*, request: Request,
              db: Session = Depends(get_db),
              #  token_data: Union[str, Any] = Depends(deps.check_jwt_token),
              projectId: str
              ):
    taskList = db.query(Tasks).filter(Tasks.project_id == projectId).all()
    data = [{
        'projectId': task.project_id,
        'taskId': task.task_id,
        'taskName': task.task_name,
        'taskDesc': task.task_desc,
        'taskLevel': task.task_level,
        'taskStatus': task.task_status,
        'lastRunStatus': task.last_run_status,
        'taskPath': task.local_path,
        'lastRunTime': str(task.last_run_time),
        'createTime': str(task.create_time),
    } for task in taskList]
    return resp_200(data=data)


# 创建任务
def create_task(*, request: Request,
                dictParam: dict,
                db: Session = Depends(get_db)
                ):
    # try:
    createTask = Tasks(
        project_id=dictParam.get("projectId"),
        task_id=str(uuid.uuid4()),
        task_name=dictParam.get("taskName"),
        task_level=dictParam.get("taskLevel"),
        task_desc=dictParam.get("taskDesc"),
        local_path=dictParam.get("taskPath"),
    )
    db.add(createTask)
    db.commit()
    return resp_200(message='添加成功')
    # except:
    #     db.rollback()
    #     return resp_400(message='添加失败')


# 删除任务
def delete_task(*, request: Request,
                dictParam: dict,
                db: Session = Depends(get_db)
                ):
    print(dictParam)
    # try:
    # 先删除该任务日志信息(主键关联)
    db.query(TaskLog).filter(TaskLog.task_id == dictParam.get(
        "taskId")).delete(synchronize_session=False)
    # 删除该任务
    db.query(Tasks).filter(Tasks.task_id == dictParam.get(
        "taskId")).delete(synchronize_session=False)
    db.commit()
    return resp_200(message='删除成功')
    # except:
    #     db.rollback()
    #     return resp_400(message='删除失败')


# 任务详情
def task_detail(*, request: Request,
                taskId: str,
                db: Session = Depends(get_db)
                ):
    # try:
    print(taskId)
    taskInfo = db.query(Tasks).filter(Tasks.task_id == taskId).first()
    data = {
        'projectId': taskInfo.project_id,
        'taskId': taskInfo.task_id,
        'taskName': taskInfo.task_name,
        'taskDesc': taskInfo.task_desc,
        'taskLevel': taskInfo.task_level,
        'taskStatus': taskInfo.task_status,
        'lastRunStatus': taskInfo.last_run_status,
        'taskPath': settings.REMOTE_DIR,
        'deployedHosts': json.loads(taskInfo.deployed_hosts) if taskInfo.deployed_hosts else [],
        'lastRunTime': str(taskInfo.last_run_time),
        'createTime': str(taskInfo.create_time),

    }
    return resp_200(data=data, message='获取成功')
    # except:
    #     db.rollback()
    #     return resp_400(message='获取失败')


def recombination_deploy_task(hosts: list, taskInfo, db: Session = Depends(get_db)):
    newHosts = []
    for host in hosts:
        hostDict = {}
        hostInfo = db.query(Hosts).filter(Hosts.ip == host).first()
        hostDict.update({
            'host': hostInfo.ip,
            'port': hostInfo.port,
            'username': hostInfo.username,
            'password': AES_Decrypt(hostInfo.password),  # password 解密
            'local_path': f'{settings.LOCAL_DIR}/{taskInfo.local_path}.zip',
            # '/home/pai/Code/local_test/nihao.zip', # 这里应该是上传的 zip 文件，在项目中的目录
            # 'remote_dir': f'{settings.REMOTE_DIR}', # 远程目录 不支持 sftp  nihao.pu -> dir/ 的写法，有空改造源码
            'remote_path': f'{settings.REMOTE_DIR}/{taskInfo.local_path}.zip',
            # '/home/remote_test/nihao.zip' # 应该选择到服务器解压才更合理 这里用任务名称重新命名
        })
        print(hostDict)
        newHosts.append(hostDict)
    return newHosts


def recombination_run_task(hosts: list, command=None, db: Session = Depends(get_db)):
    newHosts = []
    for host in hosts:
        hostDict = {}
        hostInfo = db.query(Hosts).filter(Hosts.ip == host).first()
        hostDict.update({
            'host': hostInfo.ip,
            'port': hostInfo.port,
            'username': hostInfo.username,
            'password': AES_Decrypt(hostInfo.password),  # password 解密
            'command': command  # 执行cmd命令
        })
        print(hostDict)
        newHosts.append(hostDict)
    return newHosts


def deploy_task(*, request: Request,
                dictParam: dict,
                db: Session = Depends(get_db)
                ):
    # try:
    print(f"接收到的主机列表: {dictParam.get('hosts')}")
    print(f"接收到的任务ID: {dictParam.get('taskId')}")
    taskInfo = db.query(Tasks).filter(
        Tasks.task_id == dictParam.get("taskId")).first()

    newHosts = recombination_deploy_task(hosts=dictParam.get('hosts'), taskInfo=taskInfo, db=db)
    future_result_list = SSHConnection(Tasks.task_id).bulk_exce_put_file(newHosts)
    succeedHosts = [future_result[0] for future_result in future_result_list if future_result[1]]

    print(f'成功部署的主机: {succeedHosts}')

    # 合并主机列表并去重
    # 这里待优化 任务表 <--> 主机表  多对多
    newHostList = json.loads(taskInfo.deployed_hosts) + succeedHosts if taskInfo.deployed_hosts else [] + succeedHosts
    setHostList = set(newHostList)
    # print(setHostList)

    taskInfo.deployed_hosts = json.dumps(list(setHostList))
    db.commit()  # 更新已部署的主机

    return resp_200(data={'taskName': 1}, message='成功')


# 开启任务
# 这里接收到提交的参数包括 主机列表 任务id cmd命令
# 根据任务id查询出该任务的代码目录，进到目录执行相应的cmd命令
"""cd /home/tasks/printOut && python printOut.py"""
"""cd /home/tasks/douyin && python getAjaxData.py"""


def run_task(
        *, request: Request,
        dictParam: dict,
        db: Session = Depends(get_db)
):
    # try:
    print(f"接收到的主机列表: {dictParam.get('hosts')}")
    print(f"接收到的任务ID: {dictParam.get('taskId')}")
    print(f"接收到的CMD: {dictParam.get('cmd')}")

    # 任务存在，清空该任务日志
    assert remove_task_log(dictParam.get("taskId"))

    start_spider_status(dictParam.get("taskId"))

    # 多线程任务
    newHosts = recombination_run_task(hosts=dictParam.get('hosts'), command=dictParam.get('cmd'), db=db)
    SSHConnection(task_id=dictParam.get('taskId')).bulk_exce_cmd(newHosts)

    # 更新任务状态
    end_spider_status(dictParam.get("taskId"))

    return resp_200(data={'taskName': 'RedBook'}, message='成功')

    # except:
    #     db.rollback()
    #     return resp_400(message='操作失败')


# 任务日志列表
def task_log_list(*, request: Request,
                  db: Session = Depends(get_db)):
    taskLogList = db.query(TaskLog).all()
    data = [{
        'taskId': task.task_id,
        'taskLogLevel': task.task_log_level,
        'taskLogMsg': task.task_log_msg,
        'host': task.host,
        'updateTime': str(task.update_time),
    } for task in taskLogList]
    return resp_200(data=data)


# ------------------------------- 路由添加 --------------------------------

router.add_api_route(methods=['GET'], path="/projects",
                     endpoint=project_list, summary="返回项目列表")
router.add_api_route(
    methods=['POST'], path="/project/create", endpoint=create_project, summary="创建项目")
router.add_api_route(
    methods=['DELETE'], path="/project/delete", endpoint=delete_project, summary="删除项目")
router.add_api_route(methods=['GET'], path="/project",
                     endpoint=task_list, summary="返回项目任务列表")

router.add_api_route(methods=['GET'], path="/tasks",
                     endpoint=task_search_list, summary="返回所有任务")
router.add_api_route(
    methods=['POST'], path="/task/create", endpoint=create_task, summary="创建任务")
router.add_api_route(
    methods=['DELETE'], path="/task/delete", endpoint=delete_task, summary="删除任务")
router.add_api_route(
    methods=['GET'], path="/task/detail", endpoint=task_detail, summary="任务详情")
router.add_api_route(
    methods=['POST'], path="/task/deploy", endpoint=deploy_task, summary="任务部署")
router.add_api_route(methods=['POST'], path="/task/run",
                     endpoint=run_task, summary="任务开启")
router.add_api_route(methods=['GET'], path="/task/logs",
                     endpoint=task_log_list, summary="返回任务日志列表")
