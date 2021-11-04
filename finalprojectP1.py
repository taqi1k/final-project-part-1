# Taqi Syed
# 1863528

# Imports
import csv
from datetime import datetime

# Inputs
# Lists for Inputs

mfc_list = []
price_list = []
dates_list = []

# Importing the Manufacturers List
with open("ManufacturerList.csv", 'r') as mf_list:
    mfc = csv.reader(mf_list)
    for line in mfc:
        mfc_list.append(line)

# Importing the Price List
with open("PriceList.csv", 'r') as pricelist:
    price = csv.reader(pricelist)
    for line in price:
        price_list.append(line)

# Importing Service Dates
with open("ServiceDatesList.csv", 'r') as servicedates:
    dates = csv.reader(servicedates)
    for line in dates:
        dates_list.append(line)

# Ordering the Inputted Lists by Order ID
new_mfclist = sorted(mfc_list)

new_pricelist = sorted(price_list)

new_dateslist = sorted(dates_list)

# Importing the missing Dates and Prices to the Final List
for x in range(0, len(new_mfclist)):
    new_mfclist[x].append(price_list[x][1])
for x in range(0, len(new_mfclist)):
    new_mfclist[x].append(dates_list[x][1])

# Transferring to the Final List
final_list = new_mfclist


# Outputs

# Full Inventory Output
# Use of Classes

class FinalOutput:
    def __init__(self, product_list):
        self.product_list = product_list

    def inventory(self):
        with open("FullInventory.csv", 'w') as file:
            products = self.product_list
            keys = sorted(products.keys(), key=lambda x: products[x]['manufacturer'])
        for product in keys:
            id_num = product
            mfc_name = product[products]['manufacturer']
            product_type = product[products]['item type']
            product_price = product[products]['price']
            service_date = product[products]['service date']
            product_dmg = product[products]['damaged']

            # Now all conditions and the order is set for the list
            # Now to Print the updated list with the ordered information

            file.write('{}, {}, {}, {}, {}, {}\n'.format(id_num, mfc_name,
                                                         product_type, product_price,
                                                         service_date, product_dmg))

# Item Type Inventory List Output

    def type(self):
        products = self.product_list
        types = []
        keys = sorted(products.keys())
        for product in products:
            product_type = products[product]['item_type']
            if product_type not in types:
                types.append(product_type)

                # Items are gonna be sorted by the Item ID
                # Each row will contain all the required data

        for type in types:
            file_name = 'Inventory.csv'
            with open('./output_files/' + file_name, 'w') as file:
                for products in keys:
                    id_num = product
                    mfc_name = products[product]['manufacturer']
                    product_price = products[product]['price']
                    service_date = products[product]['service date']
                    product_dmg = products[product]['damaged']
                    product_type = products[product]['item type']

                    # Now all conditions and the order is set for the list
                    # Now to Print the updated list with the ordered information

                    file.write('{}, {}, {}, {}\n'.format(mfc_name, product_price,
                                                        service_date, product_dmg))

# Past Service Date Inventory List Output



    def past_dates(self):
        product = self.product_list
        keys = sorted(product.keys(), key=lambda x: datetime.strptime(product[x]['service date'], "%m/%d/%y").date(), reverse=True)
        with open("PastServiceDateInventory.csv", 'w') as file:
            for products in keys:
                id_num = product
                mfc_name = products[product]['manufacturer']
                product_type = products[product]['item type']
                product_price = products[product]['price']
                service_date = products[product]['service date']
                product_dmg = products[product]['damaged']

            # To Implement the Dates/Expired Service Dates

                present = datetime.now().date()
                exp_date = datetime.strptime(service_date, "%m/%d/%y").date()

            # To Check if Expired

                expired = exp_date < datetime.now()
                if expired:
                    file.write('{}, {}, {}, {}, {}, {}\n'.format(id_num, mfc_name, product_type, product_price,
                                                                 service_date, product_dmg))

# Damaged Inventory List Output

    def damage_inv(self):
        product = self.product_list
        keys = sorted(product.keys(), key=lambda x: product[x]['price'], reverse=True)
        with open("DamagedInventory.csv", 'w') as file:
            for products in keys:
                id_num = product
                mfc_name = products[product]['manufacturer']
                product_type = products[product]['item type']
                product_price = products[product]['price']
                service_date = products[product]['service date']
                product_dmg = products[product]['damaged']

                # To get all the damaged products to be listed

                if product_dmg:
                    file.write('{}, {}, {}, {}, {}\n'.format(id_num, mfc_name, product_type, product_price, service_date))

# Final Output Files (All 4)

    if __name__ == '__main__':
        products = {}
        files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
        # To Format the final Output

        for file in files:
            with open(file, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for line in csv_reader:
                    product_id = line[0]
                    if file == files[0]:
                        products[product_id] = {}
                        mfc_name = line[1]
                        product_type = line[2]
                        product_dmg = line[3]
                        products[product_id]['manufacturer'] = mfc_name.strip()
                        products[product_id]['item type'] = product_type.strip()
                        products[product_id]['damaged'] = product_dmg
                    elif file == files[1]:
                        price = line[1]
                        products[product_id]['price'] = price
                    elif file == files[2]:
                        service_date = line[1]
                        products[product_id]['service date'] = service_date

# Ending Code for Outputs
        output = FinalOutput(products) # I don't understand why the class is undefined?
        output.inventory()
        output.type()
        output.past_dates()
        output.damage_inv()
