class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dolars, deposit_cents):
        self.dollars += deposit_dolars
        self.cents += deposit_cents

        if self.cents > 99:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100




# piggy = PiggyBank(1, 1)
# piggy.add_money(3, 12)
# print(piggy.dollars, piggy.cents)