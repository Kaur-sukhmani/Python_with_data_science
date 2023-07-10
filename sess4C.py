# to find the min and max
product_prices = [120, 300, 700, 450, 890, 310]
team_points = [2, 5, 8, 9, 10]
salaries = [30000, 90000, 15000, 60000, 45000]

print("PRODUCT PRICES....")
max = product_prices[0]
print("initial max:", max)

for idx in range(1, len(product_prices)):
    print(f"compare {max} with {product_prices[idx]}")
    if product_prices[idx] > max:
        max = product_prices[idx]
        print(f"current max:{max}")

print("Real max is :",max)



print()
print("TEAM POINTS....")
max = team_points[0]
print("initial max:", max)

for idx in range(1, len(team_points)):
    print(f"compare {max} with {team_points[idx]}")
    if team_points[idx] > max:
        max = team_points[idx]
        print(f"current max:{max}")

print("Real max is :",max)


print()
print("SALARIES....")
max =salaries[0]
print("initial max:", max)

for idx in range(1, len(salaries)):
    print(f"compare {max} with { salaries[idx]}")
    if salaries[idx] > max:
        max = salaries[idx]
        print(f"current max:{max}")

print("Real max is :",max)