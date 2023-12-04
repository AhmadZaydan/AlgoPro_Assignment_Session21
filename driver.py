from definition_module import PricingAZ

def createList():
    item = int(input("Enter the number of items you want to buy (at least 1): "))
    while item < 1:
        item = int(input("Enter at least 1 item: "))

    food_list = []

    for i in range(item):
        print("Item $", i + 1)
        food = input("Enter food: ")
        amount = float(input("Enter amount of pounds: "))
        while amount < 0:
            amount = float(input("Number of pounds must be > 0"))
        
        myFood = PricingAZ(food, amount)
        food_list.append(myFood)

    return food_list
    
def displayList(foodList):
    print("Here's a summary of the items purchased:")
    print("----------------------------------------")
    for food in foodList:
        print(food.__str__())

def main():
    myFoodList = createList()
    displayList(myFoodList)
    total_cost = PricingAZ.getTotalCost()
    print("Total Cost:", total_cost)

main()
