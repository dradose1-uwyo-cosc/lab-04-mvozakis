items = ['hotwheels','slim Jims','papertowels','wd-40','chicken']
prices = [1.5,2,8,6,9] # Each value in prices in dollars 

for index in range(len(items)):
    print(f'I bought {items[index]} for ${prices[index]}')

total_price = 0
for price in range(len(prices)):
    total_price=total_price+prices[price]

print(f'I spent ${total_price} at walmart')

print(f'The cheapest item I bought was {items[0]}')

print(f'The most expensive item I bought at Walmart was {items[-1]} ')

least_index = prices.index(min(prices))
most_index = prices.index(max(prices))

print(f'The most expensive item I bought at Walmart was {items.index(most_index)}')

print(f'The cheapest item I bought was {items.index(least_index)}')

print(items.index(least_index))
