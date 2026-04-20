with open("numbers.txt", "r") as f:
    nums = [int(line.strip()) for line in f]

print("Numbers:", nums)

print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))

count = sum(1 for n in nums if n > 50)
print("Greater than 50:", count)