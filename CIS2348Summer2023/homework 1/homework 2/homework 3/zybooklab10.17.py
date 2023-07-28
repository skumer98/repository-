# Sara Umer 1999495

#(1) Build the ItemToPurchase class with the following specifications:
#Attributes (3 pts)
    #item_name (string)
    #item_price (float)
    #item_quantity (int)
#Default constructor (1 pt)
    #Initializes item's name = "none", item's price = 0, item's quantity = 0
#Method
    #print_item_cost()

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")



# Main section of the code
item1 = ItemToPurchase()
item1.item_name = input("Item 1\nEnter the item name:\n")
item1.item_price = float(input("Enter the item price:\n"))
item1.item_quantity = int(input("Enter the item quantity:\n"))

item2 = ItemToPurchase()
item2.item_name = input("\nItem 2\nEnter the item name:\n")
item2.item_price = float(input("Enter the item price:\n"))
item2.item_quantity = int(input("Enter the item quantity:\n"))

#(3) Add the costs of the two items together and output the total cost. (2 pts)


total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"\nTotal: ${total_cost}")


