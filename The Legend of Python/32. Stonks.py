stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
    return stock_prices[i-1]

def max_price(a, b):
    mp = 0
    for i in range(a, b+1):
        mp = max(mp, price_at(i))
    return mp

def min_price(a, b):
    mip = price_at(a)
    for i in range(a, b+1):
        mip = min(mip, price_at(i))
    return mip

print(max_price(1, 7))
print(min_price(3, 8))
print(price_at(4))