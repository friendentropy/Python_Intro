class fruits:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def onyesha(self):
        print(f"My favourite fruit is {self.name}",
              f"and it costs Ksh. {self.price}",
              f"and it's color is {self.color}")


myobj = fruits("Bananas", 100, "yellow")
myobj2 = fruits("Oranges", 70, "orange")
myobj.onyesha()
myobj2.onyesha()

