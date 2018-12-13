

class Store:

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })


    def stock_price(self):
       return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        new_store = cls(store.name + ' - franchise') #Store(store.name + ' - franchise')
        return new_store

    @staticmethod
    def store_details(store):
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))



if __name__ == '__main__':
    store = Store("Google")
    store.add_item("Microsoft", 123)
    print(store.name)
    print(store.items)

    n_store = store.franchise(store)
    print(n_store.name)
