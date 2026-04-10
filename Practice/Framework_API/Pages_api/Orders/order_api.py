from Core.base_api import BaseApi
from utils.config import BASE_URL

class OrderApi:
    def __init__(self):
        self.api = BaseApi(BASE_URL)

    def get_orders(self,shopper_id,headers):
        return self.api.get(
            f"/shoppers/{shopper_id}/orders",
            headers=headers
        )
