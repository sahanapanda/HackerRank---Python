#Final Price for Multiple Products

def final_price(prices, discount):
    result = []
    for p in prices:
        result.append(p - (p * discount / 100))
    return result

prices = list(map(float, input("Enter prices: ").split()))
discount = float(input("Enter discount %: "))

print("Final prices:", final_price(prices, discount))
