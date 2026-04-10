from Core.base_api import BaseApi
from utils.config import BASE_URL

class CartAPI:

    def __init__(self):
        self.api = BaseApi(BASE_URL)

    def cart(self, shopper_id, headers):

        return self.api.get(f"/shoppers/{shopper_id}/carts", headers=headers)

    def add_to_cart(self, payload, shopper_id, headers):

        return self.api.post(f"/shoppers/{shopper_id}/carts", headers=headers, json=payload)