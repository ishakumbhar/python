

costs = []

n = int(input("Enter the number of assets: "))

for i in range(n):
    cost = float(input(f"Enter cost of asset {i + 1}: "))
    costs.append(cost)

print("\nOriginal Asset Costs:")
print(costs)


costs.sort(reverse=True)

print("\nAssets Sorted from Highest to Lowest:")
for cost in costs:
    print(f"{cost:.2f}")


print("\nTop Three Priciest Assets:")

limit = min(3, len(costs))

for i in range(limit):
    print(f"{i + 1}. {costs[i]:.2f}")