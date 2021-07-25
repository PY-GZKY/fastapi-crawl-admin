import uuid

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    # 通用的字段
    # id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # create_time = Column(DateTime, default=datetime.now, server_default=func.now(), comment="创建时间")
    # update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, server_default=func.now(),server_onupdate=func.now(), comment="更新时间")
    # is_delete = Column(Integer, default=0, comment="逻辑删除:0=未删除,1=删除", server_default='0')
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        import re
        # 如果没有指定__tablename__  则默认使用model类名转换表名字
        name_list = re.findall(r"[A-Z][a-z\d]*", cls.__name__)
        # 表名格式替换成 下划线_格式 如 MallUser 替换成 mall_user
        return "_".join(name_list).lower()

    @declared_attr
    def __table_args__(cls) -> dict:
        return {'extend_existing': True}  # 创建时跳过已创建的表


def gen_uuid() -> str:
    return uuid.uuid4().hex
