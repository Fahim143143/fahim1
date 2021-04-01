class ArrayStack:
    def __init__(self):
        self.item = []
        self.price = []
        self.num = 0

    def push(self, item, price):
        self.num = self.num + price
        self.item.append(item)
        self.price.append(price)

    def pop(self):
        self.num = self.num - self.price[len(self.price) - 1]
        return self.item.pop(), self.price.pop()

    def get_stack(self):
        return self.item[len(self.item)-1], self.item

    def overall(self):
        return self.num

    def iteml(self, x):
        return self.item[x], self.price[x]

    def paymentdone(self):
        if not self.price:
            return 0
        else:
            return -1

if __name__ == "__main__":
    s = ArrayStack()
    s.push('Cake', 5)
    s.push('Yogurt', 3)
    s.push('Milk', 2)
    s.push('Crisps', 3)
    s.push('Bread', 1)
    s.push('Pasta', 5)
    s.push('Orange', 2)
    s.push('Cream Roll', 3)
    s.push('Banana', 2)
    s.push('Apple', 3)
    s.pop()
    s.pop()
    # s.pop()
    # s.pop()
    # s.pop()
    # s.pop()

    for i in range(len(s.item)):
        print(s.iteml(i))
    print()
    print("Total= £", s.overall())
    #print('Thank you for shopping with us.', s.paymentdone())