from typing import Generator

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app.api.models.hosts import Hosts
from app.config.development_config import settings
from app.security.security import AES_Encrypt

Base = declarative_base()

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    max_overflow=4,  # 超过连接池大小外最多创建的连接
    pool_size=100,  # 连接池大小
    pool_timeout=60,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=3600,  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    echo=False,
    pool_pre_ping=True,
    encoding="utf-8"
)

SessionLocal = sessionmaker(bind=engine)

# 初始化 mysql 连接
import databases

# f"mysql://root:{parse.quote_plus('')}@127.0.0.1:3306/crawlAdmin?charset=utf8mb4"
database = databases.Database(settings.DATABASE_URL)  # 申明一个测试对象


def get_db() -> Generator:
    try:
        db = SessionLocal()

        yield db
    finally:
        db.close()

# 初始化本地主节点
def __initMasterHost(db: Session = Depends(get_db)):
    db = SessionLocal()
    # try:
    hostInfo = db.query(Hosts).filter(Hosts.host_type == settings.MASTER).first()
    if hostInfo:
        hostInfo.host_name = settings.MASTER_NAME
        hostInfo.ip = settings.MASTER_HOST
        hostInfo.port = settings.MASTER_PORT
        hostInfo.username = settings.MASTER_USERNAME
        hostInfo.password = AES_Encrypt(settings.MASTER_PASSWORD)
        hostInfo.desc = settings.MASTER_DESC
    else:
        createMaster = Hosts(
            host_name=settings.MASTER_NAME,
            ip=settings.MASTER_HOST,
            port=settings.MASTER_PORT,
            username=settings.MASTER_USERNAME,
            password=AES_Encrypt(settings.MASTER_PASSWORD),
            host_type=settings.MASTER,
            host_status=1,
            desc=settings.MASTER_DESC,
        )
        db.add(createMaster)
    db.commit()
    return True
    # except Exception:
    #     db.rollback()
    #     return False
