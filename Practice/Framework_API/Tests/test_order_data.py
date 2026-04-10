from Pages_api.Orders.order_api import OrderApi
from utils.read_data import read_json

def test_get_order(auth_data, headers):
    order_api = OrderApi()

    shopper_id = auth_data["user_id"]

    response = order_api.get_orders(shopper_id, headers)

    print(response.json())

    assert response.status_code == 200