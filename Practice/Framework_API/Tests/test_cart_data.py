from Pages_api.Cart.Cart_api import CartAPI
from utils.read_data import read_json

def test_add_to_cart(auth_data, headers):
    cart_api = CartAPI()
    shopper_id = auth_data["user_id"]
    payload = read_json("test_data/Cart_data.json")

    response = cart_api.add_to_cart(payload, shopper_id=shopper_id,headers=headers)
    assert response.status_code in [201, 200]

    print(response.json())

def test_get_cart(auth_data, headers):
    cart_api = CartAPI()
    shopper_id = auth_data["user_id"]
    response = cart_api.cart(shopper_id=shopper_id, headers=headers)
    assert response.status_code == 200
    print(response.json())


