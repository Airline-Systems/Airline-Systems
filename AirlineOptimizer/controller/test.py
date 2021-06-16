class Product:
    def __init__(self, product_name, occupancy, culture_coefficients, daytime):
        self.product_name = product_name
        self.occupancy = occupancy
        self.culture_coefficients = culture_coefficients
        self.daytime = daytime

    def calculate_demand(self):
        mean_sales = int(round((2 * self.occupancy), 0))
        delay_coefficients = 1
        daytime_coefficient = 1
        optimal_load = int(round((mean_sales * self.occupancy * delay_coefficients * self.culture_coefficients * daytime_coefficient), 0))
        return optimal_load


count = int(Product('panini', 178, 1.24,'morning'))
print(count)