def excluding_vat_price(price):
    if price is None:
        return -1
    else:
        a= float(price/1.15)
        return round(a,2)
