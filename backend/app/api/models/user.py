from sqlalchemy import Boolean, Column, Date, Integer, String

from app.api.db.baseClass import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True, index=True, nullable=False)
    nickname = Column(String(32))
    sex = Column(String(8), doc="性别")
    identity_card = Column(String(32), doc="身份证")
    phone = Column(String(32), doc="手机号")
    address = Column(String(32), doc="地址")
    work_start = Column(Date, doc="入职日期")
    hashed_password = Column(String(128), nullable=False)
    avatar = Column(String(128), doc="头像")
    introduction = Column(String(256), )
    status = Column(String(32), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
