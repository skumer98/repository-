# Sara Umer 1999495 

#1) You will design a program tha manages the invientory of an electronics store. 
#2) concepts that wil be used: Classes, dictionairies, and input and output of comma delimited csv files. 
#3) Input these files: ManufacturerList.csv, PriceList.csv, ServiceDatesList.csv
#4) Your code will be expected to work with any group input files of th appropriate format. 

# Replaced the use of lambda functions within code 

import csv
from datetime import datetime

# Create a class to represent each item in the inventory

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

# Helper function to convert date strings to datetime objects
def convert_to_datetime(date_string):
    return datetime.strptime(date_string, '%m/%d/%Y')

# Open csv files for ManufacturerList.csv, PriceList.csv, ServiceDatesList.csv
# Read data from CSV files and store in dictionaries

manufacturer_data = {}
price_data = {}
service_date_data = {}

# TODO: Implement the code to read data from the input CSV files and populate the dictionaries


def read_data_from_csv(manufacturer_data):
    data = []
    with open(manufacturer_data, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
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

manufacturer_dict = create_manufacturer_dict()
price_dict = create_price_dict()
service_date_dict = create_service_date_dict()

# Example usage:
print(manufacturer_dict)
print(price_dict)
print(service_date_dict)

# Generate processed inventory reports
def generate_full_inventory():
    # Sort items alphabetically by manufacturer name
    sorted_items = sorted(manufacturer_data.values(), key=item: item.manufacturer)

    # Write the data to FullInventory.csv
    with open('FullInventory.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])
        for item in sorted_items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])


def generate_item_type_inventory():
    # Create a dictionary to store items of each item type
    item_type_inventory = {}

    # Group items by their item type
    for item in manufacturer_data.values():
        if item.item_type not in item_type_inventory:
            item_type_inventory[item.item_type] = []
        item_type_inventory[item.item_type].append(item)

    # Write each item type's data to separate CSV files
    for item_type, items in item_type_inventory.items():
        # Sort items by item ID
        sorted_items = sorted(items)#, #key=item: item.item_id)


# Write the data to CSV files with the item type name
        filename = f'{item_type}Inventory.csv'
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item ID', 'Manufacturer', 'Price', 'Service Date', 'Damaged'])
            for item in sorted_items:
                writer.writerow([item.item_id, item.manufacturer, item.price, item.service_date, item.damaged])

def generate_past_service_date_inventory():
    # Get the current date
    current_date = datetime.now()

    # Filter items that are past the service date
    past_service_items = [item for item in service_date_data.values() if convert_to_datetime(item.service_date) < current_date]

    # Sort items by service date from oldest to most recent
    sorted_items = sorted(past_service_items, key=item: convert_to_datetime(item.service_date))

    # Write the data to PastServiceDateInventory.csv
    with open('PastServiceDateInventory.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])
        for item in sorted_items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

def generate_damaged_inventory():
    # Filter items that are damaged
    damaged_items = [item for item in manufacturer_data.values() if item.is_damaged()]

    # Sort items by price from most expensive to least expensive
    sorted_items = sorted(damaged_items)#, key=item: item.price, reverse=True)

    # Write the data to DamagedInventory.csv
    with open('DamagedInventory.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])
        for item in sorted_items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

# Main function to execute the program
def main():
    # Read data from CSV files and store in dictionaries
    # TODO: Implement the code to read data from the input CSV files and populate the dictionaries

    def read_data_from_csv(file_name):
        data = []
        with open(manufacturer_data, mode='r') as file:
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

manufacturer_dict = create_manufacturer_dict()
price_dict = create_price_dict()
service_date_dict = create_service_date_dict()

# Example usage:
print(manufacturer_dict)
print(price_dict)
print(service_date_dict)


# Generate processed inventory reports
generate_full_inventory()
generate_item_type_inventory()
generate_past_service_date_inventory()
generate_damaged_inventory()

if __name__ == '__main__':
    main()
