class PricingAZ:
    __totalCost = 0.0

    def __init__(self, food="", amount=0):
        self.__food_name = food
        self.__food_amount = amount
        self.__standard_price = self.__PriceList()
        self.__calculated_price = self.__calcCost()

    def __PriceList(self):
        lowFoodName = self.__food_name.lower()
        if lowFoodName == "Dry Cured Iberian Ham":
            return 177.80
        elif lowFoodName == "Wagyu Steaks":
            return 450.00
        elif lowFoodName == "Matsutake Mushrooms":
            return 272.00
        elif lowFoodName == "Kopi Luwak Coffee":
            return 306.50
        elif lowFoodName == "Moose Cheese":
            return 487.20
        elif lowFoodName == "White Truffles":
            return 3600.00
        elif lowFoodName == "Blue Fin Tuna":
            return 3603.00
        elif lowFoodName == "Le Bonnotte Potatoes":
            return 270.81
        else:
            return 0.0

    def __calcCost(self):
        cost = self.__standard_price * self.__food_amount
        PricingAZ.__totalCost += cost
        return cost

    def getTotalCost():
        return PricingAZ.__totalCost

    def __str__(self):
        return "\nItem " + self.__food_name + \
               "\nAmount: Ordered " + "@ ${:,.2f}".format(self.__food_amount) + \
               "\nPrice: per pound " + "@ ${:,.2f}".format(self.__standard_price) + \
               "\nItem: Ordered " + "@ ${:,.2f}".format(self.__calculated_price)
    
        