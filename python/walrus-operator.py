# chai making system

fruit_stock = ["Mango","Guava","Apple"]

if (fruits := input("Please enter fruit name:") in fruit_stock):
    print("Stock Available")
else:
    print("Stock Unavailable")    