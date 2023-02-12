class Store:
    def __init__(self, name, list):
        self.name = name
        self.list = []

    def add_product(self, new_product):
        self.new_product = list.append(new_product)

    def sell_product(self, id):
        list[id].pop()
        return self

    def inflation(self, percent_increase):
        

    def set_clearance(self, category, percent_discount):
        pass


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price * (1 + self.percent_change)
        else:
            self.price = self.price / (1 + self.percent_change)
        return self.price

    def print_info(self):
        print(self.name)
        print(self.category)
        print(self.price)
        return self


