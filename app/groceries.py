
# READ INVENTORY OF PRODUCTS

#products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
#products_df = read_csv(products_filepath)
#products = products_df.to_dict("records")

import os


def to_usd(my_price):
    '''
    this is a docstring it tells us what this function is about.
    what its responsibilities are
    what the params are about
    what datatypes the params are
    what this function will return
    example of invoking the function

    invoke like this: to_usd(9.9999)
    '''

    return '${:,.2f}'.format(my_price)



#create variable for custom products csv file
products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")

#create variable for default products csv file
default_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "default_products.csv")

# checks to see if a products.csv file exists. If not, it uses the default
if os.path.isfile(products_filepath) == True:
    print("USING CUSTOM PRODUCTS CSV FILE...")
    csv_filepath = products_filepath
else:
    print("USING DEFAULT PRODUCTS CSV FILE...")
    csv_filepath = default_filepath


from pandas import read_csv

#reads the csv file into products variable
products = read_csv(csv_filepath)
#pandas transforms the data into a list of dictionaries
products = products.to_dict('records')



# PRINTED INVENTORY REPORT

print("---------")
print("THERE ARE", len(products), "PRODUCTS:")
print("---------")

#for p in products:
    #print("..." + p["name"] + "   " + to_usd(p["price"]))

all_prices = []
for p in products:
    print("..." + p["name"] + "   " + to_usd(p["price"]))
    all_prices.append(float(p["price"]))

import statistics
avg_price = statistics.mean(all_prices)

print("---------")
print("AVERAGE PRICE:", to_usd(avg_price))



# EMAIL INVENTORY REPORT
