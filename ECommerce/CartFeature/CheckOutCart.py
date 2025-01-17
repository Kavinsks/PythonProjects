from PythonUniverse.ECommerce.Data.ApplicationData.SettingCartData import SettingCartData
from PythonUniverse.ECommerce.DataPersistent.DataAccessObject import Data_Access_Object


class Checkout:
    def __init__(self, product : dict, cart : dict, isFiles : bool):
        self.product = product
        self.cart = cart
        self.isFiles = isFiles

    def estimate_cost(self):
        total_cost = 0

        for category in self.cart:

            for product in self.cart[category]:

                count = self.cart[category][product]
                price = self.__find_price(category, product)
                total_cost += price * count

        print('\n\n\t\t Total Cost for Your Products in the cart is : ' , total_cost)

    def __find_price(self, category, model) -> int:
        products = self.product[category]

        for prod in products:
            if prod.name.lower() == model:
                return prod.price

        return 0

    def check_out(self):
        self.cart.clear()
        if not self.isFiles:
            Data_Access_Object.check_out()
        else:
            SettingCartData.remove()
        print('\n\n\t\t\t\t You Have Made a Successfully purchased ?')