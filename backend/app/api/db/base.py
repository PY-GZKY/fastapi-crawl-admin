# Import all the models, so that Base has them before being
# imported by Alembic
# imported by Alembic # 方便在Alembic导入,迁移用

from app.api.db.baseClass import Base
from app.api.models import hosts
from app.api.models.auth import AdminUser, AdminRole
from app.api.models.todos import Todos
from app.api.models.user import User
from app.api.models.proTask import Project, Tasks, TaskLog

'''
alembic init alembic
alembic revision --autogenerate -m "create"
alembic upgrade head
'''
