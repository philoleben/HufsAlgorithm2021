n, k = map(int, input().split())
count = 0

while n > 1:
    if (n > 1):
        n /= k
    else:
        n -= 1
    count += 1

print(count)