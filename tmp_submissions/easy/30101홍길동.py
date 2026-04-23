n = int(input())
numbers = list(map(int, input().split()))
max_val = numbers[0]
min_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print(max_val)
print(min_val)
print(max_val + min_val)
