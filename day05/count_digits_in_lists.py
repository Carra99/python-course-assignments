numbers = [1203, 1256, 312456, 98]

counts = [0] * 10

for number in numbers:
    for digit in str(number):
        counts[int(digit)] += 1

print("Digit Count")

for i, count in enumerate(counts):
    print(f"{i}  {count}")
