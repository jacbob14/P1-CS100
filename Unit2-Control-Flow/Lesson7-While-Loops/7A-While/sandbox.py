# Quick Try 1
n = 1
count = 0
while n <= 1000:
    n = 2 * n
    count += 1
print(count, n)

# Quick try 2 - Sentinel
total = 0
num = int(input("Number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Number (0 to stop): "))
    
print(f"Total: {total}")

