class Challenges:

    def dayTwoOperators(self, meal_cost, tip_percent, tax_percent):
        self.meal_cost = float(meal_cost)
        self.tip_percent = int(tip_percent)
        self.tax_percent = int(tax_percent)
        self.total_cost = 0

        self.tip_percent = (self.tip_percent / 100) * self.meal_cost
        self.tax_percent = (self.tax_percent / 100) * self.meal_cost
        self.total_cost  = self.meal_cost + self.tip_percent + self.tax_percent

        return round(self.total_cost)
