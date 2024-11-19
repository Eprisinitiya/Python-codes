class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.items[item_id] = {"name": item_name, "stock": stock_count, "price": price}

    def update_item(self, item_id, stock_count=None, price=None):
        if item_id in self.items:
            if stock_count is not None:
                self.items[item_id]["stock"] = stock_count
            if price is not None:
                self.items[item_id]["price"] = price
        else:
            print("Item not found")

    def check_item_details(self, item_id):
        return self.items.get(item_id, "Item not found")

inventory = Inventory()
inventory.add_item(1, "Apple", 50, 0.5)
inventory.add_item(2, "Banana", 100, 0.3)
inventory.update_item(1, stock_count=60)
print(inventory.check_item_details(1))