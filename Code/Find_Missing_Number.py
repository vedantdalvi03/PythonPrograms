numbers = [1, 2, 3, 5, 6]

n = len(numbers) + 1

total = n * (n + 1) // 2

missing = total - sum(numbers)

print("Missing number is:", missing)