from app.core.service import BaseService
from app.models import User


class UserService(BaseService):
    model = User
