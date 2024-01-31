
class Stock:
    items = []

    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)

    def add_items(self, items):
        for item in items:
            if item not in self.items:
                self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def remove_items(self, items):
        for item in items:
            if item in self.items:
                self.items.remove(item)