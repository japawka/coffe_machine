class Ship:
    def __init__(self, name, destination, capacity):
        self.name = name
        self.destination = destination
        self.capacity = capacity
        self.cargo = 0

    def sail(self):
        print("The {} has sailed for {}!".format(self.name, self.destination))


black_pearl = Ship("Black Pearl", input(), 800)
black_pearl.sail()
