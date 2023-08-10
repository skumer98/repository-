# Sara Umer 1999495
# Create Interactive Invetory Qiery Capability 
# a. Query the user of an item by asking for manufacturer and item type with a single query. 

#   i. Print a message(“No such item in inventory”) if either the manufacturer or the
#      item type are not in the inventory, more that one of either type is submitted or
#      the combination is not in the inventory. Ignore any other words, so “nice Apple
#      computer” is treated the same as “Apple computer”.

# ii. Print “Your item is:” with the item ID, manufacturer name, item type and price
#     on one line. Do not provide items that are past their service date or damaged. If
#     there is more than one item, provide the most expensive item

# iii. Also print “You may, also, consider:” and print information about the same item
#      type from another manufacturer that closes in price to the output item. Only
#      print this if the same item from another manufacturer is in the inventory and is
#      not damaged nor past its service date

# iv. After output for one query, query the user again. Allow ‘q’ to quit.



import csv
from datetime import datetime

# create a class for each object 
class InventoryItem:
    def __init__(self, item_id, manufacturer, item_type, price, service_date, damaged):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.damaged = damaged

    def is_damaged(self):
        return self.damaged == 'damaged'

    def is_past_service_date(self):
        current_date = datetime.now()
        return convert_to_datetime(self.service_date) < current_date

# read data from csv file 
def read_data_from_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            data.append(row)
    return data

def create_manufacturer_dict():
    manufacturer_data = read_data_from_csv('ManufacturerList.csv')
    manufacturer_dict = {}
    for row in manufacturer_data:
        item_id, manufacturer_name, item_type, damaged = row
        manufacturer_dict[item_id] = {
            'manufacturer_name': manufacturer_name,
            'item_type': item_type,
            'damaged': damaged
        }
    return manufacturer_dict

def create_price_dict():
    price_data = read_data_from_csv('PriceList.csv')
    price_dict = {}
    for row in price_data:
        item_id, item_price = row
        price_dict[item_id] = float(item_price)
    return price_dict

def create_service_date_dict():
    service_date_data = read_data_from_csv('ServiceDatesList.csv')
    service_date_dict = {}
    for row in service_date_data:
        item_id, service_date = row
        service_date_dict[item_id] = service_date
    return service_date_dict

def convert_to_datetime(date_string):
    return datetime.strptime(date_string, '%m/%d/%Y')

def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'q':
            return None
        elif len(user_input.split()) == 2:
            manufacturer, item_type = user_input.split()
            return manufacturer, item_type
        else:
            print("Invalid input. Please provide both manufacturer and item type.")

# create query inventory using def code
def query_inventory(manufacturer_data, price_data, service_date_data):
    manufacturer, item_type = get_valid_input("Enter manufacturer and item type (or 'q' to quit): ")
    if manufacturer is None:
        return

    items = []
    for item_id, item_info in manufacturer_data.items():
        if item_info['manufacturer_name'] == manufacturer and item_info['item_type'] == item_type:
            item = InventoryItem(item_id, item_info['manufacturer_name'], item_info['item_type'], 
                                 price_data.get(item_id, 0), service_date_data.get(item_id, 'N/A'), 
                                 item_info['damaged'])
            if not item.is_damaged() and not item.is_past_service_date():
                items.append(item)
# use if statements to depict length of items 
    if len(items) == 0:
        print("No such item in inventory")
    else:
        items.sort()
        output_item = items[0]
        print("Your item is:")
        print(f"Item ID: {output_item.item_id}, Manufacturer: {output_item.manufacturer}, "
              f"Item Type: {output_item.item_type}, Price: {output_item.price}")
        
        similar_items = [item for item in items if abs(item.price - output_item.price) <= 50 and item.item_id != output_item.item_id]
        if similar_items:
            print("You may also consider:")
            similar_item = similar_items[0]
            print(f"Item ID: {similar_item.item_id}, Manufacturer: {similar_item.manufacturer}, "
                  f"Item Type: {similar_item.item_type}, Price: {similar_item.price}")

    query_inventory(manufacturer_data, price_data, service_date_data)

if __name__ == '__main__':
    manufacturer_data = create_manufacturer_dict()
    price_data = create_price_dict()
    service_date_data = create_service_date_dict()

    query_inventory(manufacturer_data, price_data, service_date_data)
