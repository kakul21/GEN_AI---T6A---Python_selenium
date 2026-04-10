from Core.base_api import BaseApi
from utils.config import BASE_URL

class LoginAPI:

    def __init__(self):
        self.api = BaseApi(BASE_URL)

    def login(self,payload):
        return  self.api.post("/users/login",json=payload)


