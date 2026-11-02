def vat(price,vat_rate):
    """
      calculate the price with VAT included

    """
    return price * (100 + vat_rate)/100

order_price = [100, 200, 300]

for price in order_price:
    bill = vat(price, 20)
    print(f"Price: {price}, Price with VAT: {bill}")
print("VAT calculation completed.")