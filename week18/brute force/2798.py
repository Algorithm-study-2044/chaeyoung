n, m = map(int, input().split())
nums = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x = nums[i] + nums[j] + nums[k]
            if x <= m:
                result = max(result, x)

print(result)
